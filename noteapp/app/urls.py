from django.urls import path
from  . import views
urlpatterns = [
    path("",views.index ,name ="index"),
    path("<id>/delete",views.delete,name="delete")
]