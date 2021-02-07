class ErrorCatchMiddleware:
	def __init__(self, get_reponse):
		self._get_response = get_reponse

	def __call__(self, request):
		response = self._get_response(request)
		return response

	def proccess_exception(self, request, e):
		import logging

		logger = logging.getLogger(__name__)
		logger.debug('dfd')
