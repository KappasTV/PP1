from django.shortcuts import render
from django.http import Http404, HttpResponseRedirect, HttpResponseBadRequest
from django.urls import reverse

from .models import Family, Perevod

def index(request):
    family_info = Family.objects.all()
    return render(request, 'family/list.html', {'family_info': family_info})

def detail(request,family_id):
    try:
        a = Family.objects.get(id = family_id)
    except:
        raise Http404("Family doesn`t exist :(")

    latest_perevod_list = a.perevod_set.order_by('-id')[:3] 


    return render(request, 'family/detail.html', {'family': a, 'latest_perevod_list': latest_perevod_list})



def make_transaction(request,family_id):
    try:
        a = Family.objects.get(id = family_id)
    except:
        raise Http404("Family doesn`t exist, Sir :(")
    check = int(request.POST['text'])



    a.perevod_set.create(user_name = request.POST['name'],user_perevod = request.POST['text'])
    emount = int(request.POST['text'])
    if request.POST['name'] == a.family_name and request.POST['receiver'] == a.father_name:
        if a.family_budget < emount:
            return
        a.father_budget += emount
        a.family_budget -= emount
        a.save()
    elif request.POST['name'] == a.father_name and request.POST['receiver'] == a.family_name:
        if a.father_budget < emount:
            return
        a.family_budget += emount
        a.father_budget -= emount
        a.save()

    if request.POST['name'] == a.family_name and request.POST['receiver'] == a.mother_name:
        if a.family_budget < emount:
            return
        a.mother_budget += emount
        a.family_budget -= emount
        a.save()
    elif request.POST['name'] == a.mother_name and request.POST['receiver'] == a.family_name:
        if a.mother_budget < emount:
            return
        a.family_budget += emount
        a.mother_budget -= emount
        a.save()    

    if request.POST['name'] == a.family_name and request.POST['receiver'] == a.child_name:
        if a.family_budget <  emount:
            return
        a.child_budget += emount
        a.family_budget -= emount
        a.save() 
    elif request.POST['name'] == a.child_name and request.POST['receiver'] == a.family_name:
        if a.child_budget < emount:
            return
        a.family_budget += emount
        a.child_budget -= emount
        a.save()
       
    #a.family_budget += emount
    #a.save()

    return HttpResponseRedirect(reverse('family:detail', args=(a.id,)))
