function ShowController(showsEl, createEl) {
	this.showsView = showsEl;
	this.createEl = createEl; 
	this.createEl.submit(this.createShow.bind(this));
}

ShowController.prototype = {
	createShow: function(e) {
		e.preventDefault();

		var nameField = this.createEl.find("input[name='name']"),
			sidField = this.createEl.find("input[name='sid']");

		var show = {
			name: nameField.val(),
			sid: sidField.val()
		};
		
		nameField.val('');
		sidField.val('');
		
		var app = this;
		ShowsService.create(show).done(function(show) {
			app.addShow(show);
		});	
	},
	addShow: function(show) {
		// TODO: update shows.id with the link to the show
		this.showsView.append("<li><a href='/shows/" + show.id + "'>" + show.name + "</a></li>")
	},
	getShows: function() {
		var app = this;
		ShowsService.list().done(function(data) {
			var shows = data.shows;
			shows.forEach(app.addShow.bind(app));
		});	
	}	
}