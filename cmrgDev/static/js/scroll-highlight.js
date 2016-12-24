/*
* Allow for the list items in the side nav to be highlighted when the section
* is scrolled to.
*/
$(document).ready(function () {

	$('body').scrollspy({
		target: '.bs-docs-sidebar',
		offset: 82
	});
});
