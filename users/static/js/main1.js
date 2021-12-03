function Csubmit(){
  name = document.getElementById('name').value;
  if (name == ""){
    document.getElementById('name').style.borderColor = 'red'

    
  }
  date = document.getElementById('date').value;
   if (date == ""){
    document.getElementById('date').style.borderColor = 'red'
  }
  password = document.getElementById('password').value;
   if (password == ""){
    document.getElementById('password').style.borderColor = 'red'
  }
  email = document.getElementById('email').value;
   if (email == ""){
    document.getElementById('email').style.borderColor = 'red'
  }
  phone = document.getElementById('phone').value
 if (phone == ""){
    document.getElementById('phone').style.borderColor = 'red'
  }
}
function namec (n){
  nameC = document.getElementById('nCheck').value
if (nameC == 'False'){
  alert('This name is allready created try another ')
  
}
}