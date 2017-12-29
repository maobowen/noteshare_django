from django.db import models


# Create your models here.
class Country(models.Model):
    id = models.CharField('Country ID', max_length=5, primary_key=True)  # us
    name = models.CharField('Country Name', max_length=100)  # United States of America

    def __str__(self):
        return self.id

    class Meta:
        ordering = ['name']


class University(models.Model):
    id = models.CharField('University ID', max_length=20, primary_key=True)  # columbia
    name = models.CharField('University Name', max_length=100)  # Columbia University
    country = models.ForeignKey(Country, on_delete=models.CASCADE, verbose_name='Country')

    def __str__(self):
        return self.id

    class Meta:
        ordering = ['country', 'name']


class Course(models.Model):
    id = models.CharField('Course ID', max_length=20, primary_key=True)  # coms1004
    number = models.CharField('Course Number', max_length=20)  # COMS W1004
    name = models.CharField('Course Name', max_length=100)  # Introduction To Computer Science
    university = models.ForeignKey(University, on_delete=models.CASCADE, verbose_name='University')
    subject = models.CharField('Course Subject', max_length=10)  # coms
    fontawesome = models.CharField('Font Awesome', max_length=50, default='book')

    def __str__(self):
        return self.id

    class Meta:
        ordering = ['id']
