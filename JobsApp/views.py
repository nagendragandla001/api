from django.shortcuts import render

from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse

from JobsApp.models import Jobs

from JobsApp.serializers import JobSerializer

# Create your views here.
@csrf_exempt
def jobApi(request, id=0):
    if request.method=='GET':
        jobs = Jobs.objects.all()
        jobs_serializer = JobSerializer(jobs, many=True)
        return JsonResponse(jobs_serializer.data, safe=False)

    elif request.method=='POST':
        job_data=JSONParser().parse(request)
        job_serializer = JobSerializer(data=job_data)
        if job_serializer.is_valid():
            job_serializer.save()
            return JsonResponse("Added Successfully!!!!", safe=False)
        return JsonResponse("Failed to Add.", safe=False)

    elif request.method=='PUT':
        job_data = JSONParser().parse(request)
        job = Jobs.objects.get(id=job_data['id'])
        job_serializer = JobSerializer(job,data=job_data)
        if job_serializer.is_valid():
            job_serializer.save()
            return JsonResponse("Updated Successfully!!", safe=False)
        return JsonResponse("Failed to update.", safe=False)
    
    elif request.method=='DELETE':
        job = Jobs.objects.get(id=id)
        job.delete()
        return JsonResponse("Deleted Successfully!!", safe=False)