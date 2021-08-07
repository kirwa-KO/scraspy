from flask				import Flask, render_template, request, after_this_request, jsonify
from flask.helpers		import send_file
from download_sites		import download_all_pages, download_specifique_page
from threading			import Thread
from time				import sleep

app = Flask(__name__)
finished = False

@app.route('/')
def home_page():
	return render_template('index.html', custom_css="index")

def testoo(website):
	global finished
	sleep(5)
	print("#" * 80)
	print(website)
	print("#" * 80)
	finished = True

@app.route('/fetched', methods=['POST', 'GET'])
def fetched_page():
	global finished
	finished = False
	if request.method == 'GET':
		html_files = ['index.html', 'contact.html', 'about.html']
		css_files = ['all.min.css', 'css/about.css', 'css/main.css', 'css/contact.css']
		js_files = ["main.js", "loading.js"]
		assets_files = ['robots.txt', 'Circular_Std_Font.otf', 'fa-regular-400.eot', 'fa-solid-900.eot', 'fa-brands-400.svg', 'fa-regular-400.eot@', 'fa-solid-900.eot@', 'fa-solid-900.woff2', 'fa-regular-400.ttf', 'fa-brands-400.woff', 'fa-solid-900.woff', 'fa-brands-400.woff2', 'fa-regular-400.woff', 'fa-solid-900.ttf', 'fa-regular-400.woff2', 'fa-solid-900.svg', 'fa-regular-400.svg', 'fa-brands-400.eot@', 'fa-brands-400.eot', 'fa-brands-400.ttf', 'images/icon2.svg', 'images/kirwaKO-01.svg', 'images/kirwa-KO-white.svg', 'images/technologies/c.svg', 'images/technologies/nodejs.svg', 'images/technologies/redux.svg', 'images/technologies/docker.svg', 'images/technologies/django.svg', 'images/technologies/css.svg', 'images/technologies/mysql.svg', 'images/technologies/ruby.svg', 'images/technologies/oracle.svg', 'images/technologies/mognodb.svg', 'images/technologies/javascript.svg', 'images/technologies/wordpress.svg', 'images/technologies/php.svg', 'images/technologies/debian.svg', 'images/technologies/bootstrap.svg', 'images/technologies/python.svg', 'images/technologies/babel.svg', 'images/technologies/jquery.svg', 'images/technologies/java.svg', 'images/technologies/nginx.svg', 'images/technologies/github.svg', 'images/technologies/aws.svg', 'images/technologies/apache.svg', 'images/technologies/laravel.svg', 'images/technologies/bash.svg', 'images/technologies/cpp.svg', 'images/technologies/typescript.svg', 'images/technologies/react.svg', 'home-app-web-anim.json-white.1881f7a.webm', 'home-ui-anim.json-white.21ee591.webm', 'home-ecom-anim.json-white.04d7d27.webm', 'home-datascience-anim.json-white.f5c27a2.webm', 'meeting-animation.json.mp4.4f823af.webm', 'home-seo-anim.json-white.feb2ba5.webm', 'drone-animation.json-white.4097b84.webm']

		return render_template('fetched.html',
								custom_css="fetched",
								website="https://www.kirwako.com",
								html_files=html_files,
								css_files=css_files,
								js_files=js_files,
								assets_files=assets_files,
								zip_file_name="kirwako.com.zip")

	elif request.method == 'POST':
		website_url = request.form['website']
		# if request.form['pages'] == "all_pages":
		# 	html_files, css_files, js_files, assets_files, zip_file_name = download_all_pages(website_url)
		# else:
		# 	html_files, css_files, js_files, assets_files, zip_file_name = download_specifique_page(website_url)
		
		# down = Thread(target=download_all_pages, args=(website_url,), daemon=True)
		# down.start()
		down = Thread(target=testoo, args=(website_url,), daemon=True)
		down.start()
		html_files, css_files, js_files, assets_files, zip_file_name = [], [], [], [], []


		if "http://" not in website_url and "https://" not in website_url:
			website_url = "https://" + website_url

		return render_template('loading.html',
							custom_css="loading",
							website=website_url,
							html_files=html_files,
							css_files=css_files,
							js_files=js_files,
							assets_files=assets_files,
							zip_file_name=zip_file_name)

@app.route('/download/<filename>')
def download_zip_file(filename):
	import os
	# path = filename
	# return send_file(path, as_attachment=True)
	# file_path = derive_filepath_from_filename(filename)
	file_handle = open(filename, 'r')
	@after_this_request
	def remove_file(response):
		try:
			os.remove(filename)
			file_handle.close()
		except Exception as error:
			app.logger.error("Error removing or closing downloaded file handle", error)
		return response
	return send_file(filename, as_attachment=True)

@app.route('/result')
def result():
	""" Just give back the result of your heavy work """
	return 'Done'


@app.route('/status')
def thread_status():
	""" Return the status of the worker thread """
	return jsonify(dict(status=('finished' if finished else 'running')))


if __name__ == "__main__":
	app.run(debug=True)