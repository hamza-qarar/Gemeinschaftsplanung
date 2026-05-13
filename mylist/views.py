from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from .models import ShoppingItem

def mylist(request):
    if request.method == 'POST':
        list_type = request.POST.get('list_type', 'erledigungen')
        print('Received Data:', request.POST['itemName'], flush=True)
        ShoppingItem.objects.create(name=request.POST['itemName'], list_type=list_type)
    erledigungen = ShoppingItem.objects.filter(list_type='erledigungen')
    besorgungen = ShoppingItem.objects.filter(list_type='besorgungen')
    return render(request, 'shoppinglist.html', {'erledigungen': erledigungen, 'besorgungen': besorgungen})

def delete_item(request, item_id):
    if request.method == 'POST':
        item = get_object_or_404(ShoppingItem, id=item_id)
        item.delete()
        return JsonResponse({'success': True})
    return JsonResponse({'success': False}, status=405)
