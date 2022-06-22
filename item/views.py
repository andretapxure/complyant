from django.shortcuts import redirect, render
from .forms import ItemForm
from .models import Item


def item_list(request):
    context = {'items': Item.objects.all()}
    return render(request, "item/item_list.html", context)


def item_form(request, id=0):
    if request.method == 'GET':
        if id == 0:
            form = ItemForm()
        else:
            item = Item.objects.get(pk=id)
            form = ItemForm(instance=item)
        return render(request, "item/item_form.html", {'form': form})
    if request.method == 'POST':
        if id == 0:
            form = ItemForm(request.POST)
        else:
            item = Item.objects.get(pk=id)
            form = ItemForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
        return redirect('/item/list')


def item_delete(request, id):
    item = Item.objects.get(pk=id)
    item.delete
    return redirect('/item/list')
