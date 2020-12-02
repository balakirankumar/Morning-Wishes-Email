# __AUTHOR__   :   BalaKiranKumar



#Import required modules  

import os
import smtplib
from email.message import EmailMessage
import requests
import lxml
from bs4 import BeautifulSoup
import random

# take passwords from other file or from environ variables
EMAIL_ADDRESS=os.environ.get('Email_mail')
EMAIL_PASSWORD=os.environ.get('Email_pass')

#url to scrap
url='http://quotes.toscrape.com/tag/'
type_=["love","inspirational","life","humor","books","reading","friendship","friends","truth","simile",]
url_final=url+random.choice(type_)+"/"

#making request to url
r=requests.get(url_final)
# getting into lxml form
soup=BeautifulSoup(r.text,'lxml')

#getting required data
quotes=soup.find_all('span',class_='text')
author=soup.find_all('small',class_='author')
tags=soup.find_all('div',class_='tags')

#To select a random quote from the list all quotes are appended to this list
quotes_l=[]
author_l=[]
tags_l=[]

# getting text from lxml code
for i in range(len(quotes)):
    quotes_l.append(quotes[i].text)
    author_l.append(author[i].text)
    tag=tags[i].find_all('a',class_='tag')
    t=""
    for j in tag:
        t+=", #"+j.text
    tags_l.append(t.lstrip(", "))
len_lists=len(quotes_l)
numb=random.randrange(0,len_lists)-1

#msg composing to
contacts = ["Reciever1@gmail.com","Reciever2@gmail.com","so_on@gmail.com"]
subject= "Good Morning "
content=f"Quote: {quotes_l[numb]} \nAuthor: {author_l[numb]}. \nTags: {tags_l[numb]}."

msg = EmailMessage()
msg['Subject'] = subject
msg['From'] = EMAIL_ADDRESS
msg['Bcc'] = contacts
msg.set_content(content)


with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
	smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
	smtp.send_message(msg)