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
            "field_optgroup_type": [{
                "Choices": [],
            }, {
                "NoChoices": []
            }
            ]

        }

    }
    choice_opt_group = ["dropDown","choice","multipleChoices"]
    no_choice_opt_group = ["text","date&time","fileUpload","number"]

    sections = form.section_set.all()
    for i in sections:
        dic["section"]["section_title"].append(i.sec_title)
        dic["section"]["section_description"].append(i.description)
        fields = i.field_set.all()
        for j in fields:
            dic["field"]["field_description"].append(j.description)
            dic["field"]["field_label"].append(j.label)
            field_type = j.field
            if field_type in choice_opt_group:
                #type is choices
                choices = j.choice_set.all()
                choices_list = []
                for k in choices:
                    choices_list.append(k.option)
                dic["field"]["field_optgroup_type"][0]["Choices"].append({"field_type":field_type,"options":choices_list})
                #for all choices in field type

            elif field_type in no_choice_opt_group:
                #type is no choices
                dic["field"]["field_optgroup_type"][1]["NoChoices"].append(field_type)


    return JsonResponse({'format':dic})



def response(request):
    return render(request , 'form/response.html')
