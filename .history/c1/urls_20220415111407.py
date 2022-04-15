



from . import views
from django.urls import path


urlpatterns=[
    path('',views.nav),
    path('/analyze',views.analyze),
]