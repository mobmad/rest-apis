# Introduction to REST APIs
A basic introduction to using REST APIs from curl, javascript and python, as well as creating a simple REST API.

By completing the following the [presentation](http://mobmad.github.io/rest-apis/) and the companion tasks, you should have a basic understanding of how to use and create REST APIs.

## Installation
1. Some of the code samples use pyhton. You should [install it](http://www.python.org/getit/) if you haven't already.
2. [Install pip](http://www.pip-installer.org/en/latest/installing.html) if you haven't already
3. `pip install Flask` (using virtualenv if you like, see [installation details](http://flask.pocoo.org/docs/installation/))
4. `pip install Flask-BasicAuth`
5. `pip install requests`

## Tasks
Follow the [presentation](http://mobmad.github.io/rest-apis/). When instructed, open a `tasks/<task-number>` folder. When done or you're stuck, have a look at `tasks/<task-number>-solution` for one way at solving the task.

## What's not covered? (aka Disclaimer)
This tutorial a starting point and not an exhaustive guide for implementing REST APIs.
For brevity, several topics have been left out, such as:

* Some REST constraints: Caching and hypermedia support
* Versioning of APIs
* Security aspects such as:
	* Authentication/authorization
	* Validating user input
	* Escaping output to avoid XSS
	* Preventing Cross-Site Request Forgery (CSRF attacks)
	* Cross-domain issues