from django.db import models
from django.contrib.auth.models import User
from django.core.serializers import serialize
# Create your models here.


class pureApiManager(models.QuerySet):
    def serialize(self):
        data = self.all()
        jsonData = serialize("json", data, fields=(
            "Phone", "Address", "State", "Zipcode"))
        return jsonData

    def phoneQuery(self):
        p = self.filter(Phone__icontains=1)
        jsonData = serialize("json", p, fields=(
            "Phone", "Address", "State", "Zipcode"))
        return jsonData
    # or alternate method without using serialize method which will give only the field values instead entire model and pk and fields
    # def phoneQuery(self):
        # listoffieldvalues = list(self.values(
        #     "Phone", "Address", "State"))
        # return json.dumps(listoffieldvalues) {'Phone': 122344, 'Address': '937,Bandhamanicakappa street', 'State': 'TamilNadu'}

    def StateTN(self):
        a = self.filter(State__iexact="TamilNadu")
        jsonData = serialize("json", a, fields=(
            "Phone", "Address", "State", "Zipcode"))
        return jsonData

    def StateKA(self):
        a = self.filter(State__iexact="Karnataka")
        jsonData = serialize("json", a, fields=(
            "Phone", "Address", "State", "Zipcode"))
        return jsonData


class pureApi(models.Model):
    # user = models.ForeignKey(User, on_delete=models.CASCADE)
    Phone = models.IntegerField(blank=True, null=True)
    Address = models.CharField(null=False, max_length=60)
    State = models.CharField(blank=True, null=True, max_length=60)
    Zipcode = models.IntegerField(blank=True, null=True)

    objects = pureApiManager.as_manager()

    def serializeObjInstance(self):
        data = serialize("json", [self], fields=(
            "Phone", "Address", "State", "Zipcode"))  # passing the singeInstance Self as list
        jsonData = data
        # jsonData = {
        #     "Phone": self.Phone,
        #     "Address": self.Address,
        #     "State":  self.State
        # }
        # print(jsonData)
        # print(self.Phone)
        # print(jsonData)
        return jsonData
        # alternate method
        # data=json.loads(data)
        # jsonData=json.dumps(data[0]['fields'])data[0]['fields'] will give the only field values from that
        # list of dictionaries suits for single instance
        # return jsondata

    def __str__(self):
        return str(self.user) + " At " + str(self.Address)

    class Meta:
        verbose_name_plural = "pureApi"
