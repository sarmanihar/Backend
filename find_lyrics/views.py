
from django.shortcuts import render
from .models import  profile
from django.http import HttpResponse
from django.shortcuts import render, redirect

from django.http import HttpResponse, JsonResponse


def create(request):
    if request.method=='POST':
       song_name=request.POST['song_name']
       artist_name=request.POST['artist_name']
       new_profile=profile(song_name=song_name,artist_name=artist_name)
       new_profile.save()
       success='Song '+song_name+' by '+artist_name+' has been liked.'
       return HttpResponse(success)

def home1(request):
    queryset=profile.objects.all()
    #queryset=profile.objects.all()
    #queryset=profile.objects.get(id=6)
    context={
    'object_list':queryset,
    }
    return render(request, 'home1.html',context) 

#def like(request):
    #queryset=profile.objects.all()
    #queryset=profile.objects.get(id=6)
    #context={
    #'object_list':queryset
    #}
    #return render(request,'home1.html',context)       