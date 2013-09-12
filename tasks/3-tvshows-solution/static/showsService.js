var ShowsService = {
	create: function(show) {
		return $.ajax({
		  type: "POST",
		  url: "http://localhost:5000/shows",
		  data: JSON.stringify(show),
		  contentType: "application/json"
		});		
	},

	list: function() {
		return $.getJSON("http://localhost:5000/shows");	
	}
}