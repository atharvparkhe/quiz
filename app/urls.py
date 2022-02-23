from django.urls import path
from . import views
from .views import *


urlpatterns = [
	path('all-categories/', views.CategoryListView.as_view(), name="all-categories"),
]