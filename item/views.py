from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST
from django.shortcuts import redirect, render, get_object_or_404
from django.db.models import Q
from .forms import NewItemForm, EditItemForm
from item.models import Item, Category

def items(request):
    query = request.GET.get('query', '')
    category_id = request.GET.get('category', '')
    categories = Category.objects.all()
    items = Item.objects.filter(is_sold=False)
    
    if category_id:
        items = Item.objects.filter(Q(category_id=int(category_id)))
    
    if query:
        items = Item.objects.filter(Q(name__icontains=query) | Q(description__icontains=query))

    return render(request, 'item/items.html', {
        'items': items,
        'query': query,
        'categories': categories,
        'category_id': category_id,
    })   



def detail(request, item_id: int):
    item = get_object_or_404(Item, pk=item_id)
    related_items = Item.objects.filter(category=item.category_id,is_sold=False).exclude(pk=item_id)[0:3]
    return render(request, 'item/detail.html', {
        'item': item,
        'related_items': related_items,
    })

@login_required
def new(request):
    if request.method == 'POST':
        form = NewItemForm(request.POST, request.FILES)
        
        if form.is_valid():
            item = form.save(commit=False)
            item.created_by = request.user
            item.save()
            return redirect('item:detail', item_id=item.id)
    
    else:
        form = NewItemForm()
    
    return render(request, 'item/form.html', {
        'form': form,
        'title': 'New Item',
    })
    
@require_POST
@login_required
def delete(request, item_id):
    item = get_object_or_404(Item, pk=item_id, created_by=request.user)
    item.delete()
    return redirect('dashboard:index')

@login_required
def edit(request, item_id):
    item = get_object_or_404(Item, pk=item_id, created_by=request.user)
    if request.method == 'POST':
        form = EditItemForm(request.POST, request.FILES, instance=item)
        
        if form.is_valid():
            item.save()
            return redirect('item:detail', item_id=item.id)
    
    else:
        form = EditItemForm(instance=item)
    
    return render(request, 'item/form.html', {
        'form': form,
        'title': 'Edit Item',
    })