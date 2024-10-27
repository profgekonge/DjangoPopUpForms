from django.shortcuts import render, redirect
from . forms import ProductForm, CategoryForm
# Create your views here.



def index(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, prefix='form')
        formb = CategoryForm(request.POST, prefix='formb')
        
        if 'submit_add_inv' in request.POST:  # Check if submit button is clicked
            if form.is_valid():
                form.save()  # Save the form data to the database
                return redirect('inventory')  # Redirect back to inventory page
    else:
        form = ProductForm()
        formb = CategoryForm()
    context = {
        'form' :form,
        'formb': formb
    }
    
    return render(request, 'index.html', context)
