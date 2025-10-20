from passlib.context import CryptContext
def hashpassword():
    while True:
        password=input(">>>")
        pwd_context = CryptContext(schemes=["argon2", "bcrypt"],default="argon2", deprecated="auto")
        passwordhash = pwd_context.hash(password)
        print(passwordhash)
hashpassword()