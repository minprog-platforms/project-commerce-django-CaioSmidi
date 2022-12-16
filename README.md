# Commerce

This application is E-Commerce like website where users are able to view, host and bid on listings.
It is also possible to add items to a watchlist.

## Design Document


* First I will describe the application workflow, by showing all pages including all
functionalities available on each page.

The index view of this application is the Active Listings Page. Here you see all
listings that are currently active. By clicking on of the listing items you will
be taken to that items specific listing page, about which will follow more later
in this document.
Then in the upper part of the page we have 5 different links, where each will take
you to the specified page, as explained in the sketch itself. Also notice that
these navigation buttons are visible and accessible on all pages in this application,
as also emphasized in the sketch.
A sketch of the Active Listings Page is provided below:
![]()

Another important page is the Create Listing Page. Here a signed in user can create
their own listing by filling in the form fields (image and category are optional)
and submitting the form. When the form is filled in validly the newly created
listing can be found on the Active Listings Page.
A sketch of the Create Listing Page is provided below:
![]()


Clicking on any specific listing on the Active Listings Page will take the user
to the Listing Page of that item. As shown in the sketch, the user has different
possible actions that they can perform on this page. If not on the watchlist,
the user can add it to their watchlist by clicking on that button, and vice versa.
It is also possible to place a comment on the Listing Page, and read other comments
that have been placed if any.
Besides that it is also possible to bid on the listed item, however the bid_price
should be higher than the current bid_price, otherwise the user will be presented
an error.
Lastly, if the user happens to be the owner of the listing, they have an option
to close the listing, which will cause the listing to be removed from the Active
Listings Page.
A sketch of the Listing Page is provided below:
![]()


Lastly, I have added a small sketch of the Django Admin Interface Page. Here, the
admin/superuser can manually create/add/delete instances of classes within the
dataset, as shown in the SQL lecture.
A sketch of the Django Admin Interface Page is provided below:
![]()


For the Watchlist page and Categories page I have not drawn separate sketches,
since these are extra and I am not sure whether I will be able to implement these
pages.


* Next, I have drawn the Class Diagram according to the classes that I will use
to implement this application. It is clear to see that the classes User and
Listing are connected to basically all other classes, and will be therefore the
most essential in our dataset.
My sketch of the Class Diagram used for this application is provided below:
![]()


* Lastly we will look at which pages will be using what information from the
database.
It is clear that pretty much all pages will be needing the data from the User and
Listing classes.

The Active Listings Page will also need information from the Bid class to determine
the current prices of the listings.

The Create Listing Page will not need any additional information, but will be
connected to basically all fields in the Listing class.

The Listing Page will also be displaying information of the Bid and Comment classes,
as well as the Watchlist class. Also basically all fields of the Listing class
will be used on this page.
