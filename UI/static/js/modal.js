// Get the button that opens the modal
var rows = document.getElementsByClassName("more-details");

// When the user clicks the button, open the modal
var on_row_click = function (event) {
	var data = event.target.parentNode.getAttribute("data");
	if (data) {
		alert(data);

	}
	modal.querySelector("#modal-name").innerText = "Santos";
	modal.querySelector("#modal-status").innerText = "Available";
	modal.querySelector("#modal-tripto").innerText = "Namasuba";
	modal.querySelector("#modal-cost").innerText = "4000";
	modal.querySelector("#modal-date").innerText = "2018-06-24";
	modal.querySelector("#modal-contact").innerText = "0377888999";
	modal.style.display = "block";
};

Array.from(rows).forEach(function (element) {
	element.addEventListener('click', on_row_click);
});


// Get the modal
var modal = document.getElementById('myModal');

// Get the <span> element that closes the modal
var span = document.getElementsByClassName("close")[0];

// When the user clicks on <span> (x), close the modal
span.onclick = function () {
	modal.style.display = "none";
};

// When the user clicks anywhere outside of the modal, close it
window.onclick = function (event) {
	if (event.target === modal) {
		modal.style.display = "none";
	}
};
