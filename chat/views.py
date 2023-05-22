# views.py
from django.shortcuts import render,redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Room, Message, RoomMembership
from django.core.files.storage import FileSystemStorage
from . forms import MessageForm

@login_required
def room(request, pk):
    room = Room.objects.get(id=pk)
    messages = Message.objects.filter(room=room).order_by('timestamp')
    memberships = RoomMembership.objects.filter(room=room)
    context = {
        'room': room,
        'messages': messages,
        'memberships': memberships
    }
    return render(request, 'chat/room.html', context)

@login_required
def message_sent(request,pk):

    room = get_object_or_404(Room, id=pk)
    if request.method == 'POST':
        message_text = request.POST.get('message')
        if message_text:
            message = Message(user=request.user, room=room, message=message_text)
            message.save()
            messages.success(request, 'Your message has been sent.')
            return render(request, 'chat/message.html', {'message':message})
    return render(request, 'chat/room.html')

# def message(request,pk):
#     a1=Room.objects.get(id=pk)
#     mes=Message.objects.filter(room=a1)
#     if request.method=='POST':
#         message=request.POST['message']
#         mm=Message.objects.create(room=a1,user=request.user,content=message)
#         mm.save()

#     return render(request, 'chat/message.html',{'mes':mes,'a1':a1})

def send(request,pk):
    a1=Room.objects.get(id=pk)
    mes=Message.objects.filter(room=a1)
    return render(request, 'chat/input.html',{'mes':mes,'a1':a1})


def getroom(request):
    aa=Room.objects.all()
   
    m=[]
    for i in aa:
      
      if RoomMembership.objects.filter(room=i.id,user=request.user).exists():
          a1=Room.objects.get(id=i.id)
          m.append(a1)
    return render(request, 'chat/room.html', {'room':m})

@login_required
def delete_message(request, pk):
    message = Message.objects.get(id=pk)
    #print(message.user, request.user)
    if message.user == request.user:
        message.delete()
        messages.success(request, 'Message deleted.')
    return render(request,'chat/message.html')

def message(request,pk):
    a1 = Room.objects.get(id=pk)
    mes = Message.objects.filter(room=a1)
    if request.method=="POST":
            content=request.POST['message']
            file=''
            try:
                if request.FILES['file']:
                  file=request.FILES['file']
            except:
             pass

            if content=='' and file=='':
              messages.error(request,'Info nedded here')
            form=Message.objects.create(room=a1,user=request.user,content=content,file=file)
            form.save()
            
    return render(request, 'chat/message.html', {'mes': mes, 'a1': a1})