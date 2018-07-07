$(".messages").animate({ scrollTop: $(document).height() }, "fast");

$(".expand-button").click(function() {
  $("#profile").toggleClass("expanded");
	$("#contacts").toggleClass("expanded");
});


function newMessage() {
	message = $(".message-input input").val();
	if($.trim(message) == '') {
		return false;
	}
	$('<li class="sent"><p>' + message + '</p></li>').appendTo($('.messages ul'));
	$('.message-input input').val(null);
	$('.contact.active .preview').html('<span>You: </span>' + message);
	$(".messages").animate({ scrollTop: $(document).height() }, "fast");
};


$('#send_message').click(function() {
  newMessage();
});

$(window).on('keydown', function(e) {
  if (e.which == 13) {
    newMessage();
    return false;
  }
});

$(".contact").click(function(){
	$("#message_box").prop('readonly', false)
	$(this).parent().find('.contact').each(function(){
		$(this).removeClass('active')
	});
	$(this).addClass('active')
	name = $(this).find('.name').text()
	$(".contact-profile").find("p b").text(name)
	icon_ = $(this).find('.icon-circle').attr('style')
	$(".contact-profile").find(".icon-circle").attr('style', icon_)
	$("#receiver_id").val($(this).find('.wrap').attr("contact-id"))
})