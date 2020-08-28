from django.shortcuts import render,redirect
from .forms import FormForm,SectionForm,FieldForm
from .models import Form
from django.http import JsonResponse

def create(request):
    if request.method=='POST':
        # here this is responsible for submitting the Form Template .
        post_request = request.POST
        print(post_request)
        # contribute here for this project
        # you have to retrieve all the info from post_request


        # code space above either print the data that you retrieve to prove your work
        return redirect('response')
    forminstance = FormForm()
    sectionforminstance = SectionForm()
    fieldform = FieldForm()
    context = {'form': forminstance,'secForm':sectionforminstance,'fieldform':fieldform}
    return render(request, template_name='form/create.html',context=context)


def formInfo(request,id):
    try:
        form = Form.objects.get(id=id)
    except:
        print('No Form Exist .')
        return JsonResponse({"msg": "Bad Request"})


    dic = {
        "form": {

            "form_title": form.title,
            "form_description": form.description
        },

        "section": {
            "section_title": [],
            "section_description": []
        },

        "field": {

            "field_description": [],
            "field_label": [],
            "field_type_list": [


            ]

        }

    }
    sections = form.section_set.all()
    for i in sections:
        dic["section"]["section_title"].append(i.sec_title)
        dic["section"]["section_description"].append(i.description)
        fields = i.field_set.all()
        for k,j in enumerate(fields):
            dic["field"]["field_description"].append(j.description)
            dic["field"]["field_label"].append(j.label)
            field_type = j.field
            options_list = j.choice_set.all()
            option_list_option = []
            for l in options_list:
                option_list_option.append(l.option)
            index = k
            dic["field"]["field_type_list"].append({
                "field_type":field_type,
                "index":index,
                "options": option_list_option
            })

    return JsonResponse({'format':dic})



def response(request):
    return render(request , 'form/response.html')
