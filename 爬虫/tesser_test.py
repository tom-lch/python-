import pytesseract
from PIL import Image, ImageEnhance
img = Image.open('ric6.png')
#转化为灰度图片
img = img.convert('L')
#img.show()

#二值化处理
threshold = 140
table = []
for i in range(256):
    if i < threshold:
        table.append(0)
    else:
        table.append(1)
out = img.point(table, '1')
#out.show()
#输出
img = out.convert('RGB')
print(pytesseract.image_to_string(img))