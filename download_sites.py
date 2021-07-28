import os
import zipfile
from	urllib.parse	import	urlparse
import shutil

def zipdir(path, ziph):
	html_files = []
	css_files = []
	js_files = []
	assets_files = []
	# ziph is zipfile handle
	for root, dirs, files in os.walk(path):
		for file in files:
			if file.split('.')[-1] == "html":
				html_files.append(os.path.join(root, file))
			elif file.split('.')[-1] == "css":
				css_files.append(os.path.join(root, file))
			elif file.split('.')[-1] == "js":
				js_files.append(os.path.join(root, file))
			else:
				assets_files.append(os.path.join(root, file))
			ziph.write(os.path.join(root, file), os.path.relpath(os.path.join(root, file), os.path.join(path, '..')))
	return html_files, css_files, js_files, assets_files

# website_url = "https://www.kirwako.com/"

# download all pages
def download_all_pages(website_url):
	domain_name = urlparse(website_url).netloc
	os.system("wget -mkEpnp --html-extension --restrict-file-names=windows " + website_url)
	zipf = zipfile.ZipFile("/tmp/" + domain_name + ".zip", "w", zipfile.ZIP_DEFLATED)
	html_files, css_files, js_files, assets_files = zipdir(domain_name + '/', zipf)
	zipf.close()
	shutil.rmtree(domain_name)
	return html_files, css_files, js_files, assets_files

# download just the sepefied page
def download_specifique_page(website_url):
	domain_name = urlparse(website_url).netloc
	os.system("wget -rpk --html-extension --restrict-file-names=windows " + website_url)
	zipf = zipfile.ZipFile("/tmp/" + domain_name + ".zip", "w", zipfile.ZIP_DEFLATED)
	html_files, css_files, js_files, assets_files = zipdir(domain_name + '/', zipf)
	zipf.close()
	shutil.rmtree(domain_name)
	return html_files, css_files, js_files, assets_files

