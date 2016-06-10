$(document).ready(function(){

	$("#project_button").click(function() {
	    $('html, body').animate({
	        scrollTop: $("#projects_tab").offset().top-70
	    }, 500);
	});

	$("#photo_button").click(function() {
	    $('html, body').animate({
	        scrollTop: $("#photo_tab").offset().top-70
	    }, 500);
	});

	$("#main_button").click(function() {
	    $('html, body').animate({
	        scrollTop: $("#intro_tab").offset().top-70
	    }, 500);
	});

	$("#contact_button").click(function() {
	    $('html, body').animate({
	        scrollTop: $("#contact_tab").offset().top-70
	    }, 500);
	});

});