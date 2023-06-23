from typing import Any, Dict
from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.views.generic import View,TemplateView
from app.forms import *
def FUNCTION_BASED_VIEW(request):
    return HttpResponse("<h1>This is FUNCTION_BASED_VIEW </h1>")

class CLASS_BASED_VIEW(View):
    def get(self,request):
        return HttpResponse('<h1>this is CLASS_BASED_VIEW </h1>')

def FUNCTION_HTML(request):
    return render(request,'FUNCTION_HTML.html')

class CLASS_HTML(View):
    def get(self,request):
        return render(request,'CLASS_HTML.html')
    
def FUNCTION_FORM(request):
    d={'TFO':TopicForm()}
    return render(request,'FUNCTION_FORM.html',d)


class CLASS_CONTEXT_FORM(TemplateView):
    template_name='CLASS_CONTEXT_FORM.html'
    def get_context_data(self, **kwargs):
        PCM=super().get_context_data(**kwargs)
        TO=TopicForm()
        PCM['TO']=TO
        return PCM
    def post(self,request):
        TFO=TopicForm(request.POST)
        if TFO.is_valid():
            TFO.save()
        return HttpResponse('The data is inseted')
    





class HTML_CONTEXT(TemplateView):
    template_name='HTML_CONTEXT.html'
    def get_context_data(self,**kwargs):
        OB=super().get_context_data(**kwargs)
        OB['name']='Greeshma Shetty'
        OB['age']=22
        return OB