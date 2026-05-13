from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from .models import ShoppingItem, ShoppingList, CalendarEvent, Note


def mylist(request):
    if request.method == 'POST':
        list_id = request.POST.get('list_id')
        shopping_list = get_object_or_404(ShoppingList, id=list_id)
        print('Received Data:', request.POST['itemName'], flush=True)
        ShoppingItem.objects.create(name=request.POST['itemName'], shopping_list=shopping_list)
    all_lists = ShoppingList.objects.prefetch_related('items').all()
    return render(request, 'shoppinglist.html', {'all_lists': all_lists})


def delete_item(request, item_id):
    if request.method == 'POST':
        item = get_object_or_404(ShoppingItem, id=item_id)
        item.delete()
        return JsonResponse({'success': True})
    return JsonResponse({'success': False}, status=405)


def edit_item(request, item_id):
    if request.method == 'POST':
        item = get_object_or_404(ShoppingItem, id=item_id)
        new_name = request.POST.get('newName', '').strip()
        if new_name:
            item.name = new_name
            item.save()
            return JsonResponse({'success': True})
    return JsonResponse({'success': False}, status=400)


def events(request):
    if request.method == 'POST':
        date_str = request.POST.get('date', '').strip()
        title = request.POST.get('title', '').strip()
        if date_str and title:
            CalendarEvent.objects.create(date=date_str, title=title)
            return JsonResponse({'success': True})
        return JsonResponse({'success': False}, status=400)
    all_events = list(CalendarEvent.objects.values('id', 'date', 'title'))
    for e in all_events:
        e['date'] = str(e['date'])
    return JsonResponse({'events': all_events})


def delete_event(request, event_id):
    if request.method == 'POST':
        event = get_object_or_404(CalendarEvent, id=event_id)
        event.delete()
        return JsonResponse({'success': True})
    return JsonResponse({'success': False}, status=405)


def create_list(request):
    if request.method == 'POST':
        name = request.POST.get('listName', '').strip()
        if name:
            ShoppingList.objects.create(name=name)
            return JsonResponse({'success': True})
    return JsonResponse({'success': False}, status=400)


def notes(request):
    if request.method == 'POST':
        text = request.POST.get('text', '').strip()
        if text:
            note = Note.objects.create(text=text)
            return JsonResponse({'success': True, 'id': note.id})
        return JsonResponse({'success': False}, status=400)
    all_notes = list(Note.objects.values('id', 'text'))
    return JsonResponse({'notes': all_notes})


def delete_note(request, note_id):
    if request.method == 'POST':
        get_object_or_404(Note, id=note_id).delete()
        return JsonResponse({'success': True})
    return JsonResponse({'success': False}, status=405)
