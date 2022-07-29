# import-data-from-json-format-to-model

In this project, we are going to see how to import data from json format to model. We can import data from json, csv, xlsx, yml, etc. to model.

First of all, create a Django project and an app. Set up urls and do some basic stuff like adding the app in INSTALLED_APPS.
Create a model. Here, we don't have much to do with views.py, urls.py or any html file. We only have to work with settings.py, admin.py, models.py and admin.

Example
Install the django-import-export package − step1
pip install django-import-export


In settings.py, add the following line − step2
INSTALLED_APPS += ['import_export']


Create a model − step3
class StudentData(models.Model):
   name=models.CharField(max_length=100)
   standard=models.CharField(max_length=100)
   section=models.CharField(max_length=100)
   
   
In admin.py − step4
from django.contrib import admin
from .models import StudentData
from import_export import resources
from import_export.admin import ImportExportModelAdmin

class StudentResource(resources.ModelResource):
   class Meta:
      model = StudentData
class StudentAdmin(ImportExportModelAdmin):
   resource_class = StudentResource

admin.site.register(StudentData,StudentAdmin)
Here we created a model resource for import and export. Then, we created an admin and registered it.



File format for JSON should be like this − step5
[
   {
      "id": 13,
      "name": "John",
      "standard":"10",
      "section": "B",
      "the_json": {"name":"Jhon"}
   }
]


Now just import the JSON file import_example.json and your data will be imported in Django model.

thank you and remain Blessed.
