# Website-2
2nd Website made for connecting people over my university
Project Overview
This project is a web platform designed to help university students connect with one another and discover events happening within their community. It includes four key pages:

Login Page
Allows existing users to log into their accounts.

Registration Page
Provides new users with the ability to create an account by submitting their details.

Home Page
Acts as the main dashboard where users can view events, updates, and interact with the platform.

About Us Page
Shares details about the purpose of the platform and its mission to connect students.

The backend is powered by Flask, while the frontend is built using HTML and CSS.

Purpose
The purpose of this project is to:

Enable Connections: Allow students to interact and form connections with others who share similar interests.
Promote Events: Provide a centralized platform where university-related events are displayed and accessible.
Simplify Networking: Make it easier for students to find and engage with their peers.
How to Run This Project Locally
Prerequisites
Ensure Python is installed on your system (preferably the latest version).
You can download it from https://www.python.org/downloads/.
Install pip, Python's package manager (usually bundled with Python).
A code editor or IDE (e.g., VS Code, PyCharm, or Sublime Text) is recommended.
Steps
Download the Project Files
Save all files for the project (HTML, CSS, Python scripts) on your local system in a single folder.

Navigate to the Project Directory
Open a terminal or command prompt and navigate to the folder where the project files are saved:

bash
Copy code
cd path/to/your/project
Set Up a Virtual Environment (Optional)
Create and activate a virtual environment to isolate project dependencies:

bash
Copy code
python -m venv venv
source venv/bin/activate  # MacOS/Linux
venv\Scripts\activate     # Windows
Install Flask
Use pip to install Flask:

bash
Copy code
pip install flask
Run the Flask Application
Locate the main Python file for the project (usually named app.py) and execute it:

bash
Copy code
python app.py
Access the Website
Once the server starts, open your web browser and go to:

arduino
Copy code
http://127.0.0.1:5000
Explore the Features

Use the Login page to access the platform.
Register a new account on the Registration page.
View events or platform content on the Home page.
Learn about the platform's mission on the About Us page.
File Structure Example
Here’s a basic structure you might have for your project:

graphql
Copy code
project-folder/
│
├── app.py                  # Main Flask application file
├── templates/              # Folder containing HTML files
│   ├── login.html          # Login page
│   ├── register.html       # Registration page
│   ├── about.html          # About Us page
│   ├── home.html           # Home page
│
├── static/                 # Folder for CSS and assets
│   └── styles.css          # Main CSS file
