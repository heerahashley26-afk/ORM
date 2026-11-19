# Ex02 Django ORM Web Application
## Date: 19/11/2026

## AIM
To develop a Django Application to store and retrieve data from a Vehicle Service Database platform using Object Relational Mapping(ORM).





## DESIGN STEPS

### STEP 1:
Clone the problem from GitHub

### STEP 2:
Create a new app in Django project

### STEP 3:
Enter the code for admin.py and models.py

### STEP 4:
Detect changes and create migration files that describe how to modify the database schema

### STEP 5:
Execute the migration files and update the database schema to match your Django models

### STEP 6:
Create a superuser with full access rights to all models and data through the admin interface.

### STEP 7:
Apply the migration files of the created app to the database

### STEP 8:
Execute Django admin using localhost and create details for 10 entries

## PROGRAM
```
models.py
from django.db import models
from django.contrib import admin
class bike_service_DB(models.Model):
 Service_Number=models.IntegerField()
 Name=models.TextField(max_length=15)
 Bike_Number=models.TextField()
 Address=models.TextField()
 Mobile_Number=models.IntegerField()
 Date=models.IntegerField()
 Last_Service_Date=models.IntegerField()
class bike_service_DBAdmin(admin.ModelAdmin):
 list_display=["Service_Number","Name","Bike_Number","Address","Mobile_Number","Date","Last_Service_Date"]
admin.py
from django.db import models
from django.contrib import admin
bike_service_DB,bike_service_DBAdmin
admin.site.register(bike_service_DB,bike_service_DBAdmin)

```


## OUTPUT
<img width="1173" height="607" alt="Screenshot 2026-11-19 132519" src="https://github.com/user-attachments/assets/100a9253-1a57-40d8-86c5-02fbad74ce12" />



## RESULT
Thus the program for creating Online Food Delivery Database using ORM hass been executed successfully
