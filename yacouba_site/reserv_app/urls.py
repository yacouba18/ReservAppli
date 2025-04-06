from . import views
from django.urls import path 
from .views import creer_event

urlpatterns = [
path ('', views.index, name='index'),
path('creer_event/', creer_event, name='creer_event'),
path('/<int:evenement_id>/', views.modif_event, name='modif_event'),
path('delete/<int:evenement_id>/', views.delete_evenement, name='delete_evenement'),
path('lister_event/', views.lister_event, name='lister_event'),
path('evenements/', views.evenements, name='evenements'),
path('add_evenement/', views.add_evenement, name='add_evenement'),
path('edit_evenement/', views.edit_evenement, name='edit_evenement'),
path('delete_evenement/', views.delete_evenement, name='delete_evenement'),

]