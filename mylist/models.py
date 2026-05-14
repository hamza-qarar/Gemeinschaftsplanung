from django.db import models
from django.contrib.auth.models import User
from datetime import date

class ShoppingList(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='lists', null=True, blank=True)
    name = models.CharField(max_length=200)
    created_at = models.DateField(default=date.today)

    def __str__(self):
        return self.name

class ShoppingItem(models.Model):
    shopping_list = models.ForeignKey(ShoppingList, on_delete=models.CASCADE, related_name='items', null=True, blank=True)
    created_at = models.DateField(default=date.today)
    name = models.CharField(max_length=200)
    done = models.BooleanField(default=False)

    def __str__(self):
        return str(self.id) + ' ' + self.name


class CalendarEvent(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='events', null=True, blank=True)
    date = models.DateField()
    title = models.CharField(max_length=200)

    class Meta:
        ordering = ['date', 'id']

    def __str__(self):
        return f"{self.date}: {self.title}"


class Note(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='notes', null=True, blank=True)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.text[:50]