import AuthenticatorBlock
from StartBlock.AuthenticationObject import AuthenticationObject
from StartBlock.AuthenticationType import AuthenticationType

class ActiveInputBlock:

	def __init__(self, authenticator: AuthenticatorBlock):
		self.authenticator = authenticator

	def getUserCredentials(self) -> tuple:
		username = "a"#input("Nutzername: ")
		password = "b" #getpass.win_getpass("Passwort: ")
		return (username, password)

	def verifyCredentials(self, usernameAndPassword: tuple) -> bool:
		return all(usernameAndPassword) ##Return False if all values are empty or zero

	def getAuthenticationObjects(self):

		credentials = self.getUserCredentials()
		authObject = AuthenticationObject(credentials, AuthenticationType.UsernamePassword)
		return [authObject]
