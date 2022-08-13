from django.urls import path
from . import views

urlpatterns = [
  path('', views.index, name='index'),
  path('submit-project',views.submit_project, name='submit_project'),
  path('search/',views.search_results, name='search_results'),
  path('rate/<int:id>/',views.rate_project,name='rate_project'),


]