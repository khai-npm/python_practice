import bcrypt

class HashPassword:

    salt: bytes
    def __init__(self):
        # Adding the salt to password
        self.salt =bcrypt.gensalt()

    def DoHashPassword(self, RawPass):
        tmpPwd = bytes(RawPass,'utf-8')
        
        
        # Hashing the password
        hashed = bcrypt.hashpw(tmpPwd, self.salt)

        return hashed
    


'''

ab = HashPassword()

Newpassword = "hi"
print(ab.DoHashPassword(Newpassword))




# Declaring our password
password = b'peashooter01'
 
# Adding the salt to password
salt = bcrypt.gensalt()
# Hashing the password
hashed = bcrypt.hashpw(password, salt)
 
# printing the salt
print("Salt :")
print(salt)
 
# printing the hashed
print("Hashed")
print(hashed)
'''