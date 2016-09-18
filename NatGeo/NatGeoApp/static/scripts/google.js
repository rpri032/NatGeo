alert('google script invoked')
$(document).ready(function(){
	var addressSearch = $('#addressSearch').click(function(){
		alert('addressSearch Clicked');
		var googleSearchRequest = $.get("/sendRequest/" + $('#searchQuery').val());
		googleSearchRequest.done(function(data){
			$('#addressResult').attr('url', data.result);
		});
	});
	alert('addressSearch Ready');
});