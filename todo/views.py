from django.shortcuts import render, redirect
from .forms import NewTask
from .models import To_Do


# Create your views here.
def home(request):
	to_dos = To_Do.objects.all()
		
	return render(request, "home.html", {"to_dos":to_dos})

#  View to add new task
def add_task(request):
	form = NewTask(request.POST)
	if request.method == "POST":
		if form.is_valid():
			form.save()
		return redirect('home')
	else:
		form = NewTask()			
	return render(request, "add_task.html",  {"form": form})

# Logic to delete task
def delete_task(request, pkey):
	task_to_delete = To_Do.objects.get(id=pkey)
	task_to_delete.delete()
	return redirect('home')