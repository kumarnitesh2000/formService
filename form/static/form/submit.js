//import * as data from '../../../formFormat.json';
var objJson = {
    "form": {

        "form_title":"Untitled Form",
        "form_description":"Enter The Description"
    },

    "section":{
        "section_title":[],
        "section_description":[]
    },

    "field":{

        "field_description":[],
        "field_label":[],
        "field_optgroup_type":[{
            "Choices":[{"DropDown":false},{"Choice":false},{"MultiChoice":false}],
            "Options":[]
        },{
            "NoChoices":[{"TextField":false},{"Date&Time":false},{"FileUpload":false},{"NumberOnly":false}]
        }
    ]

    }
    
}
var but = document.getElementById('submit');
//TODO
let submitJson  = () =>{
//For Testing Alert
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
        //var t= document.getElementById('choice_'+j);
        
    }
    console.log(objJson);
}
but.addEventListener('click',submitJson);
