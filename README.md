# name
image resize/compress program

## Overview
- This program can resize/compress images.
- At this moment the program resize/compress PNG, jpg files.

- このプログラムは画像のリサイズ、圧縮を一括で行います。
- 現段階で対応している画像の拡張子はpng,jpgです。（gifなど未対応の画像データががフォルダ内にある場合無視します。）

## Requirement
- PyCharm (Python IDE)
- Pillow (Python library)

## Usage
1. Change the path at line 60 to the directory path where the target images exist.
    - No escape sequence
    - Do not use "\" to the path use "/"
    - the path should end with "/"
1. Run the program
1. Resized images are in "/Resized" directory.

1. 60行目のpath(''内)を画像ファイルのあるディレクトリにする。pathの変更は以下に注意。
    - エスケープ文字がpathに入らないようにする。
    フォルダ名先頭を数字にしない。
    フォルダ名に記号"("や"~"を使用しない。
    アンダーバー"_"は可。 -フォルダ階層がバックスラッシュ"\"で区切られてる場合はスラッシュ"/"に書き直す。（windowsのエクスプローラからアドレスをコピペした場合は階層がバックスラッシュになる）
    - pathの最後はスラッシュでを付ける。
    
    上手くいかない例. C:\Users\Banazard\Downloads\NVSO\images
    成功する例. C:/Users/Banazard/Downloads/NVSO/images/
    
1. プログラムを実行
1. リサイズされた画像は設定したpath内に自動で新規作成されるResizedフォルダ内にあります。

## Features

## Reference

## Author
Banazard

## Licence

