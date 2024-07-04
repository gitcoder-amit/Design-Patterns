
contact = Contact.objects.all()

contact[3].user
<CustomUser: 9>

CustomUser.objects.get(id=9).contacts    --> contacts is related name
<django.db.models.fields.related_descriptors.create_reverse_many_to_one_manager.<locals>.RelatedManager object at 0x7feff1ab7fa0>

CustomUser.objects.filter(id=9)[0].contacts.all()
<QuerySet [<Contact: contact2-2>]>


CustomUser.objects.prefetch_related('contacts').all()
<QuerySet [<CustomUser: 1>, <CustomUser: 2>, <CustomUser: 3>, <CustomUser: 4>, <CustomUser: 5>, <CustomUser: 6>, <CustomUser: 7>, <CustomUser: 8>, <CustomUser: 9>, <CustomUser: 10>, <CustomUser: 11>]>
>>> for i in CustomUser.objects.prefetch_related('contacts').all():
...     print(i.contacts.all())
... 
<QuerySet []>
<QuerySet []>
<QuerySet []>
<QuerySet []>
<QuerySet []>
<QuerySet []>
<QuerySet [<Contact: contact0-0>]>
<QuerySet [<Contact: contact1-1>]>
<QuerySet [<Contact: contact2-2>]>
<QuerySet [<Contact: contact3-3>]>
<QuerySet [<Contact: contact4-4>]>


Contact.objects.select_related('user').all()
<QuerySet [<Contact: ravi>, <Contact: contact0-0>, <Contact: contact1-1>, <Contact: contact2-2>, <Contact: contact3-3>, <Contact: contact4-4>]>




try:
    single_object = MyModel.objects.order_by('name').get(id=1)  # Not useful
except MyModel.DoesNotExist:
    single_object = None