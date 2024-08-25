'''In Django's ORM, annotate and aggregate are both methods used for performing aggregations on querysets, but they serve slightly different purposes and produce different types of results:

1. annotate
Purpose: annotate is used to add new fields to each object in a queryset based on aggregations or annotations from related models or existing fields.
Result: Each object in the queryset gets additional fields annotated with the result of the aggregation or annotation.'''

from django.db.models import Count

# Annotate each CustomUser with the total number of contacts
users_with_contact_count = CustomUser.objects.annotate(
    total_contacts=Count('contacts')
)



'''In this example, annotate adds a total_contacts field to each CustomUser object in the queryset, showing the count of related Contact objects.

2. aggregate
Purpose: aggregate is used to perform aggregations across the entire queryset and returns a single result for the entire queryset.
Result: Returns a dictionary-like object with the aggregated values.
'''

from django.db.models import Count

# Aggregate the total number of users
total_users = CustomUser.objects.aggregate(
    total_users=Count('id')
)

'''
In this example, aggregate computes the total number of CustomUser objects in the queryset and returns it as a single value in a dictionary-like object.

Key Differences
Output:

annotate adds fields to each object in the queryset, so the output is still a queryset where each object has additional fields.
aggregate returns a single result that summarizes the entire queryset, typically as a dictionary-like object with aggregated values.
Usage Context:

Use annotate when you want to add information to each object in the queryset based on related models or existing fields.
Use aggregate when you need a single result that summarizes the entire queryset, such as counting, averaging, or finding maximum/minimum values.
Aggregation Functions:

Both annotate and aggregate support aggregation functions like Count, Sum, Avg, etc. However, annotate applies these functions per object in the queryset, while aggregate applies them to the entire queryset.
Summary
Use annotate to add fields to each object in a queryset based on related models or existing fields.
Use aggregate to compute aggregations across the entire queryset and obtain a single result.
These methods provide powerful ways to manipulate and aggregate data in Django's ORM, catering to different needs depending on whether you want to enrich individual objects or compute summary statistics for the entire queryset.'''


# Annotate each CustomUser with the total number of contacts.
# Annotate each CustomUser with the total number of spam contacts.
# Include a field from the CustomUser model, like the user's name.

from django.db import models
from django.db.models import Count, Q, F

# Assuming models CustomUser and Contact are already defined as previously shown

# Example query to fetch CustomUsers annotated with counts and include the user's name
custom_users_with_counts = CustomUser.objects.annotate(
    total_contacts=Count('contacts'),  # Total number of contacts
    spam_contacts=Count('contacts', filter=Q(contacts__is_spam=True)),  # Number of spam contacts
    user_name=F('name')  # Including the user's name
)

# only for total_contacts similar sql query
# SELECT customuser.id, customuser.name, COUNT(contact.id) AS total_contacts
# FROM customuser
# LEFT JOIN contact ON customuser.id = contact.user_id
# GROUP BY customuser.id, customuser.name;


# Accessing the annotated fields in each CustomUser instance
for user in custom_users_with_counts:
    print(f"User: {user.user_name}, Total Contacts: {user.total_contacts}, Spam Contacts: {user.spam_contacts}")



# In this example:

# Count('contacts') calculates the total number of related Contact objects for each CustomUser.
# Count('contacts', filter=Q(contacts__is_spam=True)) filters the related Contact objects to count only those where is_spam is True.
# F('name') is used to include the name field from the CustomUser model in the queryset. This allows you to reference fields from the same model within the annotate function.
# By using F expressions, you can include fields from the same model in your annotations. This approach is useful when you want to combine data from the main model and its related models in a single query, making it more efficient and easier to handle in your views or templates.


# Q Objects
# Q objects are used to encapsulate a collection of keyword arguments for complex lookups. They allow you to perform complex queries using logical operators (& for AND, | for OR, and ~ for NOT). This is particularly useful for combining multiple conditions in a single query.

# Usage of Q objects:

# Combining multiple conditions: You can use Q objects to combine multiple conditions with AND or OR operators.
# Filtering based on related models: You can filter querysets based on fields in related models.
# Negating conditions: You can use the ~ operator to negate a condition.

# from django.db.models import Q

# Filter users who have either the name 'John' or a phone number starting with '123'
users = CustomUser.objects.filter(Q(name='John') | Q(phone_number__startswith='123'))

# Filter users who do not have the name 'John'
users = CustomUser.objects.filter(~Q(name='John'))


# F Expressions
# F expressions are used to refer to model field values directly in the database. They allow you to perform database operations involving model fields without pulling the data into Python, which makes the operations more efficient.

# Usage of F expressions:

# Referencing model fields: You can reference fields on the same model or related models within queries.
# Performing arithmetic operations: You can perform arithmetic operations on model fields.
# Updating fields based on their current values: You can update a field's value based on its current value without fetching the object into Python.

# from django.db.models import F

# # Increment the age of all users by 1
CustomUser.objects.update(age=F('age') + 1)

# # Annotate users with their name for further processing
users_with_names = CustomUser.objects.annotate(user_name=F('name'))


# c = CustomUser.objects.annotate(count_contacts = Count('contacts'))
# >>> for i in c:
# ...     print(i.count_contacts)
# ... 
# 1
# 1
# 1
# 1
# 1
# 0
# 0
# 0
# 0
# 0
# 0