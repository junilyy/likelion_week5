from django.shortcuts import render, get_object_or_404,redirect
from .models import person
from django.utils import timezone
from .forms import PersonForm
# Create your views here.

def home(request):
    firstapps = person.objects.all()
    cnt=0
    for i in range(len(firstapps)):
        cnt+=1
    return render(request, 'home.html',{"firstapps":firstapps, "cnt":cnt})

def detail(request,id):
    per=get_object_or_404(person,pk=id)
    if per.elite==False:
        el='N'
    else:
        el='Y'
    return render(request,"detail.html",{'per':per, 'el':el})

def new(request):
    form = PersonForm()
    return render(request, "new.html",{'form':form})

def create(request):
    new_blog=person()
    new_blog.name=request.POST['name']
    new_blog.event=request.POST['event']
    new_blog.position=request.POST['position']
    new_blog.intro=request.POST['intro']
    
    if len(request.POST.getlist('elite')) ==0:
        important = False
    else:
        important = True
    new_blog.elite=important
    new_blog.live=request.POST['live']
    new_blog.birth=timezone.now()
    new_blog.age=request.POST['age']
    new_blog.save()
    return redirect('detail',new_blog.id)

def edit(request,id):
    edit_person = person.objects.get(id=id)
    return render(request,'edit.html',{'person':edit_person})

def update(request, id):
    update_person = person.objects.get(id=id)
    update_person.name=request.POST['name']
    update_person.event=request.POST['event']
    update_person.position=request.POST['position']
    update_person.intro=request.POST['intro']
    
    if len(request.POST.getlist('elite')) ==0:
        important = False
    else:
        important = True
    update_person.elite=important
    update_person.live=request.POST['live']
    update_person.birth=timezone.now()
    update_person.age=request.POST['age']
    update_person.save()
    return redirect('detail',update_person.id)

def delete(request,id):
    delete_person=person.objects.get(id=id)
    delete_person.delete()
    return redirect('home')

