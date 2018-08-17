# -*- coding: utf-8 -*-

import codecs

def openTxt():
    file = codecs.open('myText.txt', 'w', 'utf-8')
    file.write("hah啊")
    file.close()

    #使用codecs.open能解决该问题
    # with codecs('myText.txt', 'w', 'utf-8') as f:
    #    try:
    #         str_1 = "我是高龙"
    #         f.write(str_1)
    #         print("write into open.txt succeed!")
    #    except:
    #        print("write into myText.txt failed")

if __name__ == '__main__':
    openTxt()