from django.db import models

# Create your models here.
from django.db.models import (
    Model,
    CharField,
    URLField,
    DateField,
    ImageField,
    TextField,
)
from django_extensions.db.fields import CreationDateTimeField, ModificationDateTimeField


class Product(Model):
    """
    Model to store all products with respective data
    """

    product_name = CharField(max_length=100, unique=True)
    description = CharField(max_length=500, blank=True)
    image_url = ImageField()
    url = URLField(max_length=100, null=True)
    created_date = CreationDateTimeField(null=True)
    updated_date = ModificationDateTimeField(null=True)

    def __str__(self):
        return f"{self.name}"


class Testimonial(Model):
    """
    Model to store all testimonials with respective data
    """

    name = CharField(max_length=100, unique=True)
    profile = CharField(max_length=100)
    comment = CharField(max_length=500)
    created_date = CreationDateTimeField(null=True)
    updated_date = ModificationDateTimeField(null=True)

    def __str__(self):
        return f"{self.name}"


class TeamMember(Model):
    """
    Model to store all team members with respective data
    """

    name = CharField(max_length=100)
    profile = CharField(max_length=100)
    image_url = ImageField()
    description = CharField(max_length=500, blank=True)
    linkedin = URLField(max_length=100, null=True)
    email = URLField(max_length=100, null=True)
    created_date = CreationDateTimeField(null=True)
    updated_date = ModificationDateTimeField(null=True)

    def __str__(self):
        return f"{self.name}"


class Project(Model):
    """
    Model to store all products with respective data
    """

    project_name = CharField(max_length=100, unique=True)
    description = CharField(max_length=500, blank=True)
    image_url = ImageField()
    url = URLField(max_length=100, null=True)
    created_date = CreationDateTimeField(null=True)
    updated_date = ModificationDateTimeField(null=True)

    def __str__(self):
        return f"{self.project_name}"


class MiscData(Model):
    """Model to store Misc data"""

    key = CharField(max_length=100, unique=True)
    data = TextField(max_length=1000)
    created_date = CreationDateTimeField(null=True)
    updated_date = ModificationDateTimeField(null=True)

    def __str__(self):
        return f"{self.key}"
