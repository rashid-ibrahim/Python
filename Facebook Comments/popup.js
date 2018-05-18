$(function() {
	let commentOrder = $('#selOrder');
	
	$(commentOrder).on('change', function() {
		$('_3scs > _p').each(function(e) {
			e.preventDefault();
			console.log(e);
			console.log('need to trigger click on what i want now);
		}
	});
	
	$('_3scs > _p').show(10, function() {
		console.log('click event fire on show');
	});
});