Django Learning Roadmap (Beginner to Job-Ready)

⏱ Duration: ~2 Weeks Full-Time (8 hrs/day)

✅ Week 1: Core Foundations

📘 Day 1: First Steps

✅ Goal: Set up your environment and understand Django's architecture.

What to Learn:

What is Django? Why use it?

Install Python, pip, virtualenv

Install Django and create your first project (django-admin startproject)

Run the development server, understand settings.py, urls.py

Practice Task: Create a sample project and home page

📘 Day 2–3: Model Layer

✅ Goal: Learn how Django interacts with databases

What to Learn:

What are models and how to create them

Django ORM (QuerySet, filtering, CRUD operations)

makemigrations and migrate

Practice Task: Create a model for a blog (Post, Author), perform CRUD from the shell

📘 Day 4–5: View Layer

✅ Goal: Connect logic to routes

What to Learn:

What are views (function-based and class-based)

URL dispatcher (urls.py)

How to pass data to templates

Practice Task: Build views to list blog posts, view details

📘 Day 6: Template Layer

✅ Goal: Display dynamic content

What to Learn:

What are Django templates

Template syntax: {{ }}, {% %}, loops, conditionals

Template inheritance (base.html)

Practice Task: Build UI for blog with reusable templates

✅ Week 2: Dynamic Forms + Admin + Workflow

📘 Day 7: Forms

✅ Goal: Create and validate input forms

What to Learn:

forms.Form vs forms.ModelForm

Form validation

Displaying and handling forms in views

Practice Task: Create a comment form for blog posts

📘 Day 8: Admin

✅ Goal: Learn Django Admin for backend management

What to Learn:

Customizing the admin interface

Registering models

Adding search, filters, and inline editing

Practice Task: Admin for managing blog posts, authors

📘 Day 9: Development Process

✅ Goal: Understand best practices

What to Learn:

Project structure

Environment variables using .env

Using debug, static, media, collectstatic

Basic deployment intro (Heroku, Render, etc.)

Practice Task: Structure your blog as a clean Django app

📘 Day 10: Capstone Mini Project

✅ Goal: Apply everything you've learned

Build a complete mini app:

Blog or To-Do List with:

Models

Forms

Templates

Views

Admin panel

User Authentication (bonus)

🧠 Tips to Learn Efficiently

🔁 Repeat by doing: Avoid just reading—type out code and test.

🧪 Debug errors: It builds your real-world skills.

🗃️ Use Git: Even locally, to track changes and learn version control.

📚 Refer to the official docs: https://docs.djangoproject.com/en/stable/
-----------------------------------------------------------------------------------------------------

That’s a fantastic Day 2–3 goal, Venus! You're diving into the **Model Layer**, which is the heart of Django’s backend: **data structure + database logic**.

Let’s break this down so you:

* Understand the **what** and **why**
* Follow **step-by-step practice**
* Get hands-on with **Django ORM** and **CRUD operations**

---

## 📘 MODEL LAYER ROADMAP (For Day 2–3)

---

### ✅ **Goal** Recap:

> Learn how Django handles data using **models** and perform **Create, Read, Update, Delete (CRUD)** using the shell and ORM.

---

## 🔹 1. 🔍 What Are Models?

In Django, **models** are Python classes that represent **tables in the database**.

* Each **model class = database table**
* Each **class attribute = column (field)**

> You define your data in models.py, and Django creates the database structure from it.

🧠 Example:

```python
from django.db import models

class Author(models.Model):
    name = models.CharField(max_length=100)

class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
```

---

## 🔹 2. ✍️ Step-by-Step Practice Task: Blog Model (Post + Author)

### 🧱 Step A: Create a Django App

In your project folder:

```bash
python3 manage.py startapp blog
```

### 🧾 Step B: Register the App

In `settings.py`, add `'blog'` to `INSTALLED_APPS`:

```python
INSTALLED_APPS = [
    ...
    'blog',
]
```

### ✏️ Step C: Define Models

In `blog/models.py`:

```python
from django.db import models

class Author(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
```

---

## 🔹 3. 🧱 Migrations: Create & Apply Database Tables

Run these:

```bash
python3 manage.py makemigrations
python3 manage.py migrate
```

🎯 Outcome: Django creates tables for `Author` and `Post` in your SQLite DB.

---

## 🔹 4. 🛠 Register Models in Admin Panel

Edit `blog/admin.py`:

```python
from django.contrib import admin
from .models import Author, Post

admin.site.register(Author)
admin.site.register(Post)
```

🟢 Now open `http://127.0.0.1:8000/admin`, log in, and you'll see **Author** and **Post** there!

---

## 🔹 5. 🔁 Practice CRUD in Django Shell

Start the shell:

```bash
python3 manage.py shell
```

Then try:

### 🔹 CREATE

```python
from blog.models import Author, Post

a = Author.objects.create(name="Venus")
p = Post.objects.create(title="My First Post", content="Learning Django is fun!", author=a)
```

### 🔍 READ

```python
Author.objects.all()
Post.objects.all()
Post.objects.filter(author__name="Venus")
```

### 📝 UPDATE

```python
p = Post.objects.get(id=1)
p.title = "Updated Post Title"
p.save()
```

### ❌ DELETE

```python
p.delete()
Author.objects.get(id=1).delete()
```

---

## 📚 Suggested Learning Resources

### 🧠 Theory (Short Reads):

* [Django Models Intro – Official Docs](https://docs.djangoproject.com/en/stable/topics/db/models/)
* [Django ORM Cheat Sheet](https://learndjango.com/tutorials/django-orm-cheat-sheet)

### 📺 Practice Videos:

* [Corey Schafer Django Series – Models](https://youtu.be/Jg3Pz5rRReU?t=165)
* [Traversy Media Django Crash Course](https://youtu.be/e1IyzVyrLSU)

---

## ✅ Checklist for Completion

| Task                                 | Done? |
| ------------------------------------ | ----- |
| Created Django app `blog` ✅          | ☐     |
| Defined `Author` and `Post` models ✅ | ☐     |
| Ran `makemigrations` and `migrate` ✅ | ☐     |
| Registered models in admin ✅         | ☐     |
| Performed CRUD in Django shell ✅     | ☐     |

---

Would you like help building a simple front-end (form + page) to show and add posts from the browser next?
