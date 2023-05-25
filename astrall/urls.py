from django.urls import path
from .views import core, CreatePhotoView

urlpatterns = [
    path('', core),
    path('create/', CreatePhotoView.as_view(), name="create"),
]