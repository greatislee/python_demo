#!/usr/bin/env python
# coding=utf-8



import Image,ImageFont,ImageDraw

myPath ="./"
fontPath = "./"

inputFIle = "1.png"

outputFile ="x.jpg"

#打开图片
im = Image.open(myPath+inputFIle)
draw = ImageDraw.Draw(im)

#根据图片大小确定字体大小
fontsize = min(im.size)/4

#加文字
myfont = ImageFont.truetype(fontPath+'xxx.ttf',fontsize)

#通过画家 在图片上画出文字
draw.text((im.size[0]-fontsize,0),'6',font = myfont,fill =(256,0,0))

im.sava(myPath+outputFile,"jpeg")
