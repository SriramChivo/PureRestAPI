from django.http import HttpResponse
from django.views import View
from pureDjangoApi.models import pureApi
import json
from django.core.serializers import serialize
from pureDjangoApi.forms import ApiForm
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator


class csrfMixin(object):
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)


class ListApiView(csrfMixin, View):
    def get(self, request, *args, **kwargs):
        print("is empty???")
        print(request.body)
        convertoJson = json.loads(request.body)
        print(convertoJson)
        id = convertoJson.get("id", None)
        print(id)
        if id is not None:
            print("Having ID")
            getObj = pureApi.objects.get(id=id)
            getObj = serialize('json', [getObj])
        else:
            print("Not Having ID")
            getObj = pureApi.objects.serialize()
            print(getObj)
        # json_data = {"hello": "World"}
        return HttpResponse(getObj, content_type="application/json")

    def post(self, request, *args, **kwargs):
        print(request.POST)
        print("---------------")
        print(request.body)
        l = json.loads(request.body)
        form = ApiForm(l)
        if form.is_valid():
            print("Inside Valid")
            form = form.save(commit=False)
            form.user = request.user
            form.save()
            # print(form)
            getObj = serialize('json', [form])
        else:
            print("Inside Not Valid")
            form = form.errors
            getObj = json.dumps(form)
        return HttpResponse(getObj, content_type="application/json")

    def put(self, request, *args, **kwargs):
        convertoJson = json.loads(request.body)
        id = convertoJson.get("id", None)
        if id is not None:
            print("Having ID")
            getObj = pureApi.objects.get(id=id)
            getObj = serialize('json', [getObj])
            getObj = json.loads(getObj)
            print(getObj)
            print(type(getObj))
            getObj = getObj[0]['fields']
            print(getObj)
            getObj = json.dumps(getObj)
            jsonobj = json.loads(getObj)
            print(jsonobj)
            for keys, values in convertoJson.items():
                jsonobj[keys] = values
            print(jsonobj)
            getObj = json.dumps(jsonobj)
        else:
            print("Not Having ID")
        return HttpResponse(getObj, content_type="application/json")
