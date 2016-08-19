import sqlite3

class Projects:

	
	def __init__(self):
		self.con = sqlite3.connect('projects.db')
		print("db opened successfully")

	def create(self):
		self.con.execute('''
		create table projects
		(id integer primary key autoincrement,
		link text not null,
		name text not null,
		description text not null,
		dependencies text,
		language text not null)''')
		print("Projects table created")

		self.con.commit()
		self.con.close()

	def empty(self):
		self.con.execute("delete from projects")

		self.con.commit()
		self.con.close()


	def delete(self, row):
		self.con.execute("delete from projects where name=(?)",(row,))

		self.con.commit()
		self.con.close()
		
