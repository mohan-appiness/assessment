from django.urls import path
from apps.businessinfo.views import BusinessInformationAdd, BusinessInformationDelete, BusinessInformationUpdate, BusinessInformationListing, BusinessInformationSearch, AddFormpageView, ListFormpageView, IndexFormpageView


urlpatterns = [
    path('create-business/', BusinessInformationAdd.as_view()),
    path('update-business/', BusinessInformationUpdate.as_view()),
    path('delete-business/', BusinessInformationDelete.as_view()),
    path('list-all-business/', BusinessInformationListing.as_view()),
    path('search-business/', BusinessInformationSearch.as_view()),
    path('index/', IndexFormpageView.as_view()),
    path('add/', AddFormpageView.as_view()),
    path('list/', ListFormpageView.as_view()),
]