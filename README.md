# CS2520-Group_Project
Project Title: Build a Contact Book App With Python, Textual, and SQLite

Team Members: Alexander Matei, Yunseon Choi, Dylan Oliva

## Objective:
The project’s ultimate goal is to create a simple but functional tool for managing contacts through a terminal interface, allowing users to store and organize their personal or business contact information effectively while learning and demonstrating core Python skills like database management, user interface design, and input validation.

## How to Run
1. Create a virtual environment:
```
python -m venv venv
```

2. Activate the virtual environment:
Windows:
```
venv\Scripts\activate
```

3. Install the dependencies:
```
pip install textual sqlite3
```
 
4. Activate the virtual environment 
```
venv\Scripts\activate
```
5. Run the application:
   * Navigate to the project directory and run the __main__.py file to start the application.
```
python -m rpcontacts
```


## Database Schema

| Column  |  Description |
|---|---|
| id |An auto-generated integer primary key
|  First Name |  A string containing the first name of a contact |
|  Middle Name |  A string containing the middle name of a contact |
|  Last Name |  A string containing the last name of a contact |
| Phone  |  A string representing the phone number of a contact |
|  Email |  A string containing the email of a contact | 	
|  Birthday |  A string containing the birthday of a contact |
|  Memo |  A string containing the memo of a contact |

## Project Structure
```
rpcontacts_project/
│
├── rpcontacts/               # Main package directory
│   ├── __init__.py           # Marks rpcontacts as a package
│   ├── __main__.py           # Entry point to run the application
│   ├── database.py           # Handles database operations (SQLite)
│   ├── tui.py                # Contains the UI (Textual-based)
│   ├── contact.py            # Defines the Contact class and attributes
│   └── other modules
├── venv/                     # Virtual environment
├── requirements.txt          # Lists all Python dependencies
```
 	
## Reference
* Ramos, L. P. (2024, October 9). Build a Contact Book App With Python, Textual, and SQLite. Realpython.com; Real Python.
* [Link](https://realpython.com/contact-book-python-textual/)

