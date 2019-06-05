from django.http import HttpResponse

from .models import Bb

def index(request):
    s = 'Список обьявлений\r\n\r\n\r\n'
    for bb in Bb.objects.order_by('-published'):
        s += bb.title + '\r\n' + bb.content + '\r\n' + str(bb.price) + '\r\n\r\n\r\n'
    return HttpResponse(s, content_type='text/plan; charset=utf-8')
