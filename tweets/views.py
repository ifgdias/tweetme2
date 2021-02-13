from django.shortcuts import render
from django.http import HttpResponse, Http404, JsonResponse

from .models import Tweet

# Create your views here.


def home_view(requests, *args, **kwargs):
    print(args, kwargs)
    return HttpResponse("<h1>Hello World</h1>")


def tweet_detai_view(requests, tweet_id, *args, **kwargs):

    data = {
        "id": tweet_id,
        # "image_path" : obj.image.url
    }
    status = 200

    try:
        obj = Tweet.objects.get(id=tweet_id)
        data['content'] = obj.content
    except:
        data['message'] = 'Not Found'
        status = 404

    return JsonResponse(data, status=status)
