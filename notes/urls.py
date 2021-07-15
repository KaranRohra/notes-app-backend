from rest_framework import routers
from . import views

route = routers.DefaultRouter()
route.register("", viewset=views.NoteApi)

urlpatterns = route.urls
