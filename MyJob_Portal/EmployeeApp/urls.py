from django.urls import path
from . import views

urlpatterns = [
    path('reg/',views.emp_register,name='emp_reg'),
    path('all/',views.all_emp,name='all_emp'),
    path('update/<int:oid>/',views.emp_update,name='update'),
    path('delete/<int:oid>oid=/',views.emp_delete,name='delete'),
    path('user/',views.usercreation,name='user'),
    path('login/',views.userlogin,name='login'),
    path('logout/',views.userlogout,name='logout'),
]