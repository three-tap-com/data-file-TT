import requests
from bs4 import BeautifulSoup
import pandas as pd

data={'Institute':[],'Branch':[],'Quota':[],'Category':[],'Gender':[],'OpenRank':[],'CloseRank':[]}

with open("R3-24.html","r") as f:
    html_doc = f.read()

soup = BeautifulSoup(html_doc, 'html.parser')

# Find all td elements with id="Institute"
institute_tags = soup.find_all('td', id='Institute')
filtered_institute_tags = [tag for tag in institute_tags if not tag.find('span')]
for tag in filtered_institute_tags:
    text = tag.get_text(strip=True)
    print(text)
    data["Institute"].append(text)
    
spans=soup.select("span#ctl00_ContentPlaceHolder1_GridView1_lblBranch") #branch
for span in spans:
    print(span.string)
    data["Branch"].append(span.string)

spans=soup.select("span#ctl00_ContentPlaceHolder1_GridView1_lblQuota") #quota
for span in spans:
    print(span.string)
    data["Quota"].append(span.string)

spans=soup.select("span#ctl00_ContentPlaceHolder1_GridView1_lblCategory") #category
for span in spans:
    print(span.string)
    data["Category"].append(span.string)

spans=soup.select("span#ctl00_ContentPlaceHolder1_GridView1_lblGender") #gender
for span in spans:
    print(span.string)
    data["Gender"].append(span.string)

spans=soup.select("span#ctl00_ContentPlaceHolder1_GridView1_lblOpenRank") #open rank
for span in spans:
    print(span.string)
    data["OpenRank"].append(span.string)
    
spans=soup.select("span#ctl00_ContentPlaceHolder1_GridView1_lblCloseRank") #closed rank
for span in spans:
    print(span.string)
    data["CloseRank"].append(span.string)

df = pd.DataFrame.from_dict(data)
df.to_csv("R2.csv",index=False)
