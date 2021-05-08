from django.urls import path
from . import views

app_name = 'poll'
urlpatterns = [
    path('', views.IndexView.as_view() , name = 'index'),
    path('<int:pk>/', views.DetailView.as_view() , name = 'detail'),
    path('<int:pk>/results/', views.ResultsView.as_view() , name = 'result'),
    path('<int:question_id>/votes/', views.vote , name = 'vote' ),
]
