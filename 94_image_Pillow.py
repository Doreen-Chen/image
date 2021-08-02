# 94. 圖片處理 - (如何寫自己的程式示範)
#
#   print(type(impage_file)) : 列印物件名稱
#

from PIL import Image
import os


# 列出資料夾裡所有檔名
#for file in os.listdir('.'):  # '.' 現在位置
#    print(file)


# 列出資料夾裡所有"圖檔png"檔名
for file in os.listdir('original'):  # '.' 現在位置; 指定資料夾 'Picture'
    if file.endswith('.png'):
        #print(file)

        # 路徑 concatenate uses 'os.path.join()'
        impage_file = Image.open(os.path.join('original', file))  # open colour image
        #print(type(impage_file))  # print:  <class 'PIL.PngImagePlugin.PngImageFile'>

        # 參數
        # '1' = convert image to black and white
        # 'L' = convert image to gray
        impage_file = impage_file.convert('L')

        # file[:-4] 檔名 flower.png 取開始到倒數第4個位置 --> 'flower'
        impage_file.save(os.path.join('result', file[:-4] + '_gray.png'))  # [:-4] = 開始到倒數第4個位置

    # startswith()
    if file.startswith('flower'):
        print('--- startswith = flower --- ', file)



### review : 77. 清單的分割
#    list_a[開始值:結束值]  : 開始有包含,結束不包含
# e.g.
#    n[:3]   ==> 取得前三個, 開始值是0可以不用寫
#    n[2:4]  ==> 取得index=2,3不包含4。 一個清單裝著n[2]跟n[3]
#    n[-2:]  ==> 取得最後2個，負數表示倒數第幾個。 結尾值不寫表示到底