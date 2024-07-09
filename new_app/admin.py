from django.contrib import admin
from . models import Student,Book,Store,Department,Employees

admin.site.register(Student)
admin.site.register(Book)
admin.site.register(Store)
admin.site.register(Department)
admin.site.register(Employees)