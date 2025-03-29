from django.urls import path, include
from . import views

urlpatterns = [
    path('<int:id>',views.job_detail, name='job_detail'),
    path('',views.job_list, name='job_list'),

]
