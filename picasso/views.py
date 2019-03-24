from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404
from .models import Data, Image

def home(request):
    data = Data.objects.all()
    return render(request, 'home.html', {'data': data})


def image_view(request, pk):
    try:
        datum = Data.objects.get(pk=pk)
    except Data.DoesNotExist:
        raise Http404
    return render(request, 'image_view.html', {'datum': datum})


def new_upload(request):
    if request.method == 'POST':
        title = request.POST['title']
        description = request.POST['description']
        images = request.FILES.getlist('images')

        datum = Data.objects.create(
            title=title,
            description=description,
            image_flagship=images[0]
        )

        for image in images:
            Image.objects.create(
                image=image,
                data=datum
            )

        return redirect('image_view', pk=datum.pk)

    return render(request, 'new_upload.html', )
