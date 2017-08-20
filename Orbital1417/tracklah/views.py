from django.shortcuts import render
from django.http import HttpResponse
from tracklah.models import *
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.core import serializers
import simplejson
import json





def index(request):


    charityProjSubAllData_list= serializers.serialize("json",CharityProjSub.objects.all())
    userInput=False;
    query = request.GET.get('q')

    #if there is input from user, send query object and all object
    if query :
        userInput=1;
        print(query)
        resultChocoCodeProj = ChocoCode.objects.get(donationCode = query) #aacount for invalid entry
        print(resultChocoCodeProj)
        displayProj = CharityProjSub.objects.get(projectNameSub = resultChocoCodeProj.projectNameSub)
        print(displayProj.projectNameSub)

        queryMarkerSubData = serializers.serialize("json", CharityProjSub.objects.filter(projectNameSub = resultChocoCodeProj.projectNameSub))

        args = {'queryMarkerSubData':queryMarkerSubData,
                'displayProj' :displayProj,
                'charityProjSubAllData_list':charityProjSubAllData_list
                ,'userInput':userInput }

    else:
        #args= {'charityProjSubAllData_list': charityProjSubAllData_list, 'userInput':userInput}

        args = {'queryMarkerSubData': {},
                'displayProj' :{},
                'charityProjSubAllData_list':charityProjSubAllData_list
                ,'userInput':userInput, }


    print('view no problem!')
    return render(request, 'trackhome.html', args)


    #googlemap data

    #CharityProjects_list= serializers.serialize("json",CharityProjects.objects.all())
    #allCharPost_list = serializers.serialize("json",CharPost.objects.all())

    #charityProjSubAllData_list= serializers.serialize("json",CharityProjSub.objects.all())
    #mapData= {"charityProjSubAllData_list":charityProjSubAllData_list}


    '''
    if query!= None:
        return render(request, 'trackhome.html', context= {'displayProj' :displayProj ,
                        "charityProjSubAllData_list": charityProjSubAllData_list,})
                        '''
