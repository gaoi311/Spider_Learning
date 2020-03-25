import requests

url = "https://www.sogou.com"

response = requests.get(url=url)
text = response.text
print(text)
with open("sogou.html", "w", encoding="utf-8") as f:
    f.write(text)

