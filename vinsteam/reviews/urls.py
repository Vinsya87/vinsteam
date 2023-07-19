from django.urls import path
from reviews.views import AddReviewView, ReviewsList, get_full_review

app_name = 'reviews'

urlpatterns = [
    path('add-review/', AddReviewView.as_view(), name='add_review'),
    path('get_full_review/', get_full_review, name='get_full_review'),
    path('', ReviewsList.as_view(), name='reviews_list'),
]
