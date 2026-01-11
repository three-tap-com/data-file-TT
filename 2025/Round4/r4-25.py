from bs4 import BeautifulSoup
import pandas as pd

rows_data = []

with open("r4-25.html", "r", encoding="utf-8") as f:
    soup = BeautifulSoup(f, "html.parser")

# find all table rows (skip header row)
rows = soup.find_all("tr")[1:]

for row in rows:
    cols = row.find_all("td")

    if len(cols) < 7:
        continue  # safety check

    rows_data.append({
        "Institute": cols[0].get_text(strip=True),
        "Branch": cols[1].get_text(strip=True),
        "Quota": cols[2].get_text(strip=True),
        "Category": cols[3].get_text(strip=True),
        "Gender": cols[4].get_text(strip=True),
        "OpenRank": cols[5].get_text(strip=True),
        "CloseRank": cols[6].get_text(strip=True),
    })

df = pd.DataFrame(rows_data)
df.to_csv("R4-25.csv", index=False)

print("✅ CSV created successfully")
