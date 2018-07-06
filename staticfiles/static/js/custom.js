/*header fixed start*/
$(window).scroll(function () {
		$(window).scrollTop() >= 100 ? $(".sticky-header").addClass("fixed") : $(".sticky-header").removeClass("fixed")
	})
/*header fixed end*/

$(".info-item .btn").click(function(){
		$(".login-container").toggleClass("log-in");
});
$(".container-form .btn").click(function(){  
	$(".login-container").addClass("active");
});