from enum import Enum

class AuthenticationType(Enum):

	UsernamePassword = "Username and Password"
	CookieRead = "Cookie read from disk"
	Face = "Face"