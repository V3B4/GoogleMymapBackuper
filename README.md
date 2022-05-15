# GoogleMymapBackuper

Googleマイマップにアップロードした画像をダウンロードするツール
![](https://cdn-ak.f.st-hatena.com/images/fotolife/V/V3B4/20211012/20211012171135.png)
をダウンロード
![](https://cdn-ak.f.st-hatena.com/images/fotolife/V/V3B4/20211012/20211012171552.png)
解像度や保存形式(PNG,JPEG)の選択可

## Requirements
- Python3
    - ElementTree
    - OpenCV (JPEGに変換する場合)

## Usage
1. KMLファイルをダウンロード
1. KMLファイルを指定のフォルダに格納
1. 必要に応じてmymap_backup.py内の設定を変更
1. `pip3 install lxml opencv-python`
1. `python3 mymap_backup.py`
