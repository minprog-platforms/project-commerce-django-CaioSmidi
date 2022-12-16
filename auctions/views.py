from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django import forms


from .models import User, Listing, Watchlist, Bid, Comment


class NewListingForm(forms.ModelForm):

    class Meta:
        model = Listing
        fields = ["title", "description", "image_URL", "price", "category"]
        widgets = {
            "title": forms.TextInput(attrs={
                    "class": "form-control",
                    "placeholder": "Title",
                    "style": "width: 200px; margin-bottom: 20px; border: 2px solid black;"
                }),
            "description": forms.Textarea(attrs={
                    "class": "form-control",
                    "placeholder": "Place your item description here",
                    "style": "margin-bottom: 20px; border: 2px solid black;"
                }),
            "image_URL": forms.URLInput(attrs={
                    "class": "form-control",
                    "placeholder": "Place the URL of your image here",
                    "style": "width: 400px; margin-bottom: 20px; border: 2px solid black;"
                }),
            "price": forms.NumberInput(attrs={
                    "class": "form-control",
                    "placeholder": "Price (in €)",
                    "style": "width: 150px; margin-bottom: 20px; border: 2px solid black;"
                }),
            "category": forms.Select(attrs={
                    "class": "form-control",
                    "placeholder": "Select category",
                    "style": "width: 150px; margin-bottom: 20px; border: 2px solid black;"
                }),
            }


class BiddingForm(forms.ModelForm):

    class Meta:
        model = Bid
        fields = ["bid_price"]
        widgets = {
            "bid_price": forms.NumberInput(attrs={
                    "class": "form-control",
                    "placeholder": "Place the amount of your bid",
                    "style": "width: 300px; border: 2px solid black;"
                })
        }


class PlaceCommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ["comment"]
        labels = {
            "comment": "Place a comment:"
        }
        widgets = {
            "comment": forms.Textarea(attrs={
                    "class": "form-control",
                    "placeholder": "Enter your comment here",
                    "style": "width: 400px; height: 150px; border: 2px solid black;"
                })
        }


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
            image_URL = form.cleaned_data["image_URL"]
            price = form.cleaned_data["price"]
            category = form.cleaned_data["category"]
            user = request.user

            listing = Listing(title = title, description = description, image_URL = image_URL, price = price, owner = user, category = category)
            listing.save()

            return HttpResponseRedirect(reverse(index))
        else:
            return render(request, "auctions/create_listing.html", {
                "form": form,
            })
    else:
        return render(request, "auctions/create_listing.html", {
            "form": NewListingForm(),
        })


def listing_page(request, listing_id):

    listing = Listing.objects.get(pk=listing_id)
    comments = Comment.objects.filter(listing=listing)

    if request.user.is_authenticated:

        user = request.user
        watchlist_item = Watchlist.objects.filter(user=user, item=listing)

        if listing.active:

            highest_bid = Bid.objects.filter(listing=listing_id).order_by("-bid_price").first()

            if request.user.id == listing.owner.id:
                return render(request, "auctions/listing.html", {
                    "listing": listing,
                    "watchlist_item": watchlist_item,
                    "bid_form": BiddingForm(),
                    "comment_form": PlaceCommentForm(),
                    "comments": comments
                })

            else:

                return render(request, "auctions/listing.html", {
                    "listing": listing,
                    "watchlist_item": watchlist_item,
                    "bid_form": BiddingForm(),
                    "comment_form": PlaceCommentForm(),
                    "comments": comments
                })

        else:

            if request.user.id == listing.owner.id:
                return render(request, "auctions/closed_listing_seller.html", {

                })

            else:
                    return render(request, "auctions/closed_listing_user.html", {
                        "highest_bid": highest_bid,
                    })

    else:
        return render(request, "auctions/listing.html", {
            "listing": listing
        })


def change_watch(request, listing_id):

    listing = Listing.objects.get(pk=listing_id)
    watchlist_item = Watchlist.objects.filter(user=request.user, item=listing)

    if request.method == "POST":
        if watchlist_item:
            watchlist_item.delete()
        else:
            new_watchlist_item = Watchlist(user=User.objects.get(id=request.user.id), item=listing)
            new_watchlist_item.save()

        return listing_page(request, listing_id)


def bid(request, listing_id):

    listing = Listing.objects.get(pk=listing_id)

    if request.method == "POST":
        bid_form = BiddingForm(request.POST)
        if bid_form.is_valid():
            listing = listing
            bidder = request.user
            bid_price = float(bid_form.cleaned_data["bid_price"])

            if bid_price <= 0:
                return render(request, "auctions/errorpage.html", {
                    "message": "Your bid must be higher than € 0."
                })

            highest_bid = Bid.objects.filter(listing=listing).order_by("-bid_price").first()
            if highest_bid is None or bid_price > highest_bid.bid_price:
                if bid_price > listing.price:
                    bid = Bid(listing = listing, bidder = bidder, bid_price = bid_price)
                    bid.save()
                    listing.price = bid_price
                    listing.save()

                    return HttpResponseRedirect(reverse(index))

            return render(request, "auctions/errorpage.html", {
                "message": "Your bid must be higher than the current price."
            })


def close(request, listing_id):

    listing = Listing.objects.get(pk=listing_id)

    if request.method == "POST":

        listing.active = False
        listing.save()

    return render(request, "auctions/closed_listing_seller.html", {
        "listing": listing,
    })


def comment(request, listing_id):

    listing = Listing.objects.get(pk=listing_id)

    if request.method == "POST":
        comment_form = PlaceCommentForm(request.POST)
        if comment_form.is_valid():

            content = comment_form.cleaned_data["comment"]

            comment = Comment(listing= listing, commenter=User.objects.get(id=request.user.id), comment=content)
            comment.save()

        return listing_page(request, listing_id)

    # else:
    #     return render(request, "auctions/errorpage.html", {
    #         "message": "Not possible"
    #     })



def watchlist(request):

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
