import StartBlock.AuthenticationType

class AuthenticationObject:

	def __init__(self, data, type: StartBlock.AuthenticationType):
		self.data = data
		self.type = type
