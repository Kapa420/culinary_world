from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect

from item.models import Item

from .forms import ConversationMessageForm
from .models import Conversation

@login_required
def new_conversation(request, item_id):
    item = get_object_or_404(Item, id=item_id)

    if item.created_by == request.user:
        return redirect('dashboard:index')
    
    conversations = Conversation.objects.filter(item=item).filter(members__in=[request.user.id])

    if conversations:
        return redirect('conversation:detail', message_id=conversations.first().id)

    if request.method == 'POST':
        form = ConversationMessageForm(request.POST)

        if form.is_valid():
            conversation = Conversation.objects.create(item=item)
            conversation.members.add(request.user)
            conversation.members.add(item.created_by)
            conversation.save()

            conversation_message = form.save(commit=False)
            conversation_message.conversation = conversation
            conversation_message.created_by = request.user
            conversation_message.save()

            return redirect('item:detail', item_id=item_id)
    else:
        form = ConversationMessageForm()
    
    return render(request, 'conversation/new.html', {
        'form': form
    })

@login_required
def inbox(request):
    conversations = Conversation.objects.filter(members__in=[request.user.id])
    
    return render(request, 'conversation/inbox.html', {
        'conversations': conversations,
        'title': 'Inbox',
    })
    
@login_required
def detail(request, message_id):
    conversation = Conversation.objects.filter(members__in=[request.user.id]).get(id=message_id)
    
    if request.method == 'POST':
        form = ConversationMessageForm(request.POST)
        
        if form.is_valid():
            conversation_message = form.save(commit=False)
            conversation_message.conversation = conversation
            conversation_message.created_by = request.user
            conversation_message.save()
            
            conversation.save()
            
            return redirect('conversation:detail', message_id=message_id)
        
    else:
        form = ConversationMessageForm()
    
    return render(request, 'conversation/detail.html', {
        'conversation': conversation,
        'title': 'Detail',
        'form': form,
    })
     