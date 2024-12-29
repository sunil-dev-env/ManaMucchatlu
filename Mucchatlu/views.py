from django.shortcuts import render, redirect, get_object_or_404
from .models import Thread, Message

def home(request):
    search_query = request.GET.get('search', '')
    threads = Thread.objects.filter(title__icontains=search_query) if search_query else Thread.objects.all()
    return render(request, 'home.html', {'threads': threads})

def thread_detail(request, thread_id):
    thread = get_object_or_404(Thread, pk=thread_id)
    messages = thread.messages.filter(parent=None)
    if request.method == 'POST':
        content = request.POST['content']
        parent_id = request.POST.get('parent_id')
        parent_message = Message.objects.get(pk=parent_id) if parent_id else None
        nickname = request.COOKIES.get('nickname')
        Message.objects.create(thread=thread, nickname=nickname, content=content, parent=parent_message)
        return redirect('thread_detail', thread_id=thread.id)
    return render(request, 'thread_detail.html', {'thread': thread, 'messages': messages})


def create_thread(request):
    if request.method == 'POST':
        title = request.POST['title']
        Thread.objects.create(title=title)
        return redirect('home')
    return render(request, 'create_thread.html')

def set_nickname(request):
    if request.method == 'POST':
        nickname = request.POST.get('nickname')
        response = redirect('home')
        response.set_cookie('nickname', nickname, max_age=60*60*24*7)  # Cookie lasts for 7 days
        return response
    return render(request, 'set_nickname.html')

