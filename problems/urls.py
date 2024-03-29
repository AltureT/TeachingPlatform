from django.urls import path

from . import views

app_name = 'problems'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<int:problem_id>/', views.detail, name='detail'),
    path('add/', views.add, name='add'),
    path('addtodb', views.add_to_db, name='add_to_db'),
]
