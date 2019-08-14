from django.urls import path
from . import views

# namespace for menu
app_name = 'menu'
urlpatterns = [
	# /menu/
	path('', views.allitems, name='allitems'),

	# /menu/drink/5/
	path('drink/<int:drink_id>/', views.drinkdetail, name='drinkdetail'),

	# /menu/snack/2/
	path('snack/<int:snack_id>/', views.snackdetail, name='snackdetail'),

	# /menu/add/
	path('add/', views.additem, name='additem'),

	# /menu/edit/
	path('edit/', views.edititem, name='edititem'),

	# /menu/delete/
	path('delete/', views.deleteitem, name='deleteitem'),
]