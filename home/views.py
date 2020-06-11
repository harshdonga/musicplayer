from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.core.files.storage import FileSystemStorage
import json
import os
import random

def updatelist(name, link):
    with open('names.txt') as f:
        data = json.load(f)
        data['songs'].append({
            'name': name,
            'link': link
        })
    with open('names.txt', 'w') as f:
        json.dump(data, f, indent=4)


def index(request):
    with open ('names.txt') as f:
        data = json.load(f)
    names = list(reversed([x['name'] for x in data['songs']]))
    links = list(reversed([x['link'] for x in data['songs']]))
    artworks = ['_1', '_2','_3','_4','_5']
    random.shuffle(artworks)
    data = {}
    data['names'] = names
    data['links'] = links
    data['artworks'] = artworks
    print(data)
    return render(request, 'home/musicplayer.html',{'data':data} )


def upload(request):
    return render(request, 'home/upload.html')


def post(request):
    if request.method == 'POST':
        uploaded_song = request.FILES['song']   
        fs = FileSystemStorage()
        f = fs.save(uploaded_song.name, uploaded_song)
        link = '/media/'+ uploaded_song.name
        updatelist(uploaded_song.name, link)
        return redirect('/')