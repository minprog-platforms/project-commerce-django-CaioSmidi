from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass


# class Category(models.Model):
#     category = models.CharField(max_length=64)
#
#     def __str__(self):
#         return f"{self.category}"


class Listing(models.Model):

    categories = [("TENN", "Tennis"), ("FOOT", "Football"), ("BASE", "Baseball"), ("BASK", "Basketball"), ("HOCK", "Hockey"), ("OTHER", "Other Sports")]

    title = models.CharField(max_length=64)
    description = models.TextField()
    image_URL = models.URLField(blank=True)
    price = models.DecimalField(max_digits=64, decimal_places=2)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name="seller")
    active = models.BooleanField(default=True)
    category = models.CharField(max_length=64, choices=categories, default="TENN")

    def __str__(self):
        return f"Listing {self.id}: {self.title}, sold by {self.owner}"

class Watchlist(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    item = models.ForeignKey(Listing, on_delete=models.CASCADE)


    def __str__(self):
        return f"{self.item} on Watchlist of {self.user}"

class Bid(models.Model):
    listing = models.ForeignKey(Listing, on_delete=models.CASCADE)
    bidder = models.ForeignKey(User, on_delete=models.CASCADE)
    bid_price = models.DecimalField(max_digits=64, decimal_places=2)


    def __str__(self):
        return f"{self.bidder} bid on {self.listing} for €{self.bid_price}"


class Comment(models.Model):
    listing = models.ForeignKey(Listing, on_delete=models.CASCADE)
    commenter = models.ForeignKey(User, on_delete=models.CASCADE)
    comment = models.TextField(blank=False)


    def __str__(self):
        return f"Comment {self.id} on listing {self.listing} written by {self.text}"
