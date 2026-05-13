from django.db import migrations


def assign_items(apps, schema_editor):
    ShoppingList = apps.get_model('mylist', 'ShoppingList')
    ShoppingItem = apps.get_model('mylist', 'ShoppingItem')
    erl = ShoppingList.objects.create(name='Erledigungen')
    bes = ShoppingList.objects.create(name='Besorgungen')
    ShoppingItem.objects.filter(list_type='erledigungen').update(shopping_list=erl)
    ShoppingItem.objects.filter(list_type='besorgungen').update(shopping_list=bes)


class Migration(migrations.Migration):

    dependencies = [
        ('mylist', '0003_shoppinglist_alter_shoppingitem_list_type_and_more'),
    ]

    operations = [
        migrations.RunPython(assign_items),
    ]
