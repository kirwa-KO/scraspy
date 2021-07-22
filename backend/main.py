# from bs4 import BeautifulSoup

# import requests
# r = requests.get("https://kirwako.com")
# data = r.text
# soup = BeautifulSoup(data)

# for link in soup.find_all('a'):
# print(link.get('href'))


# Import Required Library
from requests import get
from bs4 import BeautifulSoup
from urllib.parse import urlparse

# Web URL
web_url = "https://www.kirwako.com/"
# web_url = "https://www.geeksforgeeks.org/how-to-extract-script-and-css-files-from-web-pages-in-python/"

# get HTML content
html = get(web_url).content

web_url_domain = urlparse(web_url).netloc

# parse HTML Content
soup = BeautifulSoup(html, "html.parser")

js_files = []
css_files = []
html_files = []
assets_files = []
outside_links = []
inside_links = []

for script in soup.find_all("script"):
	if script.attrs.get("src"):
		
		# if the tag has the attribute 
		# 'src'
		url = script.attrs.get("src")
		js_files.append(url)

for css in soup.find_all("link"):
	if css.attrs.get("href"):
		
		# if the link tag has the 'href'
		# attribute
		_url = css.attrs.get("href")
		if "css" in _url:
			css_files.append(_url)
		else:
			assets_files.append(_url)


for anchor in soup.find_all("a"):
	href = anchor.attrs.get("href")
	domain = urlparse(href).netloc
	if web_url_domain != domain:
		if href not in outside_links:
			outside_links.append(href)
		elif href not in inside_links and domain == "" or domain == web_url_domain:
			inside_links.append(href)
	elif href not in inside_links and "" != href:
		inside_links.append(href)

print("=" * 150)
print(inside_links)
print("=" * 150)
print(outside_links)
# print(str("*" * 50) + " js files "  + str("*" * 50))
# print(js_files)
# print(str("*" * 50) + " css files " + str("*" * 50))
# print(css_files)

