import PassiveInputBlock
import ActiveInputBlock
import StartBlock.AuthenticationObject
from typing import List

class AuthenticatorBlock:

	def __init__(self):
		self.passiveInputBlock = None
		self.activeInputBlock = None

	def setPassiveInputBlock(self, passiveInputBlock: PassiveInputBlock):
		self.passiveInputBlock = passiveInputBlock
	def setActiveInputBlock(self, activeInputBlock: ActiveInputBlock):
		self.activeInputBlock = activeInputBlock

	def authenticateUser(self) -> bool:
		authenticationObjects: List[StartBlock.AuthenticationObject] = []
		######
		# getPassiveCredentials
		######
		authenticationObjects.extend(self.passiveInputBlock.getAuthenticationObjects())
		######
		# SendCredentials
		######
		######
		# ReceiveAnswer
		######
		######
		#
		######
		######
		# getActiveCredentials
		######
		authenticationObjects.extend(self.activeInputBlock.getAuthenticationObjects())
		for obj in authenticationObjects:
			print(obj.data)
			print(obj.type)
		return False

	def getUserActiveCredentials(self) -> tuple:
		return self.activeInput.getUserCredentials()
