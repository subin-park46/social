from bs4 import BeautifulSoup
from urllib.request import urlopen

soup = BeautifulSoup(urlopen("http://www.networksciencelab.com/"), "html.parser")

href = soup.find(href = "v2.jpg")
print(href)

links = soup.find_all("a")
firstLink = links[0]["href"]

level2headers = soup.find_all("h2")
print(level2headers)

formats = soup.find_all(["i", "b", "em", "strong"])
print(formats)