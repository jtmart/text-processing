import os;
import sys;
filePathSrc="C:\\Users\\jtmartelli\\Google Drive\\Textual_analysis\\R\\ambedkargandhiplus\\merge\\beta1.1\\corpus\\shivaniutf8"
for root, dirs, files in os.walk(filePathSrc):
    for fn in files:
      if fn[-4:] == '.txt': #or fn[-4:] == '.csv':
        notepad.open(root + "\\" + fn)
        console.write(root + "\\" + fn + "\r\n")
        notepad.runMenuCommand("Encoding", "Convert to UTF-8")
        notepad.save()
        notepad.close()