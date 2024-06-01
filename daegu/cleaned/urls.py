from django.urls import path
from .views import cleaned_posts_list

urlpatterns = [
    path('cleaned-posts/', cleaned_posts_list, name='cleaned_posts_list'),
]
