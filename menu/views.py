from django.views.generic import TemplateView
from django.shortcuts import get_object_or_404, render
from .models import Drink, Snack
from .forms import addForm, deleteForm

# Create your views here.

# /menu/
def allitems(request):
	drink_menu = Drink.objects.order_by('drink_name')[:len(Drink.objects.all())]
	snack_menu = Snack.objects.order_by('snack_name')[:len(Snack.objects.all())]
	context = {'drink_menu': drink_menu, 'snack_menu': snack_menu}
	return render(request, 'menu/allitems.html', context)

#################################################################

# /menu/snack/2/
def snackdetail(request, snack_id):
	current_snack = get_object_or_404(Snack, pk=snack_id)
	context = {'current_snack': current_snack}
	return render(request, 'menu/snackdetail.html', context)

# /menu/drink/5/
def drinkdetail(request, drink_id):
	current_drink = get_object_or_404(Drink, pk=drink_id)
	context = {'current_drink': current_drink}
	return render(request, 'menu/drinkdetail.html', context)

#################################################################

# /menu/add/
def additem(request):
	form = addForm()
	return render(request, 'menu/add.html', {'form': form})

def postadd(request):
	form = addForm(request.POST)
	form2 = ingredForm()
	if form.is_valid():
		num_i = form.cleaned_data['Number_of_Ingredients']
		Item_Name = form.cleaned_data['Item_Name']
		s_or_d = form.cleaned_data['Snack_or_Drink']
	context = {'num_i': num_i, 'Item_Name': Item_Name, 's_or_d': s_or_d, 'form2': form2}
	render(request, 'menu/add.html', context)

###################################################################

# /menu/edit/
def edititem(request):
	form1 = deleteForm()
	form2 = addForm()
	return render(request, 'menu/edit.html', {'form1': form1, 'form2': form2})

###################################################################


# /menu/delete/
def deleteitem(request):
	form = deleteForm()
	return render(request, 'menu/delete.html', {'form': form})