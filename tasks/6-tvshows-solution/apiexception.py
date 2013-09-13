class ApiException(Exception):
	def __init__(self, status_code, message):
		self._status_code = status_code
		self._message = message

	def __str__(self):
		return repr(self._message)

	@property
	def message(self):
		return self._message

	@property
	def status_code(self):
		return self._status_code