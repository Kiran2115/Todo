"""apjct URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from apjct import views


urlpatterns = [
    path('', views.api_root),
    path('admin/', admin.site.urls),
    path('todos/', include('todolist.urls')),
    path('users/', include('users.urls')),
    path('auth/', include('rest_framework.urls')),


    # path('todos/', views. Todo_list),
    #path('todos/<int:pk>', views.todo_detail),
    #path('todos/<int:pk>/', views.Todo_Detail.as_view()),

    
]


"""
Resources
1. Scalar -> one resources -> Read 1, update, delete
2. collection -> collection of resources -> 

##################
# First Iteration
##################
/todos/<int:id> -> Get one single todo(GET), Update a todo(PUT/POST/PATCH), delete a todo(delete) 
/todos/ -> Get collection of todo's(GET), Create a todo(POST) 

id : auto generated

name: body
description: body
start_date: body
end_date: body

created_at
updated_at 

POST : {
'name' : body
'description' : body
'start_date' : body
'end_date' : body
user_id -> from the logged in user 
}

Actions:
/todos/<int:id>/start ---> waiting -> working( set the start date to current date)
/todos/<int:id>/complete----> working -> done(set the end_date to current date )


Actions:

'Working'
'done'
'waiting'


Default status -> waiting
waiting -> working( set the start date to current date)

------------------
##################
# Second Iteration
##################

If a user is logged in and its id is same as that of user_id associated with that todo 200 else throw 403/401
/todos/<int:id> -> Get one single todo(GET), Update a todo(PUT/POST/PATCH), delete a todo(delete)
 
show todos as per the logged in user

if uid doesn't match the uid of logged in user throw/raise 403
/user/<int:user_id>/todos/ -> Get collection of todo's(GET), Create a todo(POST)  

only accessible to Admin
/todos/ -> Get collection of todo's(GET), Create a todo(POST) ---> List of todos that belongs to user with the given user 


Actions:
/todos/<int:id>/start
/todos/<int:id>/complete


User
    id(uniq)
    name:
    email:
    pass

Todo
    id(uniq)
    name
    status
    user_id (foreignKey)
    
"""

