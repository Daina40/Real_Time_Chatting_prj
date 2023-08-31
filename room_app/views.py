from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .models import Room, Message
from django.shortcuts import redirect
from django.http import HttpResponse, JsonResponse
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync

@login_required
def rooms(request):
    rooms = Room.objects.all()

    context = {
        'rooms': rooms,
    }

    return render(request, 'room/rooms.html', context)

@login_required

def room(request, room):
    username = request.GET.get('username')
    room_details = Room.objects.get(name=room)
    
    context = {
        'username': username,
        'room': room,
        'room_details': room_details,
        
    }

    return render(request, 'room/room.html', context)

@login_required

def checkview(request):
    room = request.POST['room_name']
    username = request.POST['username']
    
    if Room.objects.filter(name=room).exists():
        return redirect(f'{room}/?username={username}')
    else:
        new_room = Room.objects.create(name=room, username=username)
        new_room.save()
        return redirect(f'{room}/?username={username}')



@login_required

def send(request):
    message = request.POST['message']
    username = request.GET.get('username')
    room_id = request.POST['room_id']

    channel_layer = get_channel_layer()
    print("Sending message:", message)
    async_to_sync(channel_layer.group_send)(
        f'chat_{room_id}',
        {
            'type': 'chat.message',
            'message': message,
            'username': username,
        }
    )

    return HttpResponse("Message sent successfully via WebSocket.")



@login_required

def getMessages(request,  room):
    room_details = Room.objects.get(name=room)
    messages = Message.objects.filter(room=room_details.id)
    return JsonResponse({"messages": list(messages.values())})



























# ####   comment   ####
# def send(request):
#     message = request.POST['send_msg']
#     print(message)
#     new_message = Message.objects.create(value=message)
#     new_message.save()
#     context = {
#         'message' : message
#     }
#     # return JsonResponse({"messages": list(messages.values())})
#     return render(request, 'room/message.html', context)
#     # return HttpResponse("Hi, Message Sent Successfully!!")

# def getMessages(request,  room):
#     room_details = Room.objects.get(name=room)
#     messages = Message.objects.filter(room=room_details.name)
#     print('message= ', messages)

#     context = {
#         'messages' : messages
#     }
#     # return JsonResponse({"messages": list(messages.values())})
#     return render(request, 'room/message.html', context)