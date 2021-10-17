import AuthenticatorBlock
from typing import List
import StartBlock.AuthenticationObject

class PassiveInputBlock:

	def __init__(self, authenticator: AuthenticatorBlock):
		pass

	def getAuthenticationObjects(self):
		print("PassiveShizzles")
		return []