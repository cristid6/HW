import sqlite3

class Database:
    """Connection with complaints database and some methods for adding, selecting and updating info."""

    def __init__(self):
        self.connection = sqlite3.connect("complaints_database.db")
        self.cur = self.connection.cursor()
        self.create_table = self.cur.execute(
            """CREATE TABLE IF NOT EXISTS complaints (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            first_name VARCHAR(255) NOT NULL,
            last_name VARCHAR(255) NOT NULL,
            complaint_title TEXT NOT NULL,
            complaint_description TEXT NOT NULL,
            register_datetime DATETIME DEFAULT CURRENT_TIMESTAMP,
            status INTEGER DEFAULT 0
            );
            """)

    """Add complaint (requires first name, last_name, complaint title, complaint description)"""
    def add_complaint(self, first_name, last_name, complaint_title, complaint_description):
        self.first_name = first_name
        self.last_name = last_name
        self.complaint_title = complaint_title
        self.complaint_description = complaint_description
        self.insert = self.cur.execute("""INSERT INTO complaints(first_name, last_name, complaint_title, complaint_description) 
        VALUES (?, ?, ?, ?);""", (self.first_name, self.last_name, self.complaint_title, self.complaint_description))
        self.connection.commit()

    """Select complaint by id (requires id)"""
    def select_complaint(self, id):
        self.id = id
        self.select = self.cur.execute("""SELECT * FROM complaints WHERE id=?;""", (self.id,))
        print(self.select.fetchall())

    """Select all complaints"""
    def select_all(self):
        self.select = self.cur.execute("""SELECT * FROM complaints;""")
        print(self.select.fetchall())

    """Select all complaints where id is unresolved"""
    def select_0(self):
        self.select = self.cur.execute("""SELECT * FROM complaints WHERE status=0;""")
        print(self.select.fetchall())

    """Select all complaints where id is resolved"""
    def select_1(self):
        self.select = self.cur.execute("""SELECT * FROM complaints WHERE status=1;""")
        print(self.select.fetchall())

    """Update complaint status by id (requires id)"""
    def modify_status(self, id, status):
        self.id = id
        self.status = status
        self.modify = self.cur.execute("""UPDATE complaints SET status=? WHERE id=?;""", (self.status, self.id))
        self.connection.commit()
        print(f"Complaint with id {self.id} updated with status {self.status}.")

    """Get max id from complaints"""
    def get_max_id(self):
        self.max_id = self.cur.execute("""SELECT max(id) FROM complaints""")
        return self.max_id.fetchall()[0][0]









