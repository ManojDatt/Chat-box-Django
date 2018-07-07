$(".messages").animate({ scrollTop: $(document).height() }, "fast");

$(".expand-button").click(function() {
  $("#profile").toggleClass("expanded");
	$("#contacts").toggleClass("expanded");
});

function current_time(){
  var currentdate = new Date(); 
    var datetime =  
                + currentdate.getHours() + ":"  
                + currentdate.getMinutes() + ":" 
                + currentdate.getSeconds() + ", "
                + currentdate.getDate() + "-"
                + (currentdate.getMonth()+1)+ "-"
                + currentdate.getFullYear();
  return datetime;
} 

function newMessageSend(message, message_id, time) {
	
	if($.trim(message) == '') {
		return false;
	}
	$('<li class="sent" message-id="'+message_id+'"><p>' + message + '<br><span class="badge preview">'+time+'</span></p></li>').appendTo($('.messages ul'));
	$('.contact.active .preview').html('<span>You: </span>' + message);
	$(".messages").animate({ scrollTop: $(document).height() }, "fast");
};

function newMessageReceived(message, message_id, time) {
	
	if($.trim(message) == '') {
		return false;
	}
	$('<li class="replies" message-id="'+message_id+'"><p>' + message + '<br><span class="badge preview">'+time+'</span></p></li>').appendTo($('.messages ul'));
	$('.contact.active .preview').html('<span>You: </span>' + message);
	$(".messages").animate({ scrollTop: $(document).height() }, "fast");
};

function MessageSend(){
	var request_data = {
                        sender: $("#sender_id").val(),
                        receiver: $("#receiver_id").val(),
                        message: $("#message_box").val()
                        }
      $.post('/chat-box/send-message', request_data, function(data, status){
        $('.message-input #message_box').val(null);
        time = current_time()
        newMessageSend(message, data.message_id, time);
      })
}
$(document).on('click', '#send_message' , function() {
  MessageSend()
});

$(window).on('keydown', function(e) {
  if (e.which == 13) {
    MessageSend();
    return false;
  }
});


$(".contact").click(function(){
	$(".messages").find('ul').empty()
	$("#message_box").prop('readonly', false)
	$(this).parent().find('.contact').each(function(){
		$(this).removeClass('active')
	});
	$(this).addClass('active')
	name = $(this).find('.name').text()
	$(".contact-profile").find("p b").text(name)
	icon_ = $(this).find('.icon-circle').attr('style')
	$(".contact-profile").find(".icon-circle").attr('style', icon_)
	receiver = $(this).find('.wrap').attr("contact-id")
	$("#receiver_id").val(receiver)
	setInterval(function(){
		$.get("/chat-box/load-messages/"+receiver, function(data, status){
			console.log(data)
        data.forEach(function(val){
        	message_present = false
        	$(".messages").find('li').each(function(){
        		if($(this).attr('message-id') == val.id){
        			message_present = true
        		}
        	})
        	if(! message_present){
        		if(val.sender == parseInt(receiver)){
	        		newMessageReceived(val.message, val.id, val.sendon)
	        	}else{
	        		 newMessageSend(val.message, val.id, val.sendon)
	        	}
        	}
        	
        })
      })

	}, 1000)
	
})

$(document).on('keypress keyup','.search-contact' , function(e) {
  
  $("#contacts").find('.contact').each(function(){
  	search_string = $('.search-contact').val()
  	if(search_string != ""){
  		
  		if($(this).find('.name').text().toLocaleLowerCase().includes(search_string.toLocaleLowerCase())){
  			$(this).removeClass('hide')
  		}else{
  			$(this).addClass('hide')
  		}

  	}else{
  		$(this).removeClass('hide')
  	}
  })
});


