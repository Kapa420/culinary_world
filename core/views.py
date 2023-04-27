from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from item.models import Item, Category
from .forms import SignUpForm

def index(request):
    items = Item.objects.filter(is_sold=False).order_by('created_at')[0:3]
    categories = Category.objects.all()
    return render(request, 'core/index.html', {
        'categories': categories,
        'items': items,
    })

def contact(request):
    return render(request, 'core/contact.html')

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/log_in')
    else:
        form = SignUpForm()
        
    return render(request, 'core/sign_up.html', {
        'form': form,
    })

@login_required
def log_out(request):
    logout(request)
    return redirect('/')
