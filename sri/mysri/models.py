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


