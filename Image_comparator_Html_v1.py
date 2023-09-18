"""
Display all the images in a directory (also subdirectories). Rows are sorted by filelist.split('_')[0].

2022/02/02 Feature: <bgcolor> and <font size> and <font color> added.
2022/02/11 Format reorganized (Paragraph added). natsort added.
2022/10/16 File name will be oscilloscope color.
2023/06/30 v1 released.
2023/08/26 bg-color changed. black->white. (Table background color remains black)
2023/09/02 Show images also in subdirectories.
2023/09/16 Modified filename's font color.
"""

from webbrowser import open_new_tab
import os
from fnmatch import fnmatch
import sys
from natsort import natsorted
# from htmlModule import *


# --------------------------------------------------------------
# SETTINGS #

wd = r'C:\Users\A\Desktop\pythonProject\stockProject\DATA\png'
format = '*.png'

# --------------------------------------------------------------
# for Pyinstaller #

if getattr(sys, 'frozen', False):
    # Obtain file path from the dif of .exe
    wd = os.path.dirname(sys.executable)
# else:
#     # Obtain file path from the dif of .py
#     wd = os.path.dirname(os.path.abspath(__file__))

# --------------------------------------------------------------
# PROPERTIES #

img_dir = wd.split('\\')[-1]
out_filename = img_dir + '\\' + img_dir + '.html'  # Output file name
tab_name = img_dir  # Tab name for html file

# --------------------------------------------------------------

# --------------------------------------------------------------

# Create a filelist
filelist = []
for path, subdirs, files in os.walk(wd):
    print('Adding files in %s...' % (path))
    for name in files:
        if fnmatch(name, format):
            print(os.path.join(path, name))
            if path.split(wd.split('\\')[-1]+'\\')[-1] == path:
                filelist.append(name)  # for root dir
            else:
                filelist.append(path.split(wd.split('\\')[-1]+'\\')[-1] + '\\' + name)  # for sub dir


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
        font-size: 20px;
        color: #000000;
      }
      img{
      height: 400px;
      }
      
      .index{
        background-color: #000000;
        font-size: 80%;
      }
      .columns{
        background-color: #000000;
        font-size: 60%;
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

    font_cnt = ''

    font_cnt += '</font>'
    if '.png' in filelist[i]:
        new_name = "<font color='#ffffff'>" + filelist[i].split('.png')[0]  # White
    if '.jpg' in filelist[i]:
        new_name = "<font color='#ffffff'>" + filelist[i].split('.jpg')[0]  # White

    if   '_CH1-' in new_name or '_ch1-' in new_name:
        new_name = new_name.replace('_ch1-', "<font color='#ffffff'>" + '_ch1-' + "<font color='#ffff00'>")  # Yellow
        font_cnt += '</font>'
    if '_CH2-' in new_name or '_ch2-' in new_name:
        new_name = new_name.replace('_ch2-', "<font color='#ffffff'>" + '_ch2-' + "<font color='#ff00ff'>")  # Magenta
        font_cnt += '</font>'
    if '_CH3-' in new_name or '_ch3-' in new_name:
        new_name = new_name.replace('_ch3-', "<font color='#ffffff'>" + '_ch3-' + "<font color='#0000ff'>")  # Blue
        font_cnt += '</font>'
    if '_CH4-' in new_name or '_ch4-' in new_name:
        new_name = new_name.replace('_ch4-', "<font color='#ffffff'>" + '_ch4-' + "<font color='#00ff00'>")  # Green
        font_cnt += '</font>'

    font_cnt += '</font>'
    if '.png' in filelist[i]:
        f_colored = new_name + "<font color='#ffffff'>.png" + font_cnt
    if '.jpg' in filelist[i]:
        f_colored = new_name + "<font color='#ffffff'>.jpg" + font_cnt


    # i = 0
    if i == 0:
        wrapper = """
        <tr>
          <td class="index"><font color="#FFFFFF"><b>""" + filelist[i].split('_')[0].replace('\\', '<br>') + """</b></font>
          </td>
          <td class="columns">
            <font color="#FFFFFF"><!Remarks> - <br></font>
            """ + f_colored + """<br>
            <img src=""" + filelist[i] + """>
          </td>"""
    # Add a column
    elif filelist[i].split('_')[0] == filelist[i - 1].split('_')[0]:
        wrapper = """
          <td class="columns">
            <font color="#FFFFFF"><!Remarks> - <br></font>
            """ + f_colored + """<br>
            <img src=""" + filelist[i] + """>
          </td>"""
    # Move on to a new row
    else:
        wrapper = """
        </tr>
        <tr>
          <td class="index"><font color="#FFFFFF"><b>""" + filelist[i].split('_')[0].replace('\\', '<br>') + """</b></font>
          </td>
          <td class="columns"><font color="#FFFFFF">
            <!Remarks> - <br></font>
            """ + f_colored + """<br>
            <img src=""" + filelist[i] + """>
          </td>"""

    # Add wrapper (str) to <body>
    body = body + wrapper


# Insert content between <table> and </table>
index = base.find('</table>')
base = base[:index] + body + base[index:]


# OUTPUT
output = '\\'.join(wd.split('\\')[:-1]) + '\\' + out_filename
f = open(output, 'w')
f.write(base)
f.close()
print('\nOUTPUT:\n', output)

# # SHOW
# open_new_tab(output)

