from django.shortcuts import render
from .models import pureApi
from django.http import JsonResponse, HttpResponse
from django.views import View
from django.core.serializers import serialize
import json
# Create your views here.

# Normal JsonResponse


class jsonRes(View):
    def get(self, request, *args, **kwargs):
        Data = pureApi.objects.all()[0]
        jsonData = {
            "Phone": Data.Phone,
            "Address": Data.Address,
            "State": Data.State
        }  # the only problem is we cannot format the jsonresponse everytime so we can use serialize method for queryset and object
        return JsonResponse(jsonData)


class serilazedobj(View):
    def get(self, request, *args, **kwargs):
        # It is an single Instance of model object not a queryset
        obj = pureApi.objects.get(State="TamilNadu")
        # print(obj)
        json_data = serialize('json', [obj], fields=(
            "Phone", "Address", "State", "Zipcode"))
        # for the single object(Instance) we need to pass into list But which return list of dictionaries JsonResponse
        #  wont rener that it can render only dict objs
        # but we can manipulate that using python json mehtods
        loading = json.loads(json_data)
        # returns same as json datatype but in python dict
        print(loading[0]["fields"])
        # to change to datatype json need to used json.dumps
        json_data_dump = json.dumps(loading[0]["fields"])
        json_data = json_data_dump
        # which is same as JsonResponse
        return HttpResponse(json_data, content_type="application/json")
        # return JsonResponse(json_data)


class serilazedLisrobj(View):
    def get(self, request, *args, **kwargs):
        final_list = []
        obj = pureApi.objects.filter(State="Karnataka")  # returns queryset
        # print(obj)
        # obj = pureApi.objects.all()
        json_data = serialize('json', obj, fields=(  # [{"model": "pureDjangoApi.pureapi", "pk": 2, "fields": {"Phone": 123568875, "Address": "Harija Nagar", "State": "Karnataka", "Zipcode": 789098}}]
            "Phone", "Address", "State", "Zipcode"))

        # for list of objects (queryset) that simple need to pass that queryset is enough to serialize

        # This is themethod for returning only fields in the list of dictionaries notgong to use serialize
        # instead single model instance method with iterating single instance in for loop querysets
        # here obj is queryset and onj1 in each iteration is single instance of model
        # for best definition check class bestqueryset below

        for obj1 in obj:  # obj1 will become an single instance so we can use model method to serialzie and add to the list
            dump = obj1.serializeObjInstance()
            final_list.append(dump)
        json_data = final_list  # will remove model pk key and values from Serialized list
        # {'Phone': 123568875, 'Address': 'Harija Nagar', 'State': 'Karnataka'}
        return HttpResponse(json_data, content_type="application/json")


class serilazedLisrobjLimit(View):
    def get(self, request, *args, **kwargs):
        # line no 45-48 can be ruled out with modelQuerysets in CustomManagers
        # here StateKA() is custom queryset which return serialized objects from the mangers alone
        # objects is a custom model manager
        json_data = pureApi.objects.StateKA()
        return HttpResponse(json_data, content_type="application/json")


class serilazedobjLimit(View):
    def get(self, request, *args, **kwargs):
        # it is an instance we can create model method to handle instances
        json_data = pureApi.objects.get(State="TamilNadu")
        # line no 28 can be change like this due to the single instance
        json_data = json_data.serializeObjInstance()
        loading = json.loads(json_data)
        # returns same as json datatype but in python dict
        print(loading[0]["fields"])
        # to change to datatype json need to used json.dumps
        json_data_dump = json.dumps(loading[0]["fields"])
        json_data = json_data_dump
        # which is same as JsonResponse
        return HttpResponse(json_data, content_type="application/json")
        # return JsonResponse(json_data)


# this method is best one because need not to use serialize method alone to get the json response
# without custom queryset and withput serialize object
class bestJsonQueryset(View):
    def get(self, request, *args, **kwargs):
        json_data = []
        qs = pureApi.objects.all()
        for singleInstance in qs:
            json_data.append(singleInstance.serializeObjInstance())
        return HttpResponse(json_data, content_type="application/json")
        # returns {'Phone': 122344, 'Address': '937,Bandhamanicakappa street', 'State': 'TamilNadu'}{'Phone': 123568875, 'Address': 'Harija Nagar', 'State': 'Karnataka'}


class restdetailview(View):
    def get(self, request, id, *args, **kwargs):
        obj = pureApi.objects.get(id=id)
        print(obj)
        json_data = obj.serializeObjInstance()
        # print(list(json_data))
        print(json_data)
        return HttpResponse([json_data], content_type="application/json")
