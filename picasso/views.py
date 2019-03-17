from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404
from .models import MetaData, Image

def home(request):
    datas = MetaData.objects.all()
    return render(request, 'home.html', {'datas': datas})


def image_view(request, pk):
    try:
        data = MetaData.objects.get(pk=pk)
    except MetaData.DoesNotExist:
        raise Http404
    return render(request, 'image_view.html', {'data': data})


def new_upload(request):
    if request.method == 'POST':
        title = request.POST['title']
        description = request.POST['description']
        images = request.FILES.getlist('images')

        data = MetaData.objects.create(
            title=title,
            description=description
        )

        for image in images:
            Image.objects.create(
                image=image,
                metadata=data
            )

        return redirect('image_view', pk=data.pk)

    return render(request, 'new_upload.html', )
