from django.shortcuts import render, get_object_or_404,redirect
from .models import Messages
from .forms import MessageForm
from django.utils import timezone

# Create your views here.
def display(request):
    messages=reversed(Messages.objects.order_by('created_date'))
    return render(request, 'mychatapp/main.html', {'messages': messages})

def update(request):
    if request.method == "POST":
        form = MessageForm(request.POST)
        print (form)
        if form.is_valid():
            message = form.save(commit=False)
            message.created_date = timezone.now()
            message.save()
            return redirect('display')
    else:
        form = MessageForm()
        return render(request, 'mychatapp/update.html', {'form': form})
