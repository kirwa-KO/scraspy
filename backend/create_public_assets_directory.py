from	pathlib			import	Path
from	os				import	mkdir, path, chdir
from	requests		import	get
from	urllib.parse	import	urlparse
from	termcolor		import	colored


def create_folder(directory_path, change_directory = None):
	try:
		if change_directory:
			old_path = Path(__file__).parent
			chdir(change_directory)
		mkdir(directory_path)
		if change_directory:
			chdir(old_path)
	except OSError as error:
		print(error)

def create_public_assets_directory():
	current_directory = Path(__file__).parent

	public_path = path.join(current_directory, 'public')
	create_folder(public_path)

	css_path = path.join(public_path, 'css')
	create_folder(css_path, public_path)

	js_path = path.join(public_path, 'js')
	create_folder(js_path, public_path)

	images_path = path.join(public_path, 'images')
	create_folder(images_path, public_path)

def save_web_site_file(href, web_url, current_directory, sub_dic):
	file_path = path.join(current_directory, 'public', sub_dic, href.split('/')[-1])
	if urlparse(href).netloc:
		response = get(href, allow_redirects=True)
	else:
		response = get(web_url + '/' + href, allow_redirects=True)

	with open(file_path, 'wb') as file:
		file.write(response.content)
	output = "The file " + colored(href.split('/')[-1], "white") + " is downloading "
	print(output.ljust(60), end="")
	print(colored("[Success]", "green"))