import random

def password():
	token = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
	result = ''
	for i in range (11):
		result = random.choice(token)
	return result
passw = password()
print(passw)
