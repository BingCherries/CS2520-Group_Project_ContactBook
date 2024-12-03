from rpcontacts.database import Database, DATABASE_PATH
from rpcontacts.contact import Contact
db = Database()
print("Database path: ", DATABASE_PATH)
data = [
    Contact("Linda", None, None, "111-2222-3333", "linda@example.com", None, "Has 3 kids and a dog"),
    Contact("Joe", "H.", "Shmo", "111-2222-3333", "joe@example.com", "April 1, 1999"),
    Contact("Lara", None, "Lee", "111-2222-3333", "lara@example.com", "July 21, 1978", "Coworker at Example Co."),
    Contact("David", "Dave", "Davidson", "111-2222-3333", "david@example.com"),
    Contact("Jane", None, None, "111-2222-3333", "jane@example.com"),
]

db.clear_all_contacts()
for contact in data:
    db.add_contact(contact)

contacts = db.get_all_contacts()
print(contacts)

# db.delete_contact(5)
# db.delete_contact(4)

# db.get_all_contacts()
