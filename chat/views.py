from django.shortcuts import render
from django.contrib.auth.decorators import login_required
import json
from django.http import HttpResponse
from chat.utils import find_or_create_private_chat
from User.models import *
from django.conf import settings

# Create your views here.
DEBUG = False
@login_required(login_url='login')
def home(request):

	context = {
		'debug':DEBUG,
		'debug_mode':settings.DEBUG,
	}
	return render(request,'chat/home.html',context)


# Ajax call to return a private chatroom or create one if does not exist
def create_or_return_private_chat(request, *args, **kwargs):
	print("got a call *************************")
	user1 = request.user
	payload = {}
	if user1.is_authenticated:
		if request.method == "POST":
			chat_room = request.POST.get("order_id")
			try:
				payload['chatroom_id'] = chat_room
				payload['response'] = "Successfully got the chat."

			except:
				payload['response'] = "Unable to start a chat with that user."
	else:
		payload['response'] = "You can't start a chat if you are not authenticated."

	return HttpResponse(json.dumps(payload), content_type="application/json")