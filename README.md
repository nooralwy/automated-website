# Smart Farming Automated Web Application

## Overview
This is a Flask-based web application developed for the ITEC224 project.  
The project allows users to enter a website URL, scrape information from that website, and display the results through a clean web interface. It also includes task scheduling and email notification features, making the application more automated and useful.

## Features
- Flask web application
- Web scraping functionality
- Automated task scheduling
- Email notification support
- Home, Task, and About pages
- Responsive user interface using HTML and CSS
- Team member profile section
- Organized static files and templates

## Technologies Used
- Python
- Flask
- HTML
- CSS
- JavaScript
- BeautifulSoup
- Requests
- SMTP Email
- Task Scheduling

## Project Structure
```text
ITEC224_Project/
├── app.py
├── scraper.py
├── scheduler.py
├── requirements.txt
├── templates/
│   ├── home.html
│   ├── task.html
│   └── about.html
├── static/
│   ├── style.css
│   └── images/
└── README.md

## How to Run the Project
1. Clone the repository:
git clone https://github.com/nooralwy/automated-website.git
2. Open the project folder:
cd automated-website
3. Create a virtual environment:
python3 -m venv venv
4. Activate the virtual environment:
source venv/bin/activate
5. Install the required packages:
pip install -r requirements.txt
6. Run the application:
python app.py
7. Open the browser and go to:
http://127.0.0.1:5000

## Purpose of the Project

The purpose of this project is to demonstrate automation using web scraping and task scheduling.

Instead of manually visiting websites and collecting information, the application can scrape website data automatically. The task scheduling feature allows scraping tasks to run at planned times, and the email feature can send results to users.

This project shows practical skills in Python programming, Flask web development, web scraping, automation, and front-end design.

## Author
Created by Group 4
Python Flask Project
