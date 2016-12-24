/*
* Create the position sticky effect using Bootstrap's affix.
* The sidebar becomes sticky when it has reached the top of the page.
*/
$(document).ready(function () {

	$("#sidebar").affix({
		offset: {
			top: $('header').height(),
			bottom: function () {
				return $('footer').height() + 36;
			}

		}
	});
});



