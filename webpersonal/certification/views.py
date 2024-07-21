from django.shortcuts import render
from.models import Project

# Create your views here.
def certification(request):
    projects = Project.objects.all()
    return render(request, "certification/certification.html", {'projects': projects})