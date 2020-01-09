from db import DataBase
from flask import Flask, render_template, redirect, request

app = Flask(__name__)
db = DataBase()


@app.route('/')
def main():
	music = db.return_table()
	return render_template(
		'index.html', music=music
	)


@app.route('/delete-music/', methods=['POST'])
def delete_music():
	db.delete(request.form["id"])
	return redirect('/')


@app.route('/add-music/', methods=['POST'])
def add_music():
	autor = request.form["autor"]
	name = request.form["name"]
	minutes = request.form["min"]
	seconds = request.form["sec"]

	if (len(autor.replace(" ", "")) != 0 
	and len(name.replace(" ", "")) != 0 
	and minutes.isdigit() 
	and seconds.isdigit() 
	and 0 <= int(minutes) <= 180 
	and 0 <= int(seconds) <= 59):
		if len("0" + seconds) == 2:
			seconds = "0" + seconds
		db.write(autor, name, f"{minutes}:{seconds}")

	else:
		music = db.return_table()
		return render_template(
		'index.html', music=music, error=True
		)

	return redirect('/')


@app.errorhandler(404)
def page_not_found(error):
	return redirect('/')


if __name__ == '__main__':
	app.run()
