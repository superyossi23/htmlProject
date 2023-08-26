"""
Display all the images in a directory. Rows are sorted by filelist.split('_')[0].
Place "css/styleV1.css" on the same directory as the html.

2022/02/02 Feature: <bgcolor> and <font size> and <font color> added.
2022/02/11 Format reorganized (Paragraph added). natsort added.
2022/10/16 File name will be oscilloscope color.
2023/06/30 v1 released.

"""

from webbrowser import open_new_tab
import os
import sys
from natsort import natsorted
# from htmlModule import *


# --------------------------------------------------------------
# SETTINGS #

wd = r'C:\Users\A\Desktop\pythonProject\stockProject\DATA\png'
col_num = 1
format = '.png'

filelist = os.listdir(wd)  # Work file directory
filelist = list(filter(lambda x: x.endswith(format), filelist))  # Work file
img_dir = wd.split('\\')[-1]
out_filename = img_dir + '\\' + img_dir + '.html'  # Output file name
tab_name = img_dir  # Tab name for html file

# --------------------------------------------------------------
# SORTING #

# filename = 'IMG_'  # (SORTING)
# print('Execute SORTING!!')
# filedict = sort_filelist(filelist, filename)
# print('\nfiledict:\n', filedict)
# filelist = sorted(filedict.values(), key=lambda x:x[0])

# natsort
filelist = natsorted(filelist)
# --------------------------------------------------------------
print('\nfilelist:\n', filelist)

# How to read html base file
# temp_wrapper = 'temp_wrapper.html'
# htmlFile = open(temp_wrapper, 'r', encoding='UTF-8')
# base = htmlFile.read()
base = """
<!DOCTYPE html>
<html>
  <head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>""" + tab_name + """</title>
    <style>
      body {
        background-color: #FFFFFF;
        font-size: 18px;
        color: #000000;
      }
      .index{
        background-color: #000000;
        font-size: 200%;
      }
      .columns{
        background-color: #000000;
        font-size: 100%;
      }
    </style>
  </head>
  <body>
    <p>""" + img_dir + """.html
    </p>
    <table border="0">
    </table>
  </body>
  
</html>
"""
# < link rel = "stylesheet" href = "css/styleV1.css" >
# < body style = "background-color:#000000;" >

# MAIN # -----------------------------------------------------------

body = ""
for i in range(len(filelist)):

    # Oscilloscope color for a file name
    f_spl = filelist[i].split('_')
    font_cnt = ''
    for _ in range(len(f_spl)):
        if   'CH1' in f_spl[_] or 'ch1' in f_spl[_]:
            f_spl[_] = "<font color='ffff00'>" + f_spl[_]  # Yellow
        elif 'CH2' in f_spl[_] or 'ch2' in f_spl[_]:
            f_spl[_] = "<font color='ff00ff'>" + f_spl[_]  # Magenta
        elif 'CH3' in f_spl[_] or 'ch3' in f_spl[_]:
            f_spl[_] = "<font color='0000ff'>" + f_spl[_]  # Blue
        elif 'CH4' in f_spl[_] or 'ch4' in f_spl[_]:
            f_spl[_] = "<font color='00ff00'>" + f_spl[_]  # Green
        else:
            f_spl[_] = "<font color='ffffff'>" + f_spl[_]  # White
        f_colored = '_'.join(f_spl)
        font_cnt += '</font>'
    f_colored = f_colored + font_cnt

    # i = 0
    if i == 0:
        wrapper = """
        <tr>
          <td class="index"><font color="#FFFFFF"><b>""" + filelist[i].split('_')[0] + """</b></font>
          </td>
          <td class="columns"><font color="#FFFFFF">
            <!Write comments below>  <br>
            """ + f_colored + """<br>
            <img src=""" + filelist[i] + """>
          </td>"""
    # Add a column
    elif filelist[i].split('_')[0] == filelist[i - 1].split('_')[0]:
        wrapper = """
          <td class="columns"><font color="#FFFFFF">
            <!Write comments below>  <br>
            """ + f_colored + """<br>
            <img src=""" + filelist[i] + """>
          </td>"""
    # Move on to a new row
    else:
        wrapper = """
        </tr>
        <tr>
          <td class="index"><font color="#FFFFFF"><b>""" + filelist[i].split('_')[0] + """</b></font>
          </td>
          <td class="columns"><font color="#FFFFFF">
            <!Write comments below>  <br>
            """ + f_colored + """<br>
            <img src=""" + filelist[i] + """>
          </td>"""

    # Add wrapper (str) to <body>
    body = body + wrapper


# Insert content between <table> and </table>
index = base.find('</table>')
base = base[:index] + body + base[index:]


# OUTPUT
output = '/'.join(wd.split('\\')[:-1]) + '/' + out_filename
f = open(output, 'w')
f.write(base)
f.close()
print('\nOUTPUT:\n', output)

# # SHOW
# open_new_tab(output)

