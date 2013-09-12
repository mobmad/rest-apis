function ShowController(showsEl, createEl) {
	this.showsView = showsEl;
	this.createEl = createEl; 
	this.createEl.submit(this.createShow.bind(this));
}

ShowController.prototype = {
	createShow: function(e) {
		e.preventDefault();

		alert("Implement me!");
		// Should get values from gui and use ShowsService to create the show
	},
	addShow: function(show) {
		this.showsView.append("<li>" + show.name + "</li>")
	},
	getShows: function() {
		// IMPLEMENT
		// Should use ShowsService to list shows
	}	
}