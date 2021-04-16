from typing import ForwardRef
from django.db import models
from django.db.models.fields import CharField

# Create your models here.

class City(models.Model):
    name        = models.CharField(max_length=60, primary_key=True)
    latitude    = models.IntegerField()
    longitude   = models.IntegerField()

    def __str__(self):
        return "City: " + str(self.name) +" "+ str(self.latitude) +" "+ str(self.longitude)

class Neighborhood(models.Model):
    name    = CharField(max_length=60, primary_key=True)
    cityName    = models.ForeignKey(City, on_delete=models.CASCADE )
    
    def __str__(self):
        return "Neighborhood: " + str(self.name) +" in ->"+ str(self.cityName)

class Land(models.Model):
    address     = models.CharField(max_length=60, primary_key=True)
    postalCode  = models.CharField(max_length=60)
    sqrAcres    = models.DecimalField(max_digits=1000, decimal_places=3)
    neighborhoodName = models.ForeignKey(Neighborhood, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return "Land: " +str(self.address) +" "+ str(self.postalCode) +" "+ str(self.sqrAcres) \
                        + str(self.neighborhoodName)

class Developer(models.Model):
    companyName = models.CharField(max_length=60, primary_key=True)
    headQuarters = models.CharField(max_length=60)
    
    def __str__(self):
        return "Developer: " + str(self.companyName) +" "+ str(self.headQuarters)

class Owner(models.Model):
    email        = models.CharField(max_length=60)
    phoneNumber = models.CharField(max_length=15)
    ownerId     = models.IntegerField(primary_key=True)

    def __str__(self):
        return "Owner: " + str(self.ownerId) +" "+ str(self.phoneNumber) +" "+ str(self.email)

class PersonOwner(models.Model):
    ownerId     = models.ForeignKey(Owner, on_delete=models.CASCADE)
    firstName   = models.CharField(max_length=60)
    middleName  = models.CharField(max_length=60)
    lastName    = models.CharField(max_length=60)
    
    def __str__(self):
        return "PersonOwner: " + str(self.ownerId) +" "+ str(self.firstName) +" "+ str(self.middleName) +" "+ str(self.lastName)

class CompanyOwner(models.Model):
    ownerId     = models.ForeignKey(Owner, on_delete=models.CASCADE)
    companyName = models.CharField(max_length=60)
    companyType = models.CharField(max_length=60)

    def __str__(self):
        return "CompanyOwner: " + str(self.ownerId) +" "+ str(self.companyName) +" "+ str(self.companyType)

class BankOwner(models.Model):
    ownerId     = models.ForeignKey(Owner, on_delete=models.CASCADE)
    bankName    = models.CharField(max_length=60)
    headQuarters= models.CharField(max_length=60)

    def __str__(self):  
        return "BankOwner: " + str(self.ownerId) +" "+ str(self.bankName) +" "+ str(self.headQuarters)

class OwnsRelation(models.Model):
    ownerId     = models.ForeignKey(Owner, on_delete=models.CASCADE)
    land        = models.ForeignKey(Land, on_delete=models.CASCADE)
    
    def __str__(self):  
        return "OwnsRelation: " + str(self.ownerId) +" "+ str(self.land) 
   
class Building(models.Model):
    land = models.ForeignKey(Land, on_delete=models.CASCADE)
    developer = models.ForeignKey(Developer, on_delete=models.CASCADE)
    squareFootage = models.DecimalField(max_digits=100, decimal_places=3)
    numberOfStories = models.IntegerField()

    def __str__(self):
        return "Building: " +str(self.land) +" "+ str(self.developer) +" "+ str(self.squareFootage) +" "+ str(self.numberOfStories)

class CommercialBuilding(models.Model):
    building = models.ForeignKey(Building, on_delete=models.CASCADE)
    industryType = models.CharField(max_length=60)
    numberOfDesks = models.IntegerField()

    def __str__(self):
        return "CommecialBuilding: " + str(self.building) +" " + str(self.industryType) +" " + str(self.numberOfDesks)

class ResidentialBuilding(models.Model):
    building = models.ForeignKey(Building, on_delete=models.CASCADE)
    numberOfBathrooms = models.IntegerField()
    numberOfBedrooms  = models.IntegerField()

    def __str__(self):
        return "ResidentialBuilding: " + str(self.building) +" " + str(self.numberOfBathrooms) +" " + str(self.numberOfBedrooms)

class Renter(models.Model):
    renterId = models.IntegerField(primary_key=True)
    building = models.ForeignKey(Building, on_delete=models.CASCADE)
    firstName = models.CharField(max_length=60)
    middleName = models.CharField(max_length=60)
    lastName = models.CharField(max_length=60)
    phoneNumber = models.CharField(max_length=60)
    email = models.CharField(max_length=60)

    costPerMonth = models.DecimalField(max_digits=100, decimal_places=2)
    leaseDuration = models.IntegerField()

    def __str__(self):
        return "Renter: " + str(self.renterID) +" "+ str(self.building) + " "+ str(self.firstName) \
            +" "+ str(self.middleName) +" "+ str(self.lastName) + " "+ str(self.phoneNumber) \
            +" "+ str(self.email)
    