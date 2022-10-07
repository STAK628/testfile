import json
from django.http.response import JsonResponse
from django.views.decorators.csrf import ensure_csrf_cookie, csrf_exempt
from django.shortcuts import render, redirect
from django.http import HttpResponse

# Create your views here.
# @ensure_csrf_cookie
@csrf_exempt
def index(request):
    if request.method == 'GET':

        res ={"Low": "TypeA", "Middle": "TypeC", "High": "TypeB", "BestFit": "Low", "var1": "- vol.", "var2": "Best Fit", "var3": "+ vol."}

        return JsonResponse(res)

    elif request.method == 'POST':
        # JSON
        datas = json.loads(request.body)
        print(datas['userPreference'] + " is your preference")

    # # JSONに変換して戻す
        return JsonResponse(datas)

