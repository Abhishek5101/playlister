from flask import Flask, render_template, redirect, request, url_for
from pymongo import MongoClient
from bson.objectid import ObjectId

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
	playlist_id = playlists.insert_one(playlist).insert_id
	return redirect(url_for('playlists_show', playlist_id=playlist_id))


@app.route('/playlists/new')
def playlists_new():
	return render_template('playlists_new.html')


@app.route('/playlists/<playlist_id>')
def playlists_show(playlist_id):
	playlist = playlists.find_one({'_id': ObjectId(playlist_id)})
	return render_template('playlists_show.html', playlist=playlist)


if __name__ == '__main__':
	app.run(debug=True)



