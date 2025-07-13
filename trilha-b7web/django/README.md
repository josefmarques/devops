python3 -m venv venv
source venv/bin/activate
deactivate
pip install django

##Criando um projeto django

django-admin startproject core .
python3 manage.py runserver
python3 manage.py startapp tarefas

M = Model --> Banco de dados
T = Template --> parte visual
V = é o porteiro, que direciona o que vai ser feito (controller)

