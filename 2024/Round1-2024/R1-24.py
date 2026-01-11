import pandas as pd
from bs4 import BeautifulSoup

data = []

with open("R1-24.html", "r", encoding="utf-8") as f:
    soup = BeautifulSoup(f, "html.parser")

# Each row in JoSAA table
rows = soup.select("tr")

for row in rows:
    institute = row.find("td", id="Institute")
    branch = row.find("span", id="ctl00_ContentPlaceHolder1_GridView1_lblBranch")
    quota = row.find("span", id="ctl00_ContentPlaceHolder1_GridView1_lblQuota")
    category = row.find("span", id="ctl00_ContentPlaceHolder1_GridView1_lblCategory")
    gender = row.find("span", id="ctl00_ContentPlaceHolder1_GridView1_lblGender")
    open_rank = row.find("span", id="ctl00_ContentPlaceHolder1_GridView1_lblOpenRank")
    close_rank = row.find("span", id="ctl00_ContentPlaceHolder1_GridView1_lblCloseRank")

    if institute and branch and quota and category and gender and open_rank and close_rank:
        data.append({
            "Institute": institute.get_text(strip=True),
            "Branch": branch.get_text(strip=True),
            "Quota": quota.get_text(strip=True),
            "Category": category.get_text(strip=True),
            "Gender": gender.get_text(strip=True),
            "OpenRank": open_rank.get_text(strip=True),
            "CloseRank": close_rank.get_text(strip=True)
        })

df = pd.DataFrame(data)

# Save CSV in SAME folder
df.to_csv("R1-24.csv", index=False)

print("✅ CSV file created successfully")
print(df.head())