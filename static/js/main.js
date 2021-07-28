
$(function () {
	'use strict';

	$("#btn-download").on('click', function(e) {
		// e.preventDefault();
		const website_value = $("#website-input").val();
		if (website_value)
		{
			$(".download-section").fadeOut(1000, function (){});
			$(".informations-section").fadeOut(1000, function (){});
			$(".buy-coffe-section").fadeOut(1000, function (){});
			$(".loading").fadeIn(1000, function () {})
			// $.post("/fetched", {website: website_value});
		}
		else {
			$(".error-popup").fadeIn(1000, function () {
				$(this).fadeOut(3000, function() {})
			})
			e.preventDefault();
		}
	})

	$("#list-files").on("click", function () {
		$(".get-files-section").removeClass("d-none");
	});
	
	$("#close-get-files, .get-files-section").on("click", function () {
		$(".get-files-section").addClass("d-none");
	});

	$(".get-files-section .files-preview").on("click", function (event) {
		event.stopPropagation();
	})

	$("#settings").on("click", function () {
		$(".settings-section").removeClass("d-none");
	});

	$("#close-get-settings, .settings-section").on("click", function () {
		$(".settings-section").addClass("d-none");
	});

	$(".settings-section .settings-preview").on("click", function (event) {
		event.stopPropagation();
	})

	$(".html, .css, .js, .assets").on("click", function() {
		$(this).addClass('active').siblings().removeClass('active');;
	});

	$(".html").on("click", function () {
		$(".html-files").fadeIn(1000, function(){})
		$(".css-files").css("display", "none");
		$(".js-files").css("display", "none");
		$(".assets-files").css("display", "none");
	});

	$(".css").on("click", function () {
		$(".html-files").css("display", "none");
		$(".css-files").fadeIn(1000, function(){});
		$(".js-files").css("display", "none");
		$(".assets-files").css("display", "none");
	});

	$(".js").on("click", function () {
		$(".html-files").css("display", "none");
		$(".css-files").css("display", "none");
		$(".js-files").fadeIn(1000, function(){});
		$(".assets-files").css("display", "none");
	});

	$(".assets").on("click", function () {
		$(".html-files").css("display", "none");
		$(".css-files").css("display", "none");
		$(".js-files").css("display", "none");
		$(".assets-files").fadeIn(1000, function(){});
	});
})