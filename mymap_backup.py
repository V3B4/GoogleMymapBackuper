import xml.etree.ElementTree as ET
import os
import requests
import cv2
import glob

# 設定
kml_dir = 'KML'        # KMLファイルを格納するフォルダ 
image_size = 2048      # 画像の横幅
jpeg_quality = 90      # JPEGの品質
file_extension = 'jpg' # 拡張子(jpg or png)

# KMLファイルを取得
kml_list = glob.glob(kml_dir + '/*.kml')
for kml_path in kml_list:

    # KMLファイルを解析
    print(kml_path)
    root = ET.parse(kml_path).getroot()

    # 名前区間({http://www.opengis.net/kml/2.2})を抽出
    xmlns = root.tag[:-3]

    # マップ名を取得し、出力先のフォルダ名として利用
    out_path = root[0].find(xmlns + 'name').text

    # Documentの子要素であるFolderを抽出
    for folder in root[0].findall(xmlns + 'Folder'):

        # フォルダ名を取得
        folder_name = folder.find(xmlns + 'name').text
        print('・' + folder_name)

        # Placemarkを抽出
        for place in folder.findall(xmlns + 'Placemark'):

            # URLを抽出
            exdata = place.find(xmlns + 'ExtendedData')
            if exdata:
                cdata = exdata.find(xmlns + 'Data').find(xmlns + 'value')
                images = cdata.text.split(' ')

                # 場所名を取得し、保存先のフォルダを作成
                place_name = place.find(xmlns + 'name').text
                place_name = place_name.replace('/', '-') # /を-に置換
                place_name = place_name.replace(' ', '_') # スペースを_に置換
                place_name = place_name.replace('　', '_') # スペースを_に置換
                os.makedirs(out_path + '/' + folder_name + '/' + place_name, exist_ok=True)
                print('　・' + place_name)

                # 画像を保存
                for n, url in enumerate(images, 1):
                    filename = out_path + '/' + folder_name + '/' + place_name + '/' + str(n) + '.png'
                    url = url + '=s' + str(image_size)
                    with open(filename ,mode='wb') as f:
                        f.write(requests.get(url).content)

                    # JPEGに変換
                    if file_extension != 'png':
                        image = cv2.imread(filename)
                        cv2.imwrite(filename.replace('png', file_extension), image, [int(cv2.IMWRITE_JPEG_QUALITY), jpeg_quality])
                        os.remove(filename)
