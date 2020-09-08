from django.shortcuts import get_object_or_404, render
from django.utils import timezone
from django.http import HttpResponseRedirect

from .models import Message
from .forms import GreetingForm
# Create your views here.

# Get Messages and Display them
def all(request):
    message_list = Message.objects.order_by('-pub_date')
    context = {'message_list': message_list}
    return render(request, 'message/all.html',context)
    

def index(request):
    if request.method == 'POST':
        form = GreetingForm(request.POST)
        if form.is_valid():
            message_text = request.POST['message_text']
            message = Message(message_text=message_text, pub_date=timezone.now())
            message.save()
            return HttpResponseRedirect('/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = GreetingForm()

    last_message = "" if Message.objects.all().count() <= 0 else Message.objects.order_by('-pub_date')[0]
    context = {'last_message': last_message, 'form': form}
    return render(request, 'message/index.html', context)

def deleteMessage(request, message_id):
    message = get_object_or_404(Message, pk=message_id)
    message.delete()
    return HttpResponseRedirect('/all')