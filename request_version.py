import requests

res = requests.get("http://www.google.com/")
print(res.text)
res1 = requests.get("https://raw.githubusercontent.com/JoshuaN18/CMPUT-404-Labs/main/request_version.py")
print(res1.text)
