from django.db import models
from django.contrib.auth.models import User
from item.models import Item

class Conversation(models.Model):
    class Meta:
        managed = True
        verbose_name = 'conversation'
        verbose_name_plural = 'conversations'
        ordering = ('-modified_at',)
        
    
    item = models.ForeignKey(Item, related_name='conversation', on_delete=models.CASCADE)
    members = models.ManyToManyField(User, related_name='conversations')
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

class ConversationMessage(models.Model):
    class Meta:
        managed = True
        verbose_name = 'message'
        verbose_name_plural = 'messages'
        
    
    conversation = models.ForeignKey(Conversation, related_name='messages', on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User, related_name='created_messages', on_delete=models.CASCADE, default=None)
    
    
