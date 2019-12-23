import sqlite3

class DataBase:
	conn = sqlite3.connect('db.sqlite3')
	cursor = conn.cursor()

	def __init__(self):
		try:
			self.cursor.execute(''' CREATE TABLE music (
													id INTEGER PRIMARY KEY AUTOINCREMENT,
													autor TEXT,
													name TEXT,
													len TEXT
												   ) 
							''')

		except sqlite3.OperationalError:
			pass


	def write(self, autor, name, len):
		self.cursor.execute(f''' INSERT INTO music (autor, name, len) 
									VALUES ("{autor}", "{name}", "{len}") ''')
		self.conn.commit()

	def delete(self, id):
		self.cursor.execute(f' DELETE FROM music WHERE id={id} ')
		self.conn.commit()

	def return_table(self):
		self.cursor.execute(' SELECT * FROM music ')
		table = self.cursor.fetchone()

		return table
