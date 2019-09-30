from flask import Flask, render_template, redirect, request, url_for
from pymongo import MongoClient


app = Flask(__name__)

client = MongoClient()
db = client.Playlister
playlists = db.playlists
# OUR MOCK ARRAY OF PROJECTS
# playlists = [
# 	{'title': 'Cat Videos', 'description': 'Cats acting weird'},
# 	{'title': '80\'s Music', 'description': 'Don\'t stop believing!'},
# 	{'title': 'Gangnam Style', 'description': 'Ayeee sexy lady'}
# ]
#


@app.route('/')
def playlists_index():
	return render_template('playlists_index.html', playlists=playlists.find())


@app.route('/playlists', methods=['POST'])
def playlists_submit():
	playlist = {
		'title': request.form.get('title'),
		'description': request.form.get('description'),
		'videos': request.form.get('videos').split()
		
	}
	playlists.insert_one(playlist)
	return redirect(url_for('playlists_index'))


@app.route('/playlists/new')
def playlists_new():
	return render_template('playlists_new.html')


if __name__ == '__main__':
	app.run(debug=True)



