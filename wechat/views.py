from django.shortcuts import render

# Create your views here.
import hashlib
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse

WECHAT_TOKEN = "canuxcheng"


@csrf_exempt
def wechat(request):
    # If GET then use token to varify.
    if request.method == "GET":
        signature = request.GET.get("signature", None)
        timestamp = request.GET.get("timestamp", None)
        nonce = request.GET.get("nonce", None)
        echostr = request.GET.get("echostr", None)
        token = WECHAT_TOKEN
        tmp_list = [token, timestamp, nonce]
        tmp_list.sort()
        tmp_str = "%s%s%s" % tuple(tmp_list)
        tmp_str = hashlib.sha1(tmp_str).hexdigest()
        if tmp_str == signature:
            return HttpResponse(echostr, content_type="text/plain")
        else:
            return HttpResponse("Wechat varify failed!")
    # If POST then response something.
    elif request.method == "POST":
        return HttpResponse("Under developing!")
    else:
        return None
