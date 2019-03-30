from django.shortcuts import render, redirect, render_to_response
from django.http import HttpResponse, Http404
from .models import Data, Image
from django.views.decorators.csrf import csrf_protect
from django.template import RequestContext

def home(request):
    data = Data.objects.all()
    return render(request, 'home.html', {'data': data})


def image_view(request, pk):
    try:
        datum = Data.objects.get(pk=pk)
    except Data.DoesNotExist:
        raise Http404
    return render(request, 'image_view.html', {'datum': datum})


@csrf_protect
def new_upload(request):

    csrf_context = RequestContext(request)

    if request.method == 'POST' and request.is_ajax():

        print('Inside the POST request')
        title = request.POST.get('title')
        description = request.POST.get('description')
        images = request.FILES.getlist('images[]')

        print(title)
        print(description)
        print(type(images))
        for img in images:
            print(img)

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
        print('hello')
        print(datum.pk)
        return redirect('https://google.com')
    else:
        return render(request, 'new_upload.html')
