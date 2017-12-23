from django.http import HttpResponse
from .settings import CONFIG
import hashlib
# Create your views here.

def main(request):
    return checkSigurature(request)


def checkSigurature(request):
    signature = request.GET.get('signature')
    timestamp = request.GET.get('timestamp')
    nonce = request.GET.get('nonce')

    arr = [CONFIG['WeChat']['token'], timestamp, nonce]
    sorted_arr = sorted(arr)
    sorted_str = ''.join(sorted_arr).encode('utf-8')
    sha1_val = hashlib.sha1(sorted_str).hexdigest()
    result = request.GET.get('echostr')
    if sha1_val != signature :
        result = 'error'
    return HttpResponse(result)


