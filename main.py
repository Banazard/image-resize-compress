import sys
import shutil
import os
from PIL import Image, ImageSequence

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.

def import_folder(path):
    # make a new directory
    if not os.path.exists(f"{path}resized/"):
        os.makedirs(f"{path}resized/")
    # put a list of filenames(jpg, png, gif) to files
    files = []
    for file in os.listdir(path):
        if file.endswith('.png') or file.endswith('.jpg'):
            files.append(file)
    return files

def resize(path, files):
    for file_name in files:
        img = Image.open(f"{path}{file_name}")
        width = 1000 # you can set maximum width here
        height = round(img.height * width / img.width)

        if(img.width > width and file_name.endswith('.gif')):
            # Get sequence iterator
            frames = ImageSequence.Iterator(img)

            # Wrap on-the-fly thumbnail generator
            def thumbnails(frames):
                for frame in frames:
                    thumbnail = frame.copy()
                    thumbnail.thumbnail((width, height), Image.Resampling.NEAREST)
                    yield thumbnail

            frames = thumbnails(frames)

            # Save output
            om = next(frames)  # Handle first frame separately
            om.info = img.info  # Copy sequence info
            om.save(f"{path}resized/{file_name}", quality=85, optimize=True , save_all=True, append_images=list(frames))
        # over 1000px
        elif (img.width > width):
            img = img.resize((width, height), Image.Resampling.LANCZOS)
            img.save(f"{path}resized/{file_name}", quality=85,optimize=True)
        else:
            img.save(f"{path}resized/{file_name}", quality=85, optimize=True)
            # shutil.copyfile(f"{path}{file_name}", f"{path}resized/{file_name}")

        # if the image width is over 1001px resize it to 1000px
        # save with new name

def shrink():
    pass

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    path = 'C:/Users/malib/Downloads/NVSO/media/'
    files = import_folder(path)
    resize(path, files)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
