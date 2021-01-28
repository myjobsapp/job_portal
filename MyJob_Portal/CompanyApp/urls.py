from django.urls import path
from . import views
urlpatterns = [

    ## Company view urls

    path('list/',views.CompanyListView.as_view(),name='list'),
    path('detail/<int:pk>/',views.CompanyDetailView.as_view(),name='detail'),
    path('create/',views.CreateCompanyView.as_view(),name='create'),
    path('update/<int:pk>/',views.UpdateComapnyView.as_view(),name='update'),
    path('delete/<int:pk>/',views.DeleteComapnyView.as_view(),name='delete'),

    ## Job view Urls

    path('joblist/', views.JobListView.as_view(), name='joblist'),
    path('jobdetail/<int:pk>/', views.JobDetailView.as_view(), name='jobdetail'),
    path('jobcreate/', views.CreateJobView.as_view(), name='jobcreate'),
    path('jobupdate/<int:pk>/', views.UpdateJobView.as_view(), name='jobupdate'),
    path('jobdelete/<int:pk>/', views.DeleteJobView.as_view(), name='jobdelete'),

    ##Defined views

    path('login', views.userlogin,name='login'),
]