import pathlib
import sqlite3
from rpcontacts.contact import Contact

DATABASE_PATH = pathlib.Path().home() / "contacts.db"


class Database:
    def __init__(self, db_path=DATABASE_PATH):
        self.db = sqlite3.connect(db_path)
        self.cursor = self.db.cursor()
        self._create_table()

    def _create_table(self):
        query = """
            CREATE TABLE IF NOT EXISTS contacts(
                id INTEGER PRIMARY KEY,
                firstName TEXT,
                middleName TEXT,
                lastName TEXT,
                phone TEXT,
                email TEXT,
                birthday TEXT,
                memo TEXT
            );
        """
        self._run_query(query)

    def _run_query(self, query, *query_args):
        result = self.cursor.execute(query, *query_args)
        self.db.commit()
        return result

    def get_all_contacts(self):
        result = self._run_query("SELECT * FROM contacts;")
        contacts = [Contact(*contact) for contact in result.fetchall()]
        return contacts

    def get_last_contact(self):
        result = self._run_query(
            "SELECT * FROM contacts ORDER BY id DESC LIMIT 1;"
        )
        return Contact(*result.fetchone())

    def add_contact(self, contact: Contact):
        self._run_query(
            "INSERT INTO contacts VALUES (NULL, ?, ?, ?, ? , ?, ?, ?);",
            contact.all()[1:]
        )

    def delete_contact(self, id):
        self._run_query(
            "DELETE FROM contacts WHERE id=(?);",
            (id,),
        )

    def clear_all_contacts(self):
        self._run_query("DELETE FROM contacts;")
