from django.shortcuts import render
from django.http import JsonResponse
from .models import Client, Artist, Work
from .forms import UserRegistrationForm
from django.views.decorators.csrf import csrf_exempt


# Create your views here.
@csrf_exempt
def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            return JsonResponse({'status': 'ok', 'message': 'User created'})
        else:
            errors = form.errors.as_json()
            return JsonResponse({'status': 'error', 'message': errors})
    else:
        return JsonResponse({'status': 'error', 'message': 'Invalid request'})


def works(request):
    if (request.method == 'GET'):
        works = Work.objects.all()
        artist = request.GET.get('artist')
        work_type = request.GET.get('work_type')
        if artist:
            artists = Artist.objects.filter(name=artist)
            data = [{'name': artist.name, 'work': [{'link': work.link, 'work_type': work.work_type}
                                                   for work in artist.work.all()]} for artist in artists]
            return JsonResponse({'status': 'ok', 'data': data})
        if work_type:
            works = works.filter(work_type=work_type)
            data = [{'link': work.link, 'work_type': work.work_type}
                    for work in works]
            return JsonResponse({'status': 'ok', 'data': data})
        data = [{'link': work.link, 'work_type': work.work_type} for work in works]

        return JsonResponse({'status': 'ok', 'data': data})
    else:
        return JsonResponse({'status': 'error', 'message': 'Invalid request'})

def insert_sample_data(request):
    if request.method == 'GET':
        # Create sample data for 10 works
        works=[]
        for i in range(1, 11):
            work = Work.objects.create(
                link=f'https://www.youtube.com/watch?v=0{i}',
                work_type=Work.YOUTUBE
            )
            works.append(work)
        for i in range(11, 21):
            work = Work.objects.create(
                link=f'https://www.instagram.com/p/0{i}',
                work_type=Work.INSTAGRAM
            )
            works.append(work)
        for i in range(21, 31):
            work = Work.objects.create(
                link=f'https://www.example.com/0{i}',
                work_type=Work.OTHER
            )
            works.append(work)
        # Create sample data for 10 artists
        artists=[]
        for i in range(1, 11):
            artist = Artist.objects.create(
                name=f'Artist {i}'
            )
            artists.append(artist)
        # Assign works to artists
        for i in range(0, 10):
            artists[i].work.set(works[i*3:i*3+3])
        return JsonResponse({'status': 'ok', 'message': 'Sample data inserted'})

    else:
        return JsonResponse({'status': 'error', 'message': 'Invalid request'})