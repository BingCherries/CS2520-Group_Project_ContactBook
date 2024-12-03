from rpcontacts.contact import Contact
from textual.app import App, on
from textual.containers import Grid, Horizontal, Vertical
from textual.screen import Screen
from textual.widgets import (
    Button,
    DataTable,
    Footer,
    Header,
    Input,
    Label,
    Static,
)


class ContactsApp(App):
    CSS_PATH = "rpcontacts.tcss"
    BINDINGS = [
        ("m", "toggle_dark", "Toggle dark mode"),
        ("a", "add", "Add"),
        ("d", "delete", "Delete"),
        ("c", "clear_all", "Clear All"),
        ("q", "request_quit", "Quit"),
    ]

    def __init__(self, db):
        super().__init__()
        self.db = db

    def compose(self):
        yield Header()
        contacts_list = DataTable(classes="contacts-list")
        contacts_list.focus()
        contacts_list.add_columns("First Name", "Middle Name", "Last Name", "Phone", "Email", "Birthday", "Memo")
        contacts_list.cursor_type = "row"
        contacts_list.zebra_stripes = True
        add_button = Button("Add", variant="success", id="add")
        add_button.focus()
        buttons_panel = Vertical(
            add_button,
            Button("Delete", variant="warning", id="delete"),
            Static(classes="separator"),
            Button("Clear All", variant="error", id="clear"),
            classes="buttons-panel",
        )
        yield Horizontal(contacts_list, buttons_panel)
        yield Footer()

    def on_mount(self):
        self.title = "RP Contacts"
        self.sub_title = "A Contacts Book App With Textual & Python"
        self._load_contacts()

    def _load_contacts(self):
        contacts_list = self.query_one(DataTable)
        for contact in self.db.get_all_contacts():
            contacts_list.add_row(*contact.all()[1:], key=contact.id)

    def action_toggle_dark(self):
        self.dark = not self.dark

    def action_request_quit(self):
        def check_answer(accepted):
            if accepted:
                self.exit()

        self.push_screen(QuestionDialog("Do you want to quit?"), check_answer)

    @on(Button.Pressed, "#add")
    def action_add(self):
        def check_contact(contact_data):
            if contact_data:
                self.db.add_contact(Contact(None, *contact_data))
                contact = self.db.get_last_contact()
                self.query_one(DataTable).add_row(*contact.all()[1:], key=id)

        self.push_screen(InputDialog(), check_contact)

    @on(Button.Pressed, "#delete")
    def action_delete(self):
        contacts_list = self.query_one(DataTable)
        row_key, _ = contacts_list.coordinate_to_cell_key(
            contacts_list.cursor_coordinate
        )

        def check_answer(accepted):
            if accepted and row_key:
                self.db.delete_contact(id=row_key.value)
                contacts_list.remove_row(row_key)

        name = contacts_list.get_row(row_key)[0]
        self.push_screen(
            QuestionDialog(f"Do you want to delete {name}'s contact?"),
            check_answer,
        )

    @on(Button.Pressed, "#clear")
    def action_clear_all(self):
        def check_answer(accepted):
            if accepted:
                self.db.clear_all_contacts()
                self.query_one(DataTable).clear()

        self.push_screen(
            QuestionDialog("Are you sure you want to remove all contacts?"),
            check_answer,
        )


class QuestionDialog(Screen):
    def __init__(self, message, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.message = message

    def compose(self):
        no_button = Button("No", variant="primary", id="no")
        no_button.focus()

        yield Grid(
            Label(self.message, id="question"),
            Button("Yes", variant="error", id="yes"),
            no_button,
            id="question-dialog",
        )

    def on_button_pressed(self, event):
        if event.button.id == "yes":
            self.dismiss(True)
        else:
            self.dismiss(False)


class InputDialog(Screen):
    def compose(self):
        yield Grid(
            Label("Add Contact", id="title"),
            Label("First Name:", classes="label"),
            Input(placeholder="Contact First Name", classes="input", id="firstName"),
            # Label("Middle Name:", classes="label"),
            # Input(placeholder="Contact Middle Name", classes="input", id="middleName"),
            # Label("Last Name:", classes="label"),
            # Input(placeholder="Contact Last Name", classes="input", id="lastName"),
            Label("Phone:", classes="label"),
            Input(placeholder="Contact Phone", classes="input", id="phone"),
            Label("Email:", classes="label"),
            Input(placeholder="Contact Email", classes="input", id="email"),
            # Label("Birthday:", classes="label"),
            # Input(placeholder="Contact Birthday", classes="input", id="birthday"),
            # Label("Memo:", classes="label"),
            # Input(placeholder="Contact Memo", classes="input", id="memo"),
            Static(),
            Button("Cancel", variant="warning", id="cancel"),
            Button("Ok", variant="success", id="ok"),
            id="input-dialog",
        )

    def on_button_pressed(self, event):
        if event.button.id == "ok":
            name = self.query_one("#name", Input).value
            phone = self.query_one("#phone", Input).value
            email = self.query_one("#email", Input).value
            self.dismiss((name, phone, email))
        else:
            self.dismiss(())
