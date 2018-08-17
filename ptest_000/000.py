
from PIL import Image, ImageDraw, ImageFont

def add_num(img):
    draw = ImageDraw.Draw(img)
    myfont = ImageFont.truetype('/Users/gl/Desktop/mui.ttf')
    fillColor = "#ff0020"
    width, height = img.size
    draw.text((width-40, 0), "gaolong", font=myfont, fill=fillColor)
    img.save('result.jpg', 'jpeg')
    print("OK")

    return 0


if  __name__ == '__main__':
    image = Image.open('/Users/gl/Desktop/图片/pig.jpg')
    add_num(image)