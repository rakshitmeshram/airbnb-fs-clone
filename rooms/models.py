from django.db import models
from django_countries.fields import CountryField
from core import models as core_models
from users import models as user_models

class AbstractItem(core_models.TimeStampedModel):

    """ Abstract Item """

    name = models.CharField(max_length=80)

    class Meta:
        abstract = True

    def __str__(self):
        return self.name


class RoomType(AbstractItem):

    """ Room Type """
    class Meta:
        verbose_name = "Room Type"
        ordering = ['name']

class Amenity(AbstractItem):

    """ Amenity """
    class Meta:
        verbose_name_plural = "Amenities"

class Facility(AbstractItem):

    """ Facility """
    class Meta:
        verbose_name_plural = "Facilities"

class HouseRule(AbstractItem):

    """ House Rule """
    class Meta:
        verbose_name = "House Rule"

class Photo(core_models.TimeStampedModel):

    """ Photo """
    caption = models.CharField(max_length=80)
    file = models.ImageField()
    room = models.ForeignKey("Room", on_delete=models.CASCADE)

    def __str__(self):
        return self.caption

class Room(core_models.TimeStampedModel):

    """ Room Model """

    
    name = models.CharField(max_length=140)
    description = models.TextField()
    country = CountryField()
    city = models.CharField(max_length=80)
    price = models.IntegerField()
    address = models.CharField(max_length=140)
    guests = models.IntegerField()
    beds = models.IntegerField()
    bedrooms = models.IntegerField()
    baths = models.IntegerField()
    check_in = models.TimeField()
    check_out = models.TimeField()
    instant_book = models.BooleanField(default=False)
    host = models.ForeignKey("users.User", on_delete=models.CASCADE) 
    room_type = models.ForeignKey("RoomType", on_delete=models.SET_NULL, null=True)
    amenities = models.ManyToManyField("Amenity", blank=True)
    facilities = models.ManyToManyField("Facility", blank=True)
    house_rule = models.ManyToManyField("HouseRule", blank=True)


    def __str__(self):
        return self.name