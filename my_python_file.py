import requests
import datetime

print("--------------------------")
print("Started script main.py")

"""
web1="https://www.salford.gov.uk"
web2="http://www.google.com"
string1="Lucky"
"""

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






"""
print("web1:",response.status_code)
if response.status_code == 200:
    print("The site is up.")
    if string1 in response.text:
        print("The string",string1,"is found.")
    else:
        print("The string",string1,"was not found.")
elif response.status_code == 403:
    print("Access refusal.")
else:
    print("Unsure, please check.")

response=requests.get(web2)
print("web2:",response.status_code)
if response.status_code == 200:
    print("The site is up.")
    if string1 in response.text:
        print("The string",string1,"is found.")
    else:
        print("The string",string1,"was not found.")
elif response.status_code == 403:
    print("Access refusal.")
else:
    print("Unsure, please check.")
"""
