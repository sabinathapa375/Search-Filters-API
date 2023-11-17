from django.urls import path, include
from apiapp import views
 

urlpatterns = [
    path('studentapi/', views.StudentListView.as_view(), name='studentapi'),
    path('auth/', include('rest_framework.urls', namespace='rest_framework'))
 ]
