from asgiref.sync import async_to_sync
from channels.layers import get_channel_layer
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import json


@csrf_exempt
def send_message(request):
    channel_layer = get_channel_layer()
    message = request.POST.get('message')
    async_to_sync(channel_layer.group_send)(
            'chat_varzesshi',
            {
                'type': 'chat_message',
                'message': message
            }
        )


    return HttpResponse('Message sent')
