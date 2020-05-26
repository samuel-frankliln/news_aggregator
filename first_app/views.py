from django.shortcuts import render
from django.http import HttpResponse
import requests
import urllib.request
import re
from bs4 import BeautifulSoup
# Create your views here.

# def index(request):
#     return HttpResponse("Hello World!")
string=["COVOID-19"]

def index(request):
    return render(request,'first_app\index.html')

def international(request):
    return render(request,'first_app/international.html')
def national(request):
    return render(request,  'first_app/national.html')

who_r = requests.get("https://www.who.int/emergencies/diseases/novel-coronavirus-2019/media-resources/news")
who_soup = BeautifulSoup(who_r.content, 'lxml')
who_soup1 = BeautifulSoup(who_r.content,'lxml')
who_headings = who_soup.find_all("div", {"class": "info"})
who_headings2= who_soup.find_all("div", {"class": "link-container"},"a")




who_news = []
who_link =[]
who_up=[]
who_linkup=[]


# list=["COVOID-19",""]
for th in who_headings:
    who_news.append(th.text)

for th in who_headings2:
    who_news.append(th.text)

for ti in range(len(who_news)):
    if(who_news[ti].find("COVID-19")>0):
        who_up.append(who_news[ti])



#for REUTERS

bbc_r = requests.get("https://www.feedspot.com/?_src=folder")
bbc_soup = BeautifulSoup(bbc_r.content, 'lxml')
bbc_headings = bbc_soup.find_all("div", {"class": "rssitem"})



bbc_news = []

for bc in bbc_headings:
    bbc_news.append(bc.text)

def bbc(req):
    return render(req, "first_app\BBC.html", {'bbc_news':bbc_news})



def check(string, sub_str):
    if (string.find(sub_str) == -1):
        print(string)

def who(req):
    return render(req, 'first_app\who.html', {'who_news':who_up})




# GEtting news from Times of India

toi_r = requests.get("https://timesofindia.indiatimes.com/briefs")
toi_soup = BeautifulSoup(toi_r.content, 'lxml')

toi_headings = toi_soup.find_all("h2")

toi_headings = toi_headings[0:-13] # removing footers

toi_news = []

for th in toi_headings:
    toi_news.append(th.text)




ht_r = requests.get("https://www.hindustantimes.com/india-news/")
ht_soup = BeautifulSoup(ht_r.content, 'lxml')
ht_headings = ht_soup.findAll("div", {"class": "headingfour"})
ht_headings = ht_headings[2:]
ht_news = []

for hth in ht_headings:
    ht_news.append(hth.text)


def toi(req):
    return render(req, 'first_app/toi.html', {'toi_news':toi_news})


def ht(req):
    return render(req, 'first_app/ht.html', {'ht_news': ht_news})
