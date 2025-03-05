import requests
import datetime

# print("________________")
print("Started script main.py")


websites=[
    {"url":"https://www.salford.gov.uk","keyword":"abc"},
    {"url":"https://www.google.com","keyword":"Lucky"},
    {"url":"https://www.facebook.com","keyword":"Facebook"}
    ]

for web in websites:
    print("\n",datetime.datetime.now())
    response=requests.get(web["url"])
    keyword=web["keyword"]
    print("Checking",web["url"])
    print("Response:",response.status_code)
    if response.status_code == 200:
        print("The site is up.")
        if keyword in response.text:
            print("Keyword",keyword,"is found.")
        else:
            print("Keyword",keyword,"was not found.")
    elif response.status_code == 403:
        print("Access refusal.")
    else:
        print("Unsure, please check.")





