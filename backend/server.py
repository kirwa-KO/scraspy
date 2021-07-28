from flask import Flask, render_template

scraspy = Flask(__name__)

@scraspy.route('/')
def home_page():
	return render_template('index.html', custom_css="index")


@scraspy.route('/fetched')
def fetched_page():
	return render_template('fetched.html', custom_css="fetched")

if __name__ == "__main__":
	scraspy.run(debug=True)