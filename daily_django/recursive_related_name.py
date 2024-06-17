from django.db import models

class Person(models.Model):
    mother = models.ForeignKey('self', on_delete=models.CASCADE, null=True, related_name='son')
    siblings = models.ManyToManyField('self', related_name='ssiblings')
    partner = models.OneToOneField('self', on_delete=models.CASCADE, related_name='ppartner')

    def __str__(self):
        return self.mother


Mary = Person.objects.create()
Mary.save()
john= Person.objects.create(mother = Mary)
john.save()
john.mother
Mary.son.get()