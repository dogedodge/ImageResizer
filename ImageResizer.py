# -*- coding:utf-8 -*-
import os
from os.path import join, isfile
from PIL import Image

sourceDir = "drawable-xxhdpi"
cwd = os.getcwd()

def resizeImage(fileName, fromDir, toDir, coefficient):
	img = Image.open(fromDir+"/"+fileName)
	
	if coefficient <= 1:
		sampleOpt = Image.ANTIALIAS
	else:
		sampleOpt = Image.BILINEAR
	newImg = img.resize((int(img.size[0]*coefficient), int(img.size[1]*coefficient)), sampleOpt)
	
	if not os.path.exists(toDir):
		os.makedirs(toDir)
	newImg.save(toDir+"/"+fileName);
	print("Done! "+fileName+" width:"+str(newImg.size[0])+" height:"+str(newImg.size[1]))

def resizeImageInDir(fromDir, toDir, coefficient):
	print("Start resize from:"+fromDir+" toDir:"+toDir)
	for name in os.listdir(fromDir):
		if isfile(join(fromDir,name)):
			resizeImage(name, fromDir, toDir, coefficient)
		else:
			resizeImageInDir(join(fromDir,name), join(toDir,name), coefficient)

def resizeImageFromSource(subDir, coefficient):
	global sourceDir, cwd
	resizeImageInDir(join(cwd,sourceDir), join(cwd, subDir), coefficient)

resizeImageFromSource("drawable-hdpi", 480.0/1080)
resizeImageFromSource("drawable-xhdpi", 800.0/1080)