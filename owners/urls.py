
from django.urls import path, include

urlpatterns = [
    path('owners', include('owner.urls'))
]

#폴더, 앱