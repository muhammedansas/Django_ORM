from django.shortcuts import render
from . models import Student,Book,Store,Department,Employees
from django.db.models import Q,Sum,F
from django.db.models.functions import Length


# Create your views here.

# example of select related :                                                   # when we use foreign key to a model and print the values of that foreign key model in that case there is so many queris works because that will checke each element of that model so thats why that take so meny queries we can solve that with the help of select related

# this makes inner join for that and reduce the queries
# //////////////////////////////////////
def home(request): 
    new = Employees.objects.all().select_related('department')                
    for i in new:
        print(i.name,i.department.name)                                       # printing foreign key model name
    
    return None



# ///////////////////////////////////////////////////////

# example of prefetch related:

# ////////////////////////////////////////////////////////

# def home(request):
#     new = Book.objects.all().prefetch_related('aa')                             # that is a related of store models books field.in that case i givened that name i didnt give a related name in that model then that name will be 'store_set'.that meaning is we can get values from store using book model(the oposite direction) 
#     for i in new:
#         print(i.aa.all())





# /////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

# BULK_UPDATE :
# /////////////////////////////////////

# bulk update using for loop:


# updates = [
#     {'id': 1, 'price': 19.99},
#     {'id': 2, 'price': 29.99},
#     {'id': 3, 'price': 39.99},
# ]

# for update in updates:
#     # Fetch the book instance
#     book = Book.objects.get(id=update['id'])
#     # Update the price
#     book.price = update['price']
#     # Save the changes
#     book.save()


# Performance: Updating records one by one with save() can be slower, especially if you have a large number of records, due to the multiple database queries. Each save() call generates a separate SQL UPDATE query.


# Transaction Management: If you're updating many records and want to ensure that either all updates succeed or none of them do, you should use Django’s transaction management to wrap the updates in a transaction.:

# from django.db import transaction

# try:
#     with transaction.atomic():
#         for update in updates:
#             book = Book.objects.get(id=update['id'])
#             book.price = update['price']
#             book.save()
# except Exception as e:
#     # Handle the exception if needed
#     print(f"An error occurred: {e}")


# This ensures that if an error occurs, all changes are rolled back, maintaining database consistency.

# Bulk Update for Efficiency: If performance is a concern and you’re updating many records, consider using bulk_update() for efficiency, as it reduces the number of database queries to just one.


# Summary:
# Individual Updates: Use the save() method on each model instance if you need to update records individually
# Performance: For large datasets, consider bulk_update() for efficiency.
# Transaction Management: Use transaction.atomic() to ensure all updates are applied successfully or none are applied in case of an error.






