#!/usr/bin/env python
# coding: utf-8

# In[80]:


import requests
from bs4 import BeautifulSoup

headers={'User-agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:61.0) Gecko/20100101 Firefox/61.0'}
r = requests.get("http://www.pyclass.com/real-estate/rock-springs-wy/LCWYROCKSPRINGS/", headers=headers)
c=r.content

soup=BeautifulSoup(c,"html.parser")

all=soup.find_all("div",{"class":"propertyRow"})

all[0].find("h4",{"class":"propPrice"}).text.replace("\n","").replace(" ","")

page_nr=soup.find_all("a",{"class":"Page"})[-1].text


# In[82]:


l=[]
base_url="http://www.pyclass.com/real-estate/rock-springs-wy/LCWYROCKSPRINGS/t=0&s="
for page in range(0,int(page_nr)*10,10):
    print(base_url+str(page)+"html")
    r=requests.get(base_url+str(page)+".html", headers=headers)
    c=r.content
    soup=BeautifulSoup(c,"html.parser")
    all=soup.find_all("div",{"class":"propertyRow"})
    for item in all:
        d={}
        d["Address"]=item.find_all("span",{"class","propAddressCollapse"})[0].text
        d["Locality"]=item.find_all("span",{"class","propAddressCollapse"})[1].text
        d["Price"]=item.find("h4",{"class":"propPrice"}).text.replace("\n","").replace(" ","")
        try:
            d["Beds"]=item.find("span",{"class","infoBed"}).find("b").text#numbers of beds#
        except:
            d["Beds"]=None

        try:
            d["Area"]=item.find("span",{"class","infoSqFt"}).find("b").text#square meter#
        except:
            d["Area"]=None

        try:
            d["Full Bath"]=item.find("span",{"class","infoValueFullBath"}).find("b").text#numbers of FullBaths#
        except:
            d["Full Bath"]=None

        try:
            d["Half Bath"]=item.find("span",{"class","infoValueHalfBath"}).find("b").text#numbers of HaldBaths#
        except:
            d["Half Bath"]=None

        for column_group in item.find_all("div",{"class":"columnGroup"}):#i use zip because i want mach spans(group and name)#
            for feature_group, feature_name in zip(column_group.find_all("span",{"class":"featureGroup"}),column_group.find_all("span",{"class":"featureName"})):
                #print(feature_group.text, feature_name.text)
                if "Lot Size" in feature_group.text:
                    d["Lot Size"]=feature_name.text
        l.append(d)


# In[83]:


import pandas
df=pandas.DataFrame(l)


# In[84]:


df


# In[85]:


df.to_csv("Output.csv")


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




