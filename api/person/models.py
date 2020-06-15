from django.db import models

from api.person.define import BORDER_CROSS_TYPES, MARITAL_STATUS


class PersonsAddress(models.Model):

    street = models.CharField(max_length=255)
    street2 = models.CharField(max_length=255, null=True, blank=True)
    city = models.CharField(max_length=255)
    state = models.CharField(max_length=255, null=True, blank=True)
    zip_code = models.IntegerField()
    country = models.CharField(max_length=255)


class Person(models.Model):

    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)

    date_of_birth = models.DateTimeField()

    marital_status = models.IntegerField(choices=MARITAL_STATUS, default=MARITAL_STATUS.NOT_MARRIED)
    married_with = models.CharField(max_length=255, null=True, blank=True)

    living_address = models.ForeignKey(PersonsAddress, on_delete=models.CASCADE)
    # phone number field could be more specific type of field if needed
    phone_number = models.CharField(max_length=100)

    height = models.FloatField()
    nationality = models.CharField(max_length=255)
    color_of_eyes = models.CharField(max_length=255)


    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class ForbiddenStaff(models.Model):

    name = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return f'{self.name}'


class BorderCrossing(models.Model):

    person = models.ForeignKey(Person, related_name='border_crosses', on_delete=models.CASCADE)
    date_of_border_cross = models.DateTimeField(auto_now_add=True)
    border_cross_type = models.IntegerField(choices=BORDER_CROSS_TYPES, default=BORDER_CROSS_TYPES.IN)
    forbidden_stuff_withdrawn = models.ManyToManyField(ForbiddenStaff)
    allowed_pass = models.BooleanField(default=False)
