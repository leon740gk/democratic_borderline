from django.urls import path

from api.person import views

urlpatterns = [
    path('latest_crossers/', views.LatestBorderCrossersView.as_view(), name='latest_crossers'),
    path('create_person/', views.CreatePersonView.as_view(), name='create_person'),
]

app_name = 'api_person'