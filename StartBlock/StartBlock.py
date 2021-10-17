from PassiveInputBlock import PassiveInputBlock
from SensorBlock import SensorBlock
from ActiveInputBlock import ActiveInputBlock
from AuthenticatorBlock import AuthenticatorBlock

class Startblock:

	def __init__(self):
		self.authenticator = AuthenticatorBlock.AuthenticatorBlock()

		######
		#Input Blocks
		######
		self.sensor = SensorBlock.SensorBlock(self.authenticator)
		self.passiveInput = PassiveInputBlock.PassiveInputBlock(self.authenticator)
		self.activeInput = ActiveInputBlock.ActiveInputBlock(self.authenticator)
		######
		# Setting Blocks for Authenticator to use
		######
		self.authenticator.setActiveInputBlock(self.activeInput)
		self.authenticator.setPassiveInputBlock(self.passiveInput)

		self.authenticateUser()

	def authenticateUser(self) -> bool:
		self.authenticator.authenticateUser()