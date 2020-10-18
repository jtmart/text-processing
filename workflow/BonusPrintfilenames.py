from os import listdir
from os.path import isfile, join
MyList = [f for f in listdir('C:\\Users\\jtmartelli\\Google Drive\\Textual_analysis\\R\\ambedkargandhiplus\\merge\\beta1.2\\corpus\\eco_survey_from1998\\edited\\all_utf8_nonum_nostar') if isfile(join('C:\\Users\\jtmartelli\\Google Drive\\Textual_analysis\\R\\ambedkargandhiplus\\merge\\beta1.2\\corpus\\eco_survey_from1998\\edited\\all_utf8_nonum_nostar', f))]

MyFile=open('output.txt','w')

for element in MyList:
     MyFile.write(element)
     MyFile.write('\n')
MyFile.close()