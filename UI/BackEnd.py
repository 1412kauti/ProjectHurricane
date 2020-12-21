from random import randint

class BackEnd(object):

    def security_code(self):
       return randint(1, 1000)


user1 = BackEnd()

code = user1.security_code()

print(code)