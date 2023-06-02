from django.shortcuts import render, redirect
from .forms import *
from django.http import *
from dashboard.models import users
# Create your views here.
def chatPage(req):
    form = MessageForm
    context = {
        "messageForm": form,
        "data": model_to_dict(ChatMessage.objects.all())
    }
    return render(req, "chat/aje.html", context)

from rest_framework.views import APIView
from rest_framework.response import Response
# from .serializers import MyModelSerializer
from .models import *
from django.views.decorators.csrf import csrf_exempt


def chat(req):
    chats = ChatMessage.objects.all()
    context = {
        "chats": chats,
        "form": MessageForm()
    }
    return render(req, 'chat/aj.html', context)
def getMessage(req):
    room_details= ChatMessage.objects.all()
    messages= ChatMessage.objects.all()
    return JsonResponse({'messages': list(messages.values())})
def gmessages(request,pk):
    
    if request.method=="POST":
        form = MessageForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
    user= users.objects.get(email=pk)
    
    context= {
        "userEmail": pk,
        "user": user,
        "group": f"{user.student_department.department} - {user.batch} year",
        "chats": ChatMessage.objects.all()
    }
    return render(request, 'chat/responsive.html', context)


@csrf_exempt
def send_message(request):
    if request.method == 'POST':
        username = 'Anonymous'
        content = request.POST['message']
        timestamp = datetime.now()
        message = ChatMessage(username=username, content=content, timestamp=timestamp)
        message.save()
        return JsonResponse({'success': True})
    else:
        return JsonResponse({'success': False})
from .serializers import ChatMessageSerializer

def getMessgageAPI(req,pk):
    user= users.objects.get(email=pk)
    # a = ChatMessage.objects.filter(dept=user.student_department.department,batch= user.batch )
    print(user.student_department.department)
    a= ChatMessage.objects.all()
    ser= ChatMessageSerializer(a, many= True)

    return Response(ser.data)

class GetMessages(APIView):
    def get(self,req,pk,*args,**kwargs):
        a= ChatMessage.objects.all()
        ser= ChatMessageSerializer(a, many= True)

        return Response(ser.data)


def postMessage(req):
    if req.method=="POST":
        form = MessageForm(req.POST)
        if form.is_valid():
            form.save()
            return redirect("getMessage")




# import asyncio
# import websockets

# async def chat_server(websocket, path):
#     async for message in websocket:
#         # Handle incoming message
#         print(f"Received message: {message}")
        
#         # Forward message to other connected clients
#         for client in clients:
#             if client != websocket:
#                 await client.send(message)

# async def start_chat_server():
#     async with websockets.serve(chat_server, "localhost", 8000):
#         print("Chat server started!")
#         await asyncio.Future()  # Keep the server running indefinitely

# # Start the chat server
# asyncio.run(start_chat_server())