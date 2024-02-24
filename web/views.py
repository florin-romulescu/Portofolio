from django.shortcuts import render, get_object_or_404, get_list_or_404
from django.http import JsonResponse
from . import models

class IndexPage:
    template_name="web/index.html"
    context = {
        "title" : "Portofolio",
    }
    
    @staticmethod
    def as_view(request):
        owner = get_object_or_404(models.Owner, pk=1)
        projects = models.Project.objects.all()
        
        IndexPage.context["owner"] = owner
        IndexPage.context["projects"] = projects
        IndexPage.context["projects_range"] = range(len(projects))
        
        return render(request,
                      IndexPage.template_name, 
                      IndexPage.context)