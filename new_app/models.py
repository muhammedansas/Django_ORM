from django.db import models


class Student(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    place = models.CharField(max_length=100)
    department = models.CharField(max_length=20)

    def __str__(self):
        return self.name
    
class Book(models.Model):
    name = models.CharField(max_length=100)
    price = models.IntegerField()

class Store(models.Model):
    name = models.CharField(max_length=100)
    books = models.ManyToManyField(Book,related_name='aa')

class Department(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Employees(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    department = models.ForeignKey(Department,on_delete=models.CASCADE)

    def __str__(self):
        return self.name