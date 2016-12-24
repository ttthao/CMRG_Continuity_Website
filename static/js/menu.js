/*
* Open or close the menu when the menu button is clicked.
*/
$("#menu-toggle").click(function(e) {
  e.preventDefault();
  $("#wrapper").toggleClass("toggled");
  $("body").toggleClass("no-scroll");
  $('#page-content-wrapper').toggleClass('fade');
});
