import requests
import re


url = 'https://e-smartdata.org/'
website = requests.get(url)
html = website.text
links = re.findall('"((http|ftp)s?://.*?)"', html)
for link in links:
    print(link[0])
