//Javascript included
console.log('JS Added !');

//add Section
var addSecBut = document.getElementById('addSec');
//add field
var addFieldBut = document.getElementById('addField');

var init = 1;
//button clicked of add Section
addSecBut.addEventListener('click',function(){

var body = document.getElementsByTagName('body')[0];
init+=1
var sec_title_id = 'sec_title_'+init;
var sec_des_id = 'sec_des_'+    init ;
console.log('Adding Section ');
var div = document.createElement('div');
var input = document.createElement('input');
var textarea = document.createElement('textarea');
textarea.setAttribute('id',sec_des_id);
input.setAttribute('type','text');
input.setAttribute('id',sec_title_id);
var label_2 = document.createElement('label');;
label_2.innerHTML = 'Description '
var label = document.createElement('label');
label.innerHTML = 'Section Title'
div.setAttribute('class','section');
div.appendChild(label);
div.appendChild(input);
div.appendChild(label_2);
div.appendChild(textarea);
body.appendChild(div);
});
var initial = 1;

//button clicked of add Field
addFieldBut.addEventListener('click',function(){
console.log('Adding Field ');
var body = document.getElementsByTagName('body')[0];
initial+=1;
var description_id = 'description_'+initial.toString();
var label_id = 'label_' + initial.toString();
var choice_id = 'choice_'+initial.toString();
var div = document.createElement('div');
div.setAttribute('class','field');
var label_2 = document.createElement('label');;
label_2.innerHTML = 'Description ';

var hidden_input = document.createElement('input');
hidden_input.setAttribute('type','hidden');
hidden_input.setAttribute('value','1');
hidden_input.setAttribute('id',initial);
div.append(hidden_input);

div.appendChild(label_2);
var textarea = document.createElement('textarea');
textarea.setAttribute('id',description_id);
var span = document.createElement('span');
span.setAttribute('class','description');
span.appendChild(textarea);
var br = document.createElement('br');

div.appendChild(span);
div.appendChild(br);
var input = document.createElement('input');
input.setAttribute('type','text');
input.setAttribute('value','Label');
input.setAttribute('id',label_id);
var label = document.createElement('label');
label.appendChild(input);
div.appendChild(label);
var select = document.createElement('select');
select.setAttribute('name','fields');
select.setAttribute('id',choice_id);
select.setAttribute('onchange','selectFun(event)');
var opgroup1 = document.createElement('optgroup');
var opgroup2 = document.createElement('optgroup');
opgroup1.setAttribute('label','Choices');
opgroup2.setAttribute('label','NoChoices');

var option1 = document.createElement('option');
option1.setAttribute('value','choice');
option1.innerHTML = 'Choices';

var option2 = document.createElement('option');
option2.setAttribute('value','multipleChoices');
option2.innerHTML = 'multipleChoices';

var option3 = document.createElement('option');
option3.setAttribute('value','dropDown');
option3.innerHTML = 'dropDown';


var option4 = document.createElement('option');
option4.setAttribute('value','text');
option4.innerHTML = 'TextField';

var option5 = document.createElement('option');
option5.setAttribute('value','datetime');
option5.innerHTML = 'Date&Time';

var option6 = document.createElement('option');
option6.setAttribute('value','fileUpload');
option6.innerHTML = 'FileUpload';

var option7 = document.createElement('option');
option7.setAttribute('value','number');
option7.innerHTML = 'NumberOnly';
//adding 3 option
opgroup1.appendChild(option1);
opgroup1.appendChild(option2);
opgroup1.appendChild(option3);
//adding 4 option
opgroup2.appendChild(option4);
opgroup2.appendChild(option5);
opgroup2.appendChild(option6);
opgroup2.appendChild(option7);



select.appendChild(opgroup2);
select.appendChild(opgroup1);

div.appendChild(select);
body.appendChild(div);


});


