import secrets
import string
def psw():
    c = ""

    p = string.ascii_lowercase + string.ascii_uppercase + string.punctuation
    for i in range(12):
        c = c + (secrets.choice(p))
         
    print(c)
psw()