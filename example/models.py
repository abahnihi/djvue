from django.db import models


class Profile(models.Model):
    username = models.CharField(max_length=64)
    email = models.EmailField()
    # do not do this
    password = models.CharField(max_length=64)
    file = models.FileField(upload_to="profiles/")


class Address(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    name = models.CharField(max_length=64)
    country = models.CharField(
        max_length=2, choices=(("ro", "Romania"), ("kw", "Kuwait"))
    )
    zip_code = models.CharField(max_length=12)
    address = models.TextField(blank=True, default="")
