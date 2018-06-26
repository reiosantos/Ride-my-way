function validateEmail(email) {
	var re = /^(([^<>()\[\]\\/.,;:\s@"]+(\.[^<>()\[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/;
	return re.test(email.toLowerCase());
}

function validateContact(phone) {
	var re = /\(?\d{3}\)?([\-\s\.])?\d{3}\1?\d{4}/;
	return re.test(phone.toLowerCase());
}

function validateAmount(cost) {
	var re = /^[.0-9]+$/;
	return re.test(cost);
}


function validatePassword(password) {
	var re = /^[\S\s]{6,}$/;
	return re.test(password.toLowerCase());
}

function submitForm(form) {
	var username = form.inputUsername;
	var password = form.inputPassword;
	var user = form.userType;

	document.getElementById("usernameError").style.display = "none";
	document.getElementById("passwordError").style.display = "none";

	if (form.id === "form-sign-in") {

		if (username.value.length > 3) {
			if (validatePassword(password.value)) {
				if (user.value === "passenger") {
					form.action = "passenger/index.html"

				} else if (user.value === "driver") {
					form.action = "driver/index.html"
				}
				return true;
			}
			document.getElementById("passwordError").style.display = "block";
			return false;
		}
		document.getElementById("usernameError").style.display = "block";
		return false;
	} else if (form.id === "form-sign-up") {
		var fullname = form.inputName;
		var contact = form.inputPhone;

		document.getElementById("nameError").style.display = "none";
		document.getElementById("contactError").style.display = "none";

		if (fullname.value.length > 3) {
			if (username.value.length > 3) {
				if (validateContact(contact.value)) {
					if (validatePassword(password.value)) {
						if (user.value === "passenger") {
							form.action = "passenger/index.html"
						} else if (user.value === "driver") {
							form.action = "driver/index.html"
						}
						return true;
					}
					document.getElementById("passwordError").style.display = "block";
					return false;
				}
				document.getElementById("contactError").style.display = "block";
				return false;
			}
			document.getElementById("usernameError").style.display = "block";
			return false;
		}
		document.getElementById("nameError").style.display = "block";
		return false;
	}
	return false;
}

function saveRide(form) {
	var location = form.inputLocation;
	var amount = form.inputCost;

	document.getElementById("locationError").style.display = "none";
	document.getElementById("costError").style.display = "none";

	if (form.id === "form-new-offer") {

		if (location.value.length > 3) {
			if (validateAmount(amount.value)) {
				return true;
			}
			document.getElementById("costError").style.display = "block";
			return false;
		}
		document.getElementById("locationError").style.display = "block";
		return false;
	}
	return false;
}


function searchRide(event) {

}

function searchRequest(event) {

}