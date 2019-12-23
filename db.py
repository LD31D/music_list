import sqlite3

class DataBase:

	def __init__(self):
		self.create_connect()

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

		self.break_connection()

	def create_connect(self):
		self.conn = sqlite3.connect('db.sqlite3', check_same_thread = False)
		self.cursor = self.conn.cursor()

	def break_connection(self):
		self.cursor.close()
		self.conn.close()

	def write(self, autor, name, len):
		self.create_connect()

		self.cursor.execute(f''' INSERT INTO music (autor, name, len) 
									VALUES ("{autor}", "{name}", "{len}") ''')
		self.conn.commit()

		self.break_connection()

	def delete(self, id):
		self.create_connect()

		self.cursor.execute(f' DELETE FROM music WHERE id={id} ')
		self.conn.commit()

		self.break_connection()

	def return_table(self):
		self.create_connect()

		self.cursor.execute(' SELECT * FROM music ')
		table = self.cursor.fetchall()

		self.break_connection()

		return table
