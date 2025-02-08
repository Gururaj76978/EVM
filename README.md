### Event Management System
### Project Overview

- The Event Management System (EMS) is a command-line interface (CLI) application built using Python, following the Model-View-Controller (MVC) architecture. It enables different user roles to manage and view events effectively. The system supports three user roles: Admin, Organizer, and Attendee, each with distinct permissions. The project uses Python dictionaries for data storage and manipulation.

### Project Architecture (MVC Design Pattern)

1. #### Model (Data Storage & Business Logic)

- The Model layer handles data storage and operations related to events and users. Events and users are stored in dictionaries, where each event is identified by an event ID.

Data Storage (Dictionaries)
users = {
    "admin": {"role": "Admin"},
    "organizer1": {"role": "Organizer"},
    "attendee1": {"role": "Attendee"}
}

events = {}
2. #### View (CLI Interface)

- The View layer provides a command-line interface for users to interact with the system. It presents menus and prompts for input based on the user role.

3. #### Controller (Business Logic & Role-Based Access)

- The Controller layer processes user inputs from the CLI, applies business logic, and updates the Model accordingly. It ensures that users can only perform actions permitted by their roles.

### User Roles and Functionalities

1. ### Admin:
- Manages all events (add, update, delete, view all events).
- Searches for any event by name or date.
- Has full control over the system.

2. ### Organizer:
- Can add new events.
- Can update or delete only their own events.
- Can view all events.
- Can search for events.

3. ### Attendee:
- Can only view events.
- Can search for events based on title or date.

### Command-Line Interface (CLI) Functionalities

- Below are the commands used to interact with the system:

### Admin Menu

- Add Event
- View All Events
- Delete Any Event
- Update Any Event
- Search Event
- Exit

### Organizer Menu

- Add Event
- View All Events
- Delete Own Events
- Update Own Events
- Search Event
- Exit

### Attendee Menu
- View Events
- Search Event
- Exit

### Implementation Details

- The Event Management System is implemented using a structured Model-View-Controller (MVC) approach to separate data handling, business logic, and user interaction.

1. #### Model (Data Storage & Management)

The model is responsible for managing user data and event information. Events are stored in a dictionary, with event IDs as keys. Each event entry contains attributes like event name, date, location, and organizer.

- Event Creation: New events are stored in the dictionary with a unique event ID.
- Event Deletion: Admins can delete any event, while organizers can only delete their own events.
- Event Search: Events can be retrieved by their title or date.

### Controller (Business Logic & Role-Based Access Control)

The controller enforces role-based permissions and processes user actions. It handles event creation, updating, deletion, and retrieval based on the user's role.

- Admins can create, update, delete, and search all events.
- Organizers can only modify or delete events they have created.
- Attendees can view and search events but cannot modify them.

### View (Command-Line Interface for User Interaction)

The view component is responsible for displaying information to users and collecting input from them. It dynamically presents menu options based on the user role and invokes the appropriate controller functions.

### How to Use

- Login: The system prompts for a username and assigns a role (Admin, Organizer, or Attendee).
- Menu Navigation: Based on the role, users interact with the system using the CLI.
- Perform Actions: Users can add, update, delete, view, or search events as per their permissions.
- Exit the System: Users can exit the system from the main menu.

### Conclusion

- This Event Management System effectively implements an MVC architecture with role-based access control. It uses Python dictionaries to store user and event data, making it efficient and scalable for managing events through a command-line interface.