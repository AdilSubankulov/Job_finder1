from django.db import models
from django.utils import timezone


class Job(models.Model):
    title = models.CharField(max_length=50)
    salary = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    location = models.CharField(max_length=100)
    description = models.TextField()
    company = models.CharField(max_length=50)
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)


class Resume(models.Model):
    urls = models.URLField(blank=True, null=True)
    title = models.CharField(max_length=50)
    Lastname = models.CharField(max_length=20)
    Firstname = models.CharField(max_length=20)
    Address = models.CharField(max_length=50)
    birthday = models.DateField()
    # models.PhoneNumberField(_(""))
    description = models.TextField()


    def publish(self):
        self.published_date = timezone.now()
        self.save()


    def __str__(self):
        return self.title
