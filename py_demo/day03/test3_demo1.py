#coding: utf-8

import Image, ImageFont, ImageDraw

myPath = "/home/itcast/ace/media/"
fontPath = "/home/itcast/ace/media/"

inputFile = "ace.jpg"

outputFile = "output.jpg"

#打开图片
im = Image.open(myPath + inputFile)
draw = ImageDraw.Draw(im)

#根据图片大小确定字体大小
fontsize = min(im.size)/4

#加文字
myfont = ImageFont.truetype(fontPath + 'simhei.ttf', fontsize)

#通过画家 在 图片上画出 文字
draw.text((im.size[0]-fontsize, 0), '6', font = myfont, fill = (256,0,0))

im.save(myPath + outputFile, "jpeg")

