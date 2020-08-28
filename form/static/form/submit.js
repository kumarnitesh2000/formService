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
        "field_type_list":[

    ]

    }
    
  }
var but = document.getElementById('submit');

//TODO
let submitJson  = () =>{
//For Testing Alert

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
        objJson.field.field_type_list.push({"field_type":t,options:[],"index":j-1});
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
    //logging the resultant template
    console.log(objJson);
    //xmlhttp.open(method,url,isasync)


/*

    xmlhttp.open("POST", "/forms/create", true);
    xmlhttp.setRequestHeader("Content-type", "application/x-www-form-urlencoded");
    var token = document.querySelector('[name="csrfmiddlewaretoken"]').value ;

    xmlhttp.send(`csrfmiddlewaretoken=${token}&body=${JSON.stringify(objJson)}`);


    location.href = '/forms/response';

*/
}
but.addEventListener('click',submitJson);
