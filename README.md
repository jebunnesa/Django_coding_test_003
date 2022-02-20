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

● Admin can create multiple surveys. <br/>
● In each survey, the admin can add multiple questions. <br/>
● Depending on one question’s answer another question can be shown. <br/>
● For each question, its answer could be of multiple types, like text-field,
number-field, dropdown, checkbox, radio button, etc. <br/>
● In dropdown or checkbox or these types of answers, the admin can give multiple
options. <br/>
● Admin can see each survey’s question’s answers in a list. <br/>
● Admins can see the submissions of customers in a report <br/>

Here are the requirements for customers:<br/>
<!-- ● Users can log into the customer portal. -->
● Users can select surveys from the list.<br/>
● Users can answer questions.<br/>
● Users can submit the form with the answer.<br/>
