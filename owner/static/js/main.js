function Error1 (){
  name = document.getElementById('name').value
  password = document.getElementById('password').value
  email = document.getElementById('email').value;
  if (name == "" && password == "" && email == ""){
    let person = prompt("Please enter your name", "Harry Potter");
let text;
if (person == null || person == "") {
  text = "User cancelled the prompt.";
} else {
  text = "Hello " + person + "! How are you today?";
}
  }
  else {
    alert('go')
  }
}