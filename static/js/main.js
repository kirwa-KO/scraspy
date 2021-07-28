
$(function () {
	'use strict';

	$("#btn-download").on('click', function() {
		$(".download-section").fadeOut(1000, function (e){
			e.preventDefault();
		});
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
	})
})


// $(window).on('load', function () {
//     $("body").css("overflow", "auto");
//     $(".onload").fadeOut(1000, function (){
//         $(this).fadeOut(1000, function ()
//         {
//             $(this).remove();
// 			$("iframe").fadeIn(1000, function (){})
//         })
//     })
// });