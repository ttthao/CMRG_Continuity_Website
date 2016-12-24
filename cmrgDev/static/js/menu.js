$(document).ready(function () {

	/*
	* Open or close the menu when the menu button is clicked.
	*/
	$("#menu-toggle").click(function(e) {
		e.preventDefault();
		$("#wrapper").toggleClass("toggled");
		$("body").toggleClass("no-scroll");
		$('#page-content-wrapper').toggleClass('fade');
	});

	/*
	* Deals with all things scrolling-related for the menu.
	* Display the page title on the navbar when it passes the jumbotron.
	* Displays the navigation title when it passes the jumbotron.
	*/
	$(document).scroll(function() {

		//top of window: current position
		scroll_start = $(this).scrollTop();

		//if page moves, change the navbar
		if (scroll_start > 0) {
			$('.menu-icon-wrapper').css('background-color', '#0E1B25');
			$('.menu-icon-wrapper').css('opacity', '0.8');

		}

		//restore original settings
		else {
			$('.menu-icon-wrapper').css('background-color', 'transparent');
		}

		//bottom of the jumbotron
		jumbotron_bottom = $('header').height();

		//if page moves past jumbotron, display title
		if (scroll_start > jumbotron_bottom) {
			$('.menu-nav-header').removeClass('disable');
		}

		//hide the title if jumbotron is in view
		else {
			$('.menu-nav-header').addClass('disable');
		}
	});
});

