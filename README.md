# StudySync

A full-stack collaborative task management web app that helps students organize group study using shared workspaces called **Circles**.

Built with **Django • SQLite • JavaScript • HTML/CSS**


## Features
- Create and join study groups (*Circles*)
- Assign tasks to group members with deadlines
- Secure user authentication (login / register / logout)
- Role-based permissions (admins & members)
- Dynamic task updates using AJAX (no page reloads)
- Personal and group task tracking dashboards
- Join, leave, create and manage circles easily

## Tech Stack
**Backend:** Django, Python  
**Frontend:** HTML, CSS, JavaScript (AJAX)  
**Database:** SQLite  
**Authentication:** Django built-in authentication system  


## How to Run Locally

Clone the repository:
git clone https://github.com/YOUR_USERNAME/StudySync  
cd StudySync  

Install dependencies:
pip install -r requirements.txt  

Apply migrations:
python manage.py migrate  

Run the server:
python manage.py runserver  

Open in browser:  
http://127.0.0.1:8000/


## Key Learning Outcomes
This project strengthened my ability to:

- Design relational databases with multiple interconnected models  
- Implement role-based access control  
- Build full-stack web applications using Django  
- Handle asynchronous requests using JSON & AJAX  
- Structure a real-world multi-user application  


## Project Architecture

### Core Models
- **User** – authentication and accounts  
- **Circle** – collaborative study group  
- **Task** – assignments with deadlines & status  
- **Membership** – user roles within circles  

### Core Functionalities
- User authentication and session handling  
- Circle creation, joining, leaving and deletion  
- Task assignment and tracking  
- Admin-only permissions for circle management  
- JSON responses for smoother user experience  


## Future Improvements
- Notifications for new task assignments  
- Task prioritization and categories  
- File sharing within circles  
- Improved mobile-responsive UI  
- Deadline reminder system  
- Search and filtering for tasks  
- Two-factor authentication  


## Credits
Developed as part of CS50’s Web Programming with Python and JavaScript.

##  Author
Gargee Pandey
