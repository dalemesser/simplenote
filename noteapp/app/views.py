from django.shortcuts import render,redirect,reverse
from . forms import TodoForm
from . models import Todo

def index(request):
    item_list = Todo.objects.order_by("date")
    form = TodoForm(request.POST)
    if form.is_valid():
        form.save()
        return redirect(reverse("index"))

    contex = {
        "items": item_list,
        "form" : form
    }
    return render (request,"app/todo.html",contex)

def delete(request,id):
    obj = Todo.objects.get(id = id)
    obj.delete()
    return redirect(reverse("index"))
