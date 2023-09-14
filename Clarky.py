def retrieve(D,Q,K,S,SO,REM,R):
  import requests
  api = "Insert your CSE API Key"
  sid = "Insert your Search Engine ID"
  url = f"https://www.googleapis.com/customsearch/v1?key={api}&cx={sid}&dateRestrict={D}&q={Q}&keywords={K}&start={S}&sort={SO}&num={REM}"
  data = requests.get(url).json()
  search_items = data.get("items")
  for k, search_item in enumerate(search_items, start=1):
   k = k + 1
   R = R + 1
   title = search_item.get("title")
   snippet = search_item.get("snippet")
   link = search_item.get("link")
   print("="*10,f"Result #{R}","="*10)
   print("Title:", title)
   print("Description:", snippet)
   print("URL:", link, "\n")

import requests

query = input("Enter your search terms:")
results = int(input("Enter the number of results that you want(≤100):"))
date = "d"+input("Enter the number of days you want to restrict the search to:")
keywords = input("Enter Keywords (at least 1):")
sort = "date"

quo = int(results/10)
rem = results%10
start = 0
r_num = 0

for i in range(0,quo):
 start = i*10 + 1
 retrieve(date,query,keywords,start,sort,10,r_num)
 r_num = r_num + 10

start = start + 10

if rem>0:
 retrieve(date,query,keywords,start,sort,rem,r_num)
