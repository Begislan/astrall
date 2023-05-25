from django.shortcuts import render
from .models import Photo
from django.views.generic.edit import CreateView


photo = Photo.objects.all()

def core(request):
    context = {
        'photo': photo
    }
    return render(request, 'astrall/index.html', context)


class CreatePhotoView(CreateView):
    model = Photo
    template_name = 'astrall/create.html'
    fields = ['file']
    
