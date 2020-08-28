//import * as data from '../../../formFormat.json';
var objJson = {
    "form": {

        "form_title":"",
        "form_description":""
    },

    "section":{
        "section_title":[],
        "section_description":[]
    },

    "field":{

        "field_description":[],
        "field_label":[],
        "field_optgroup_type":[{
            "Choices":[]
        },{
            "NoChoices":[]
        }
    ]

    }
    
  }
var but = document.getElementById('submit');

let search = (t,choices) =>{

for(var i=0;i<choices.length;i++){

    if(t==choices[i]){
        return true ;
    }

}
return false;
}


//TODO
let submitJson  = () =>{
//For Testing Alert
    var choices = ["dropDown","choice","multipleChoices"];
    var nochoices = ["text","date&time","fileUpload","number"];
    //form title , description
    var form_title = document.getElementById('id_title').value;
    var form_description = document.getElementById('id_description').value;
    objJson.form.form_title = form_title;
    objJson.form.form_description = form_description ;
    //Hardik contrib
    var sec = document.getElementsByClassName("section").length;
    var fld = document.getElementsByClassName("field").length;
    
    for(var i =1; i<= sec; i++){
        var p = document.getElementById("sec_title_"+i);
        objJson.section.section_title.push(p.value);
        objJson.section.section_description.push(document.getElementById("sec_des_"+i).value);
    }
    for(var j=1;j<= fld;j++){
        var p= document.getElementById("description_"+j);
        objJson.field.field_description.push(p.value);
        objJson.field.field_label.push(document.getElementById("label_"+j).value);
        var t =  document.getElementById('choice_'+j).value;
        if(search(t,choices))
        objJson.field.field_optgroup_type[0].Choices.push({"field_type":t, options:[]})
        else
        objJson.field.field_optgroup_type[1].NoChoices.push(t);
    }
    //now this objJson for to
    //xhr post request
    //objJson
    if (window.XMLHttpRequest) {
    // code for modern browsers
        xmlhttp = new XMLHttpRequest();

    } else {
    // code for old IE browsers
        xmlhttp = new ActiveXObject("Microsoft.XMLHTTP");
    }

    //xmlhttp.open(method,url,isasync)
    xmlhttp.open("POST", "/forms/create", true);
    xmlhttp.setRequestHeader("Content-type", "application/x-www-form-urlencoded");
    var token = document.querySelector('[name="csrfmiddlewaretoken"]').value ;

    xmlhttp.send(`csrfmiddlewaretoken=${token}&body=${JSON.stringify(objJson)}`);


    location.href = '/forms/response'
}
but.addEventListener('click',submitJson);
