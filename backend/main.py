# Import Required Library
from	os								import	link
from	requests						import	get
from	bs4								import	BeautifulSoup
from	urllib.parse					import	urlparse
from	create_public_assets_directory	import	create_public_assets_directory, save_web_site_file
from	pathlib							import	Path
from	os								import	path

create_public_assets_directory()

# Web URL
# web_url = "https://www.kirwako.com/"
web_url = "https://bookylia.com/"
# web_url = "https://www.geeksforgeeks.org/how-to-extract-script-and-css-files-from-web-pages-in-python/"

# get HTML content
url = get(web_url)
html = url.content
# text = url.text

web_url_domain = urlparse(web_url).netloc

# parse HTML Content
soup = BeautifulSoup(html, "html.parser")

js_files = []
css_files = []
html_files = []
assets_files = []
outside_links = []
inside_links = []

current_directory = Path(__file__).parent


for script in soup.find_all("script"):
	if script.attrs.get("src"):
		# if the tag has the attribute 
		# 'src'
		href = script.attrs.get("src")
		js_files.append(href)
		file_path = save_web_site_file(href, web_url, current_directory, 'js')
		script['src'] = script['src'].replace(script['src'], file_path)

for css in soup.find_all("link"):
	if css.attrs.get("href"):
		
		# if the link tag has the 'href'
		# attribute
		href = css.attrs.get("href")
		if "css" in href:
			css_files.append(href)
			save_web_site_file(href, web_url, current_directory, 'css')
		else:
			assets_files.append(href)
			save_web_site_file(href, web_url, current_directory, 'images')


for anchor in soup.find_all("a"):
	href = anchor.attrs.get("href")
	domain = urlparse(href).netloc
	if web_url_domain != domain:
		if href not in outside_links and "" != domain and domain != web_url_domain:
			outside_links.append(href)
		elif href not in inside_links and domain == "" or domain == web_url_domain:
			inside_links.append(href)
	elif href not in inside_links and "" != href:
		inside_links.append(href)

for anchor in soup.find_all("img"):
	src = anchor.attrs.get("src")
	if src not in assets_files:
		assets_files.append(src)
		save_web_site_file(src, web_url, current_directory, 'images')

# new_content = ""

# for line in url.text.split('\n'):
# 	print(line)
# 	new_content += line

# for a in soup.findAll('a'):
# 	a['href'] = a['href'].replace(a['href'], "mysite")
# 	break
print(str(soup))