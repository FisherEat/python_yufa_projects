
from datetime import datetime

now = datetime.now()

print(now.timestamp())

dt = datetime(2018,1,12,0,0)
print(dt)

from  collections import  namedtuple

Point = namedtuple('Point', ['x', 'y'])
p = Point(1,2)

print(p.x)
print(p.y)

from collections import deque
q = deque(['z', 'c', 's'])
q.append('x')
q.appendleft('y')
print(q)

import base64

print(base64.b64decode(b'binary\x00string'))

n = 10240099
b1 = (n&0xff000000) >> 24
print(b1)

import hashlib

md5 = hashlib.md5()
md5.update('how to use md5 in python hashlib?'.encode('utf-8'))
print(md5.hexdigest())

# from urllib import  request
# with request.urlopen('https://api.douban.com/v2/book/2129650') as f:
#     data = f.read()
#     print('Status:', f.status, f.reason)
#     for k,v in f.getheaders():
#         print('%s:%s' % (k,v))
#     print ('Data:', data.decode('utf-8'))


from PIL import  Image

im = Image.open('test.jpg')
w,h = im.size

print('Original image size: %sx%s' % (w,h))
im.thumbnail((w//2, h//2))

print('Resize image to: %sx%s' % (w//2, h//2))

from PIL import  Image, ImageFilter

im = Image.open('test.jpg')
im2 = im.filter(ImageFilter.BLUR)
im2.save('blue.jpg', 'jpeg')


from PIL import Image, ImageDraw, ImageFont, ImageFilter

import random

# 随机字母:
def rndChar():
    return chr(random.randint(65, 90))

# 随机颜色1:
def rndColor():
    return (random.randint(64, 255), random.randint(64, 255), random.randint(64, 255))

# 随机颜色2:
def rndColor2():
    return (random.randint(32, 127), random.randint(32, 127), random.randint(32, 127))

# 240 x 60:
width = 60 * 4
height = 60
image = Image.new('RGB', (width, height), (255, 255, 255))
# 创建Font对象:
font = ImageFont.truetype('Arial.ttf', 36)
# 创建Draw对象:
draw = ImageDraw.Draw(image)
# 填充每个像素:
for x in range(width):
    for y in range(height):
        draw.point((x, y), fill=rndColor())
# 输出文字:
for t in range(4):
    draw.text((60 * t + 10, 10), rndChar(), font=font, fill=rndColor2())
# 模糊:
image = image.filter(ImageFilter.BLUR)
image.save('code.jpg', 'jpeg')