
# Generate a 10 character alphanumeric password

import secrets
import string

key = string.ascii_letters + string.digits
password = ''.join(secrets.choice(key) for i in range(10))

print('10 character alphanumeric password: ' + password)


# Generate a 10 character alphanumeric password with at least one lowercase character, at least one uppercase character, and at least three digits

key = string.ascii_letters + string.digits
while True:
    password = ''.join(secrets.choice(key) for i in range(10))
    if (any(c.islower() for c in password) and any(c.isupper()
    for c in password) and sum(c.isdigit() for c in password) >= 3):
        print('10 character alphanumeric password with at least one lowercase character, at least one uppercase character, and at least three digits: ' + password)
        break


# Return a random integer from within a given range

password = secrets.randbelow(20)
print('random integer: ' + str(password))


# Return a random integer with k random bits

password = secrets.randbits(7)
print('random integer with k random bits: ' + str(password))


# Generating Tokens: At least 32 bytes for tokens should be used to be secure against a brute-force attack.


# Generates a random byte string containing nbytes number of bytes. If no value is provided, a reasonable default is used.
  
token1 = secrets.token_bytes() 
token2 = secrets.token_bytes(10) 
  
print('token with random length: ' + str(token1)) 
print('token with 10 characters: ' + str(token2))


# Generates a random text string in hexadecimal containing nbytes random bytes. If no value is provided, a reasonable default is used.
  
token1 = secrets.token_hex() 
token2 = secrets.token_hex(10) 
  
print('hexadecimal token with random length: ' + str(token1)) 
print('hexadecimal token with 10 characters: ' + str(token2))


# Generates a random URL-safe text string containing nbytes random bytes. This is suitable for password recovery applications.
# Example : Generate a hard-to-guess temporary URL containing a security token.
  
url = 'https://mydomain.com/reset=' + secrets.token_urlsafe() 
print('random url with random length: ' + url) 