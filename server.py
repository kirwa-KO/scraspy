from flask				import Flask, render_template, request
from download_sites		import download_all_pages


scraspy = Flask(__name__)

@scraspy.route('/')
def home_page():
	return render_template('index.html', custom_css="index")

@scraspy.route('/fetched', methods=['POST', 'GET'])
def fetched_page():
	if request.method == 'GET':
		return render_template('fetched.html', custom_css="fetched", website="https://www.kirwako.com")
	elif request.method == 'POST':
		download_all_pages(request.form['website'])
		return render_template('fetched.html', custom_css="fetched", website="https://www.kirwako.com")

if __name__ == "__main__":
	scraspy.run(debug=True)