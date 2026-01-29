# 🎓 Django Fake Data Dashboard

## 📌 Overview
The **Django Fake Data Dashboard** is a web-based application built using **Django** that generates fake student data using the **Faker** library and displays it in a structured table format.

The project demonstrates how to:
- Populate a database with fake data
- Retrieve records using Django ORM
- Apply filtering and ordering
- Display data dynamically on a web page

This project is useful for understanding **backend development**, **ORM queries**, and **data handling in Django**.

---

## ⚙️ Features
- Generate fake student records using Faker
- Store generated data in the database
- Display student data in a tabular format
- Filter records using Django ORM
- Order records based on fields (e.g., name, marks)
- Clean UI using HTML and CSS
- Django Admin integration for data management

---

## 🧠 Concepts Used
- Django Models and ORM
- Faker library for fake data generation
- Database migrations
- Django Views and Templates
- Static files handling (CSS)
- Filtering and ordering using `filter()` and `order_by()`
- Admin panel customization

---

## 🎓 Learning Outcomes
- Learned how to integrate **Faker** with Django
- Gained hands-on experience with **Django ORM queries**
- Understood dynamic data rendering using templates
- Improved knowledge of **project structure in Django**
- Practiced separating logic, templates, and static files

---

## 📁 Project Structure

```
django-fake-data-dashboard/
│
├── modelproject3/
│ ├── settings.py
│ ├── urls.py
│ └── ...
│
├── testapp/
│ ├── models.py
│ ├── views.py
│ ├── admin.py
│ └── migrations/
│
├── templates/
│ └── testapp/
│ └── stud.html
│
├── static/
│ └── css/
│ └── stud.css
│
├── populate.py
├── manage.py
├── README.md
└── .gitignore

```
---
## ▶️ How to Run
- Install required packages `requirements.txt`
- Configure database in `settings.py`
- Update DATABASES as per your system (SQLite / MySQL / PostgreSQL)
- Apply migrations
  ```
  python manage.py makemigrations
  python manage.py migrate

  ```
- Populate fake data `python populate.py`
- Run the server `python manage.py runserver`
- Open in browser send request `http://127.0.0.1:8000/students` 


---

## Author & Contact
<strong>Rajat Kumar Bal</strong><br>
📧 Email: rajatkumarbal961@gmail.com<br>
🔗 <a href="https://www.linkedin.com/in/rajat-kumar-bal">LinkedIn</a>
