from django.urls import path
from .views import Add_village, List_village, Detail_village, Update_village, Delete_village

urlpatterns = [
    path('add/', Add_village.as_view()),
    path('list/', List_village.as_view()),
    path('detail/<int:pk>/', Detail_village.as_view()),
    path('update/<int:pk>/', Update_village.as_view()),
    path('delete/<int:pk>/', Delete_village.as_view()),
]
