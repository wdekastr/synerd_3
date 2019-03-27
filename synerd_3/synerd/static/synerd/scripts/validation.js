var $ = function (id) {
	return document.getElementById(id); // $ jQuery standard function
}

function passwordCheck() {
	
	var password = document.getElementById("id_Password");
	var passwordval = document.getElementById("id_Password").value;
	var passwordlength = password.value.length;
	var lowernum = 0;
	var uppernum = 0;
	var digitnum = 0;
	var lengthnum = 0;
	var lowerCaseLetters = /[a-z]/g;
	var upperCaseLetters = /[A-Z]/g;
	var numbers = /[0-9]/g;

	if(password.value.match(lowerCaseLetters)) {  
		$("lowererrormessage").style = "display: none;";
		lowernum = 1;
  } else {
		$("lowererrormessage").style = "display: block;";
		lowernum = 0;
  }

  	if(password.value.match(upperCaseLetters)) {  
		$("uppererrormessage").style = "display: none;";
		uppernum = 1;
  } else {
		$("uppererrormessage").style = "display: block;";
		uppernum = 0;
  }
 
   	if(password.value.match(numbers)) {  
		$("digiterrormessage").style = "display: none;";
		digitnum = 1;
  } else {
		$("digiterrormessage").style = "display: block;";
		digitnum = 0;
  }

   	if(passwordlength >= 4) {  
		$("lengtherrormessage").style = "display: none;";
		lengthnum = 1;
  } else {
		$("lengtherrormessage").style = "display: block;";
		lengthnum = 0;
	}

	var totalnum = lowernum+uppernum+digitnum+lengthnum;

	if (totalnum == 4) {
		$("submitID").style = "background-color: #617bff;"
		$("submitID").disabled = false;
	} else {
		$("submitID").style = "background-color: #cc0000;"
		$("submitID").disabled = true;
	}

}

function logincheck() {
	var username = document.getElementById("id_Username").value;
	var password = document.getElementById("id_Password").value;

	if (username === "") {
		$("usernamemessage").style = "display: block;";
	}

	if (password === "") {
		$("passwordmessage").style = "display: block;";
	}

	if (username !== "" && password !== "") {
		$("usernamemessage").style = "display: none;";
		$("passwordmessage").style = "display: none;";
		setTimeout(function() {
			document.getElementById("loginform").submit();
		}, 250);
	}


	if (username == "" && password !== "") {
		$("usernamemessage").style = "display: block;";
		$("passwordmessage").style = "display: none;";
	}

	if (username !== "" && password == "") {
		$("usernamemessage").style = "display: none;";
		$("passwordmessage").style = "display: block;";
	}

}

