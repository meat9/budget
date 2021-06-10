from django.shortcuts import render

# Create your views here.
from .models import Budget, GlavBudgetClass
from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework import permissions
from .serializer import BudgetSerializer, GlavBudgetSerializer
from rest_framework.response import Response
from rest_framework.decorators import action, api_view
import requests
from rest_framework import status
from django.http import HttpResponse


class BudgetViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Budget.objects.all().order_by('code')
    serializer_class = BudgetSerializer
    permission_classes = [permissions.AllowAny]
    
    @action(detail=False, permission_classes=[permissions.AllowAny], methods=['POST','PATCH', 'GET'])
    def me(self, request, *args, **kwargs):
        pageSize = str(request.POST.get('pageSize'))
        if pageSize == None and pageSize == '':
            pageSize = str(1000)
        url_level_first = 'http://budget.gov.ru/epbs/registry/7710568760-BUDGETS/data?filterbudglevelcode=1&filterstatus=ACTIVE'
        data_level_first = requests.get(url=url_level_first)
        if data_level_first.status_code == 200 and request.method == 'POST':
            data = data_level_first.json()
            for i in data["data"]:
                if i["enddate"] == '':
                    i["enddate"] = None
                    try:
                        Budget.objects.update_or_create(defaults={
                            "startdate": i["startdate"],
                            "enddate": i["enddate"],
                            "status": i["status"],
                            "budgettype": i["budgtypecode"],
                            },
                            code = i["code"],name = i["name"])
                        obj = Budget.objects.filter(code = i["code"]).first()
                        GlavBudgetClass.objects.update_or_create(defaults={
                            "startdate": i["startdate"],
                            "enddate": i["enddate"],
                            "budget": obj,
                            },
                            code = i["code"],name = i["name"])
                    except:
                        pass
            for i in range(2, 4):
                url_start = 'http://budget.gov.ru/epbs/registry/7710568760-BUDGETS/data?filterbudglevelcode='+str(i)+'&pageSize='+pageSize+'&filterstatus=ACTIVE&pageNum=1'
                data_start = requests.get(url=url_start)
                data = data_start.json()
                #print(data["pageCount"])
                for x in range (2, data["pageCount"]):
                    url_level_another = 'http://budget.gov.ru/epbs/registry/7710568760-BUDGETS/data?filterbudglevelcode='+str(i)+'&pageSize='+pageSize+'&filterstatus=ACTIVE&pageNum='+str(x)
                    data_level_another = requests.get(url=url_level_another)
                    if data_level_another.status_code == 200 and request.method == 'POST':
                        data = data_level_another.json()
                        for i in data["data"]:
                            x = i["parentcode"]
                            level_up=Budget.objects.filter(code = x).first()
                            if i["enddate"] == '':
                                i["enddate"] = None
                            try:
                                Budget.objects.update_or_create(defaults={
                                    "parentcode": level_up,
                                    "startdate": i["startdate"],
                                    "enddate": i["enddate"],
                                    "status": i["status"],
                                    "budgettype": i["budgtypecode"],
                                    },
                                    code = i["code"],name = i["name"])
                                obj = Budget.objects.filter(code = i["code"]).first()
                                GlavBudgetClass.objects.update_or_create(defaults={
                                    "startdate": i["startdate"],
                                    "enddate": i["enddate"],
                                    "budget": obj,
                                    },
                                    code = i["code"],name = i["name"])
                            except:
                                pass
                    return HttpResponse('Upgrade DB is successful')



class GlavBudgetViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = GlavBudgetClass.objects.all()
    serializer_class = GlavBudgetSerializer
    permission_classes = [permissions.AllowAny]