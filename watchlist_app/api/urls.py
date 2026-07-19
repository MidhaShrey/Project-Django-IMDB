from django.urls import path
from rest_framework.routers import DefaultRouter
from django.urls import include
from watchlist_app.api.views import *

router = DefaultRouter()
router.register('stream', StreamPlatformVS, basename='streamplatform')

urlpatterns = [
    path('list/', WatchListAV.as_view(), name='watchlist-list'),
    path('list/detail/<int:primary_key>/', WatchListDetailsAV.as_view(), name='watchlist-details'),

    # path('stream/list/', StreamPlatformAV.as_view(), name='streamplatform-list'),
    # path('stream/detail/<int:primary_key>/', StreamPlatformDetailsAV.as_view(), name='streamplatform-details'),

#  below code solves the issue of different urls for list and detail view by use of router
    path('', include(router.urls)),

    path('stream/<int:primary_key>/review-create/', ReviewCreate.as_view(), name='review-create'),
    path('stream/<int:primary_key>/review/', ReviewList.as_view(), name='review-list'),
    path('stream/review/<int:pk>/', ReviewDetails.as_view(), name='review-details'),
    path('api-auth', include('rest_framework.urls', namespace='rest_framework'))
]

# Class Based Views
# urlpatterns = [
#     path('list/', MovieListAV.as_view(), name='movie-list'),
#     path('detail/<int:primary_key>/', MovieDetailsAV.as_view(), name='movie-details'),
# ]

# Function Based Views
# urlpatterns = [
#     path('list/', movie_list, name='movie-list'),
#     path('detail/<int:primary_key>/', movie_details, name='movie-details'),
# ]
