from model import DataManager
from views import show_main_menu, admin_menu, organizer_menu, attendee_menu

class EventManagementController:
    def __init__(self):
        self.data_manager = DataManager()
        self.data_manager.load_data()

    def authenticate_user(self, username, password):
        user = self.data_manager.get_user_by_credentials(username, password)
        return user

    def main(self):
        user_authenticated = False
        while not user_authenticated:
            username, password = show_main_menu()
            user = self.authenticate_user(username, password)
            if user:
                user_authenticated = True
                self.user_role_menu(user)
            else:
                print("Invalid credentials. Please try again.")

    def user_role_menu(self, user):
        if user["role"] == "Admin":
            self.admin_menu(user)
        elif user["role"] == "Organizer":
            self.organizer_menu(user)
        elif user["role"] == "Attendee":
            self.attendee_menu(user)

    def admin_menu(self, user):
        while True:
            choice = admin_menu()
            if choice == "1":
                self.add_event(user)
            elif choice == "2":
                self.view_events(user)
            elif choice == "3":
                self.delete_event(user)
            elif choice == "4":
                self.update_event(user)
            elif choice == "5":
                self.search_event(user)
            elif choice == "6":
                break

    def organizer_menu(self, user):
        while True:
            choice = organizer_menu()
            if choice == "1":
                self.add_event(user)
            elif choice == "2":
                self.view_events(user)
            elif choice == "3":
                self.delete_event(user)
            elif choice == "4":
                self.update_event(user)
            elif choice == "5":
                self.search_event(user)
            elif choice == "6":
                break

    def attendee_menu(self, user):
        while True:
            choice = attendee_menu()
            if choice == "1":
                self.view_events(user)
            elif choice == "2":
                self.search_event(user)
            elif choice == "3":
                break

    def add_event(self, user):
        # Logic for adding event
        print("Adding event...")

    def view_events(self, user):
        # Logic for viewing events
        print("Viewing events...")

    def delete_event(self, user):
        # Logic for deleting events
        print("Deleting event...")

    def update_event(self, user):
        # Logic for updating events
        print("Updating event...")

    def search_event(self, user):
        # Logic for searching events
        print("Searching events...")
