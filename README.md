StudySync

Video Demo: 

Description:

StudySync is a collaborative task and study management web application built using Django. It allows users to organize their academic work efficiently by creating groups called “Circles,” where members can assign tasks, track progress, and collaborate in a structured way.

Users can register, log in, and join or create circles. Within each circle, tasks can be assigned to specific members with deadlines. Each user can track their own tasks as well as view all tasks within a circle.

The goal of StudySync is to simplify group study coordination and improve productivity through clear task management and accountability.


Distinctiveness and Complexity:

StudySync satisfies the distinctiveness and complexity requirements through its multi-user collaborative system, relational database design, and role-based functionality.

StudySync focuses on task management and collaboration, introducing new challenges such as task assignment workflows, user roles, and real-time interaction.

Key aspects of complexity include:

**Relational database design** using multiple interconnected models (User, Circle, Task, Membership)
**Role-based access control**, where admins have additional privileges (e.g., deleting circles)
**Task assignment system**, allowing users to assign tasks to other members
**User-specific permissions**, ensuring users can only modify their own tasks
**Dynamic task updates** using asynchronous requests (AJAX with JSON responses)
**Multiple user workflows**, including joining, leaving, creating, and managing circles

These features go beyond basic CRUD functionality and require careful coordination between backend logic, database relationships, and frontend interaction.

Files and Their Purpose:

`views.py`
Handles all backend logic and routing, including:

* User authentication (register, login, logout)
* Circle management (create, join, exit, delete)
* Task assignment and retrieval
* Rendering templates with dynamic data
* Task status toggling using JSON responses

`models.py`
Defines the database structure:

* **User**: Stores user account information
* **Circle**: Represents a study group
* **Task**: Stores task details such as title, description, assigned user, due date, and status
* **Membership**: Manages relationships between users and circles, including roles (admin/member)

`templates/`
Contains all HTML templates for:

* Authentication pages (login, register)
* Dashboard and homepage
* Circles view and individual circle pages
* Task assignment and activity pages

`static/`
Includes CSS and JavaScript files used for styling and frontend interactivity.

`urls.py`
Maps application routes to their respective views.


How to Run the Application:

1. Clone the repository:
```
git clone <your-repository-url>
cd studysync
```

2. Install dependencies:
```
pip install -r requirements.txt
```

3. Apply migrations:
```
python manage.py migrate
```

4. Run the server:
```
python manage.py runserver
```

5. Open in your browser:
```
http://127.0.0.1:8000/
```

Additional Information:

* Only authenticated users can access core features such as circles and tasks.
* Users can only toggle the status of tasks assigned to them, ensuring proper access control.
* Admin users have the ability to delete circles they created.
* Circles act as collaborative spaces where multiple users can work together.
* The application uses Django’s built-in authentication system for secure login and session handling.
* JSON responses are used to enable smoother user experience without requiring full page reloads.


Future Improvements:
These are features that could further enhance StudySync:


**Notifications System**
  Add in-app or email notifications to alert users when they are assigned a task or when deadlines are approaching.

**Task Prioritization and Categories**
  Allow users to assign priority levels (high, medium, low) or categorize tasks for better organization.

**File Sharing in Circles**
  Enable users to upload and share study materials within circles to improve collaboration.

**Improved UI/UX**
  Enhance the frontend design to make the application more responsive and mobile-friendly.

**Deadline Reminders**
  Integrate scheduled reminders for upcoming due dates.

**Search and Filtering**
  Add functionality to search tasks or filter them based on status, due date, or assigned user.

**Enhanced Security**
  Add features such as two-factor authentication and improved permission handling.


Summary:
StudySync is a full-stack Django application that demonstrates the use of authentication, relational databases, and interactive features to build a collaborative productivity tool. It emphasizes structured teamwork, role-based permissions, and efficient task tracking, making it a more complex and feature-rich application than basic web projects.


Credits:

Developed as part of Harvard's CS50's Web Programming with Python and JavaScript.

Technologies Used:
Python
Django
HTML
CSS
JavaScript
SQLite

Author: Gargee Pandey
