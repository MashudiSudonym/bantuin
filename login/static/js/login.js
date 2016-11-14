$('.message-forgot').click(function(){
	$('.forgot-form').animate({height: "toggle", opacity: "toggle"}, "slow");
  	document.getElementById('login').style.display="none";
  	document.getElementById('register').style.display="none";
});

$('.message-register').click(function(){
	$('.register-form').animate({height: "toggle", opacity: "toggle"}, "slow");
  	document.getElementById('login').style.display="none";
  	document.getElementById('forgot').style.display="none";
});

$('.message-login').click(function(){
  	$('.login-form').animate({height: "toggle", opacity: "toggle"}, "slow");
 	document.getElementById('register').style.display="none";
	document.getElementById('forgot').style.display="none";
});