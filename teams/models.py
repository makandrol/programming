
from django.db import models


class Customer(models.Model):
    name = models.CharField(max_length=15)

    def __unicode__(self):
        return self.name


class Manager(models.Model):
    name = models.CharField(max_length=15)

    def __unicode__(self):
        return self.name


class Developer(models.Model):
    name = models.CharField(max_length=15)
    qualification = models.CharField(max_length=15)
    hour_cost = models.IntegerField()
    isFree = models.BooleanField()

    def __unicode__(self):
        return self.name + " - " + self.qualification + " for " + str(self.hour_cost) + " gold per hour"


class Specification(models.Model):
    name = models.CharField(max_length=15)
    customer = models.ForeignKey(Customer)

    def __unicode__(self):
        return self.name


class Project(models.Model):
    name = models.CharField(max_length=15)
    manager = models.ForeignKey(Manager)
    specification = models.ForeignKey(Specification)

    def __unicode__(self):
        return self.name + " with manager " + str(self.manager)


class Job(models.Model):
    specification = models.ForeignKey(Specification)
    developer = models.ForeignKey(Developer)
    qualification = models.CharField(max_length=15)
    haveDeveloper = models.BooleanField()

    def __unicode__(self):
        return str(self.specification) + " need 1 " + str(self.qualification) + " programmer"


class Bill(models.Model):
    project = models.ForeignKey(Project)
    price = models.IntegerField()

    def __unicode__(self):
        return str(self.project) + " for " + str(self.price)