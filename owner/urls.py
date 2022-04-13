
from django.urls import path
from owner.views import DogView, OwnerView

urlpatterns = [
    path('/owner', OwnerView.as_view()),
    path('/dog', DogView.as_view())
]

#http://127.0.0.1:8000/owners/owner
