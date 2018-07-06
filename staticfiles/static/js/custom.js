/*header fixed start*/
$(window).scroll(function () {
		$(window).scrollTop() >= 100 ? $(".sticky-header").addClass("fixed") : $(".sticky-header").removeClass("fixed")
	})
/*header fixed end*/

/*Menu star*/
$('#menu-toggle').click(function(){
  $(this).toggleClass('open');
})
/*Menu end*/




/*review star*/
$(document).ready(function () {
	$("#testimonial").owlCarousel({
		loop: true,
		navText: ["<img src='images/left-arrow.png'>", "<img src='images/right-arrow.png'>"],
		margin: 10,
		responsiveClass: true,
		nav: true,
		responsive: {
			0: {
				items: 1,
				nav: true
			},
			600: {
				items: 2,
				nav: true
			},
			1000: {
				items: 2,
				nav: true,
				loop: false,
				margin: 20
			}
		}
	})
})

/*review end*/



/*store star*/
$(document).ready(function () {
	$("#stores").owlCarousel({
		loop: true,  
		margin:0,
		responsiveClass: true,
		nav: true,
		responsive: {
			0: {
				items: 1,
				nav: true
			},
			600: {
				items: 3,
				nav: true
			},
			1000: {
				items: 5,
				nav: true,
				loop: false,
				margin: 0
			}
		}
	})
})

/*store end*/



/*Services Category start*/
$(document).ready(function () {
	$("#services-scroll").owlCarousel({
		loop: true,  
		navText: ["<img src='images/left-arrow.png'>", "<img src='images/right-arrow.png'>"],
		margin:10,
		responsiveClass: true,
		nav: true,
		responsive: {
			0: {
				items: 1,
				nav: true
			},
			600: {
				items: 2,
				nav: true
			},
			1000: {
				items: 3,
				nav: true,
				loop: false,
				margin: 30
			}
		}
	})
})

/*Services Category end*/
