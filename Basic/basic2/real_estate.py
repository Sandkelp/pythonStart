from bs4 import BeautifulSoup
import requests
import pandas as pd
df = pd.DataFrame(columns=["Price","Address","Town","Beds","Baths"])

r = requests.get("http://www.pyclass.com/real-estate/rock-springs-wy/LCWYROCKSPRINGS/", headers={'User-agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:61.0) Gecko/20100101 Firefox/61.0'})
c = r.content
soup = BeautifulSoup(c,"html.parser")
all = soup.find_all("div",{"class":"propertyRow"})
for item in all:
    df=df.append({"Price":item.find("h4",{"class":"propPrice"}).text.replace("\n","").replace(" ","")}, ignore_index=True)
    print(item.find("h4",{"class":"propPrice"}).text.replace("\n","").replace(" ",""))
    df=df.append({"Address":item.find_all("span",{"class","propAddressCollapse"})[0].text},ignore_index=True)
    print(item.find_all("span",{"class","propAddressCollapse"})[0].text)
    df=df.append({"Town":item.find_all("span",{"class","propAddressCollapse"})[1].text},ignore_index=True)

    print(item.find_all("span",{"class","propAddressCollapse"})[1].text)
    try:
        df=df.append({"Beds":item.find("span",{"class","infoBed"}).text},ignore_index=True)
        print(item.find("span",{"class","infoBed"}).text)
    except:
        df=df.append({"Beds":"None"},ignore_index=True)
    try:
        df=df.append({"Baths":item.find("span",{"class","infoValueFullBath"}).text},ignore_index=True)
        print(item.find("span",{"class","infoValueFullBath"}).text)
    except:
        df=df.append({"Baths":"None"},ignore_index=True)

    for column_group in item.find_all("div",{"class":"columnGroup"}):
        for feature_group, feature_name in zip(column_group.find_all("span",{"class":"feartureGroup"}),column_group.find_all("span",{"class":"featureName"})):
           print(feature_group.text, feature_name.text)

df.to_csv("real_estate.csv")

