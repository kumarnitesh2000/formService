from django.shortcuts import render
from .forms import FormForm,SectionForm,FieldForm
from .models import Form,Section,Field,Choice
from django.http import JsonResponse
import json
from django.contrib.auth.models import User
import datetime
from datetime import timedelta

def create(request):
    if request.method=='POST':
        # here this is responsible for submitting the Form Template .
        post_request = request.POST
        body = post_request.get("body")
        body_dict = json.loads(body)
        form = body_dict["form"]
        section = body_dict["section"]
        field = body_dict["field"]
        #default author admin
        author = User.objects.get(id=1)
        #form valid upto 10 days
        d = datetime.datetime.now() + timedelta(days=10)
        #form part
        form_save = Form(title=form['form_title'],description=form['form_description'],publishDate=datetime.datetime.now(),endValidity=d,author=author)
        form_save.save()
        #section Part
        total_sections = len(section['section_title'])
        c = 0
        for i in range(total_sections):
            title = section['section_title'][i]
            description = section['section_description'][i]
            section_save = Section(sec_title=title,description=description,form=Form.objects.get(id=form_save.id))
            section_save.save()
            #total fields in this section

            total_fields = int(section['section_fields'][i])
            for k in range(c,total_fields):
                c+=1
                fields = Field(label=field['field_label'][k],description=field['field_description'][k],field=field['field_type_list'][k]['field_type'],section=section_save)
                fields.save()
                choices = field['field_type_list'][k]['options']
                choice_length = len(field['field_type_list'][k]['options'])
                for l in range(choice_length):
                    choice = Choice(option=choices[l],field=Field.objects.get(id=fields.id))
                    choice.save()

            #saving all the fields

        return JsonResponse({"id":form_save.id})

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
            "section_description": [],
             "section_fields" : []
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
        dic["section"]["section_fields"].append(len(i.field_set.all()))
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

    return JsonResponse({'template':dic})



def response(request):
    return render(request , 'form/response.html')
