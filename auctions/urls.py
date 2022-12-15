from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("create_listing", views.create_listing, name="create_listing"),
    path("<int:listing_id>", views.listing_page, name="listing"),
    path("<int:listing_id>/change_watch", views.change_watch, name="change_watch"),
    path("<int:listing_id>/bid", views.bid, name="bid"),
    path("<int:listing_id>/comment", views.comment, name="comment"),
    path("<int:listing_id>/close", views.close, name="close"),
    path("watchlist", views.watchlist, name="watchlist")
    # path("categories", views.categories, name="categories"),
]
