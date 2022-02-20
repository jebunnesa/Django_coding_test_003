# Django_coding_test_003


## Getting Started

Setup project 
```bash
$ python3 -m venv venv
$ source venv/bin/activate
(venv)$ pip3 install -r requirements.txt


(venv)$ python manage.py migrate
(venv)$ python manage.py runserver
```

## Features

● Admin can create multiple surveys.
● In each survey, the admin can add multiple questions.
● Depending on one question’s answer another question can be shown.
● For each question, its answer could be of multiple types, like text-field,
number-field, dropdown, checkbox, radio button, etc.
● In dropdown or checkbox or these types of answers, the admin can give multiple
options.
● Admin can see each survey’s question’s answers in a list.
● Admins can see the submissions of customers in a report

Here are the requirements for customers:
<!-- ● Users can log into the customer portal. -->
● Users can select surveys from the list.
● Users can answer questions.
● Users can submit the form with the answer.
