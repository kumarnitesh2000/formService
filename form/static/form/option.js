//global variable

var selectFun_added = [];


// get in the current id
let getid = (choice_id) =>{

var id_list = choice_id.split('_');
var id = id_list[1];
return parseInt(id);

}



//checking for choice_type
let search = (find,choices) =>{

for(var i=0;i<choices.length;i++){

    if(choices[i]==find)
    return true;


}

return false ;
}

//add more function to add more options
let addMore = (e) =>{

var button_identity = e.target.id;
var id = getid(button_identity);

var selec_id = button_identity.split('_');
var count = document.getElementById(String(id)).value;
var fin_count = parseInt(count)+1;
document.getElementById(String(id)).value = String(fin_count);
var counter = document.getElementById(String(id)).value;
//creating A LABEL
var label = document.createElement('label');
label.innerHTML = 'Option '+counter;
//creating a br
var br = document.createElement('br');
//creating a input
var input = document.createElement('input');
input.setAttribute('type','text');
input.setAttribute('value','');
var input_id = `${selec_id[0]+'_'+selec_id[1]}_input_${counter}`;
input.setAttribute('id',input_id);
//field
var field_div =  document.getElementById('choice_'+String(id)+'_total');

field_div.appendChild(label);
field_div.appendChild(input);
field_div.appendChild(br);

}

let searchid =(id,selectFun_added) => {
for(var i=0;i<selectFun_added.length;i++)
{
    if(id==selectFun_added[i])
    return true
}
return false;

}


//function to add the choice when choice opt group is selected
let selectFun = (e) =>
{

        var choices = ["choice","multipleChoices","dropDown"];
        var select_id = e.target.id;
        var id = getid(select_id);
        var field_type = document.getElementById(select_id).value;
        if(!search(field_type,choices)){
        if(searchid(id,selectFun_added))
                    {

                         // this is the area where you select nochoice opt group after choice opt group
                         //console.log(id);
                         var dom_id = document.getElementById('choice_'+id+'_total');
                         //console.log(dom_id);
                         dom_id.style.display = 'none';
                    }
        }
        else if(search(field_type,choices)){
        //alert("Choice Type");

        if(searchid(id,selectFun_added)){
        //console.log('not able');

        return ;

        }
        else
        selectFun_added.push(id);

        var counter = document.getElementById(String(id)).value;
        //creating a div
        var div = document.createElement('div');
        div.setAttribute('id',select_id+'_total');
        //creating A LABEL
        var label = document.createElement('label');
        label.innerHTML = 'Option '+counter;
        //creating a br
        var br = document.createElement('br');
        //creating a input
        var input = document.createElement('input');
        input.setAttribute('type','text');
        input.setAttribute('value','');
        var input_id = `${select_id}_input_${counter}`;
        input.setAttribute('id',input_id);
        //creating a add option button
        var button = document.createElement('button');
        button.setAttribute('id',select_id+'_add');
        button.innerHTML = 'Add';
        button.setAttribute('onclick','addMore(event)');
        //append all in div
        div.appendChild(br);
        div.appendChild(button);
        div.appendChild(br);
        div.appendChild(label);
        div.appendChild(input);


        //field
        var field_div =  document.getElementsByClassName('field')[id-1];
        field_div.appendChild(div);
        }
}

