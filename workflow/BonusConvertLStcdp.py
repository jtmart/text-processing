import pandas as pd
import os
import random
import datetime
import re

Sessions = [13,14,15,16]
Govts = ['nda1','upa1','upa2','nda2']

Questions = pd.read_csv('./TCPD_QH.csv', sep=',', index_col=False, encoding='utf-8', error_bad_lines=False)
#df = pd.read_csv('Test.csv', header=None, sep='\n')
#for Row in Questions:
#	Questions[Row] = Questions[Row].str.split('","', expand=True)

print(list(Questions))
print(len(list(Questions)))
print(len(Questions))

PathFinal = os.getcwd()
No = 1

with open('Metadata_LS.csv','a',encoding='utf-8') as fd:
	print('File Opened')
	for Ind in range(4):
		Session = Sessions[Ind]
		Govt = Govts[Ind]
		print(Govt,Session)
		QOld = pd.read_csv('./ls'+str(Session)+'_Q.csv', sep=',', index_col=False, encoding='utf-8')
		for Row in range(len(Questions)):
		
			if (Questions.loc[Questions.index[Row],'ls_number'] == Session):

				Text = Questions.loc[Questions.index[Row],'answer_text']
				Question = Questions.loc[Questions.index[Row],'question_text']
				if (Question!="URL_Not_Found"):
					Date = Questions.loc[Questions.index[Row],'date']
					QMinistry = Questions.loc[Questions.index[Row],'ministry']
					print(Date,Row,Text)
					try:
						DateFull = datetime.datetime.strptime(Date,'%Y-%m-%dT00:00:00').strftime('%Y/%m/%d')
					except ValueError:
						DateFull = datetime.datetime.strptime(Date,'%Y- %m- %dT00:00:00').strftime('%Y/%m/%d')
					# except KeyError:
					# 	BT+=1
					# 	DateFull = datetime.datetime.strptime(Questions.loc[Questions['ID']==CID,'date'][Row-BT],'%d.%m.%Y').strftime('%Y/%m/%d')
					# 	Text = Answers.loc[Answers['ID']==CID,'Answers'][Row-BT]
					# 	QLink = Questions.loc[Questions['ID']==CID,'Q_Link'][Row-BT]
					# 	Question = Questions.loc[Questions['ID']==CID,'Question'][Row-BT]
					# 	QMinistry = Questions.loc[Questions['ID']==CID,'ministry'][Row-BT]
					# 	Details = Questions.loc[Questions['ID']==CID,'subject'][Row-BT]
					
					DateFull = DateFull.split('/')
					
					Token = str(random.randint(0,999999))
					if (len(Token)<6):
						Token = '0'*(6-len(Token)) + Token

					Year = DateFull[0]
					Month = Year + DateFull[1]
					Day = Month + DateFull[2]

					Id = 't'+Day+Token
					FileName = Id+".txt"
					
					try:
						OB = Text.find('(')
						CB = Text.find(')')
					#Designation = Text[0:OB]
						Loc = Text[OB+1:CB]
						Answer = Text[CB+1:]
						if (Loc=='a'):
							Loc = 'na'
							Answer = Text[OB+1:]
						
						#Answer = str(Answer.encode("utf-8"))

						QID = str(Questions.loc[Questions.index[Row],'id'])

						QLink = QOld.loc[QOld['ID']==QID,'Q_Link']
						
						Details = QOld.loc[QOld['ID']==QID,'subject']
						QLoc = Questions.loc[Questions.index[Row],'member']
						Party = Questions.loc[Questions.index[Row],'party']
						Const = Questions.loc[Questions.index[Row],'constituency']
						State = Questions.loc[Questions.index[Row],'state']
						Sex = Questions.loc[Questions.index[Row],'gender']
						ConstType = Questions.loc[Questions.index[Row],'constituency_type']
						
						ConcatStr = Details+'/'+QLoc+'/'+Party+'/'+Const+'/'+State+'/'+Sex+'/'+ConstType
						
						#Question = Question.replace(';',' ')

						Answer = re.sub(r'\.+', ".", Answer)
						Answer = re.sub(r'\.\s+', ".", Answer)
						Answer = re.sub(r'\.+', ".", Answer)

						Answer = re.sub(r'\*+', "", Answer)
						Answer = re.sub(r'\*\s+', "", Answer)
						Answer = re.sub(r'\*+', "", Answer)

						Question = re.sub(r'\.+', ".", Question)
						Question = re.sub(r'\.\s+', ".", Question)
						Question = re.sub(r'\.+', ".", Question)

						Question = re.sub(r'\*+', "", Question)
						Question = re.sub(r'\*\s+', "", Question)
						Question = re.sub(r'\*+', "", Question)

						f = open(PathFinal+"\\TextFiles\\"+FileName, "a",encoding="utf-8")
						f.write(Answer)
						f.close()

						fd.write('\n'+str(Id)+',loksabha,minister,'+str(Year)+','+str(Month)+','+str(Day)+',mp,'+str(Session)+','+Govt+',nationalpol,qanda,na,na,na,"'+str(QMinistry)+'",india,ncr,newdelhi,capital,hindiorenglish,"'+str(ConcatStr)+'","'+str(Question)+'","'+str(QLink)+'",loksabha'+str(Year)+','+str(No)+','+str(No+8637)+',notrans,rahul,others,others,others,others,others,others,others,others,others,others,others,others,others,others,others,others,others,others,others,others,others,others,others,loksabha,others,others,others,others,'+str(Loc)+',yes')
						print(No)
						No+=1
					except AttributeError:
						continue