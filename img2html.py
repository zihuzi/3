#! python3
# -*- coding: utf-8 -*-
import os

html = '''<!DOCTYPE html>
<html>
<head>
  <meta charset="utf-8">
  <title></title>
  <style>
    p{
      text-align: center;
    }
    img{
      width:;
      height:;
    }
  </style>
</head>
<body>
  <p><img src="image/xyz" /></p>
</body>
</html>'''

# a
# fileList = ['i-000.jpg', 'i-001.jpg']

# b
filePath = os.path.join(os.getcwd(), 'image')
fileList = os.listdir(filePath)

for i in range(len(fileList)):
    htmlFileName = "{:0>3d}".format(i + 1) + '.html'
    htmlFileText = html.replace('xyz', fileList[i])
    with open(htmlFileName, 'w', encoding='utf-8') as f:
        f.write(htmlFileText)
        print(fileList[i] + ' work done.')
print('all done.')
