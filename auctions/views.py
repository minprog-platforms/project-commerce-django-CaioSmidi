from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django import forms

from .models import User, Listing, Bid, Comment


class NewListingForm(forms.ModelForm):

    title = forms.CharField(max_length=64)
    description = forms.CharField(max_length=128)
    starting_bid = forms.DecimalField(max_digits=64, decimal_places=2)
    image_URL = forms.URLField(required=False)
    category = forms.ChoiceField(required=False, choices=Listing.categories)

    class Meta:
        model = Listing
        fields = ["title", "description", "starting_bid", "image_URL", "category"]

class BiddingForm(forms.ModelForm):

    class Meta:
        model = Bid
        fields = ["price_bid"]


class PlaceCommentForm(forms.ModelForm):
    pass

    class Meta:
        model = Comment
        fields = ["listing", "commenter", "comment"]


def index(request):

    listings = Listing.objects.filter(active=True)

    return render(request, "auctions/index.html", {
        "active_listings": listings,
    })


def create_listing(request):
    if request.method == "POST":
        form = NewListingForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data["title"]
            description = form.cleaned_data["description"]
            starting_bid = form.cleaned_data["starting_bid"]
            image_URL = form.cleaned_data["image_URL"]
            category = form.cleaned_data["category"]
            user = request.user

            listing = Listing(title = title, description = description, image_URL = image_URL, starting_bid = starting_bid, category = category, owner = user)
            listing.save()

            return HttpResponseRedirect(reverse(index))
        else:
            return render(request, "auctions/create_listing.html", {
                "form": form,
                "categories": Listing.categories
            })
    else:
        return render(request, "auctions/create_listing.html", {
            "form": NewListingForm(),
            "categories": Listing.categories
        })


def listing(request, listing_id):

    listing = Listing.objects.get(pk=listing_id)
    user = User.objects.get(pk=request.user.id)

    if request.user.is_authenticated:

        if listing.active:

            highest_bid = Bid.objects.filter(listing=listing_id).order_by("price_bid").first()

            if request.user.id == listing.owner.id:
                return render(request, "auctions/control_listing.html", {
                    "price": highest_bid
                })

            else:

                return render(request, "auctions/listing.html", {
                    "title": listing.title,
                    "active": listing.active,
                    "image": listing.image_URL,
                    "description": listing.description,
                    "price": highest_bid,
                    "owner": listing.owner
                })

        else:

            if request.user.id == listing.owner.id:
                return render(request, "auctions/closed_listing_seller.html", {

                })

            else:
                return render(request, "auctions/closed_listing_user.html", {

                })

    else:
        pass


    # listing = Listing.objects.get(id=listing_id)
    #
    # if listing.active:
    #
    #     comments = Comment.objects.filter(listing=listing_id)
    #
    #     return render(request, "auctions/listing.html", {
    #         "listing": listing
    #     })
    #     if request.user.is_authenticated:
    #         watchlist_listing = Watchlist.objects.get(listing=listing_id, user=User.objects.get(pk=request.user.id))
    #         if watchlist_listing is None:
    #             listing_on_watchlist = False
    #         else:
    #             listing_on_watchlist = True
    #     else:
    #         listing_on_watchlist = False
    #
    #
    # else:
    #     pass


def watchlist(request):
    pass

def categories(request):
    pass

def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "auctions/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "auctions/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "auctions/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "auctions/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "auctions/register.html")