import requests

url = "http://img5.imgtn.bdimg.com/it/u=766812076,75558733&fm=26&gp=0.jpg"
img_data = requests.get(url=url).content

with open("新垣结衣.jpg", "wb") as f:
    f.write(img_data)