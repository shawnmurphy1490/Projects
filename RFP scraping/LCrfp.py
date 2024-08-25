import requests
import bs4

#TODO: pull LCBDD rfp website from web

#TODO: Save site as rfp.html

#using rfp.html in bs4
exampleFile = open("rfp.html")
exampleSoup = bs4.BeautifulSoup(exampleFile.read(), 'html.parser')

#finding the specific rfp elements - title and description
rfpTitle = exampleSoup.select('.testimonial-entry-title')
rfpElems = exampleSoup.select('.testimonial-entry-details')

#Iteration through all rfp title and descriptions
#TODO: change print statments to save into document of some sort
for i in range(len(rfpElems)):
    print(rfpTitle[i].getText())
    print(rfpElems[i].getText())
    print()

#TODO opening master RFP file  

#TODO comparing lake county file to master with for loop and IF ELSE

#TODO write new RFPs to master file with datestamp