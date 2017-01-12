import sys
import datetime
 
paperhiveID = sys.argv[1]

template = """Dear  {name},
thanks for your offer. The book can be found at

https://paperhive.org/documents/{paperhiveID}

You are assigned the following chapters:

* {chapterlist}

You can either download the PDF, proofread locally and send the corrections in your preferred format, or you can create a Paperhive account and add your suggestions right in your browser.  

Guidelines for proofreaders can be found here
http://langsci-press.org/public/downloads/LangSci_Guidelines_Proofreaders.pdf

We aim at having the corrections in by {duedate}.

Best wishes and thanks again for your help
Sebastian
"""

chapters = ['0']+[l.strip() for l in open("chapternames").readlines()]
assignments = open("assignments").readlines()

mails = []

duedate = (datetime.datetime.now()+datetime.timedelta(days=28)).strftime('%B %d')

for a in assignments:
	name = a.split()[0]
	chapternumbers = a.split()[1:]
	chapterlist = '\n'.join("%s %s"%(i,chapters[int(i)]) for i in chapternumbers)
	#linklist  = '\n'.join(["http://www.glottotopia.org/%s/%s.pdf"%(author,i) for i in chapternumbers])
	#orlist  = "\n".join(["https://via.hypothes.is/http://www.glottotopia.org/%s/%s.pdf"%(author,i) for i in chapternumbers])
	mails.append(template.format(name=name, paperhiveID=paperhiveID,chapterlist=chapterlist,duedate=duedate))
	
separator =	'\n'+80*'-'+'\n'
print separator.join(mails)
