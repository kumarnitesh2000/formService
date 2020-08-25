from django.shortcuts import render
from .forms import FormForm,SectionForm,FieldForm

from django.http import JsonResponse
DEFAULT_TITLE = ''
DEFAULT_DESCRIPTION = ''


def create(request):
    if request.method=='POST':
        print(request.POST)
        return JsonResponse(request.POST)
    forminstance = FormForm()
    sectionforminstance = SectionForm()
    fieldform = FieldForm()
    context = {'form': forminstance,'secForm':sectionforminstance,'fieldform':fieldform}
    return render(request, template_name='form/create.html',context=context)


