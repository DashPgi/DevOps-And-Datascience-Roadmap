# Decorators

users = {"usrname" : "aria", "access_lvl": "admin"}

def get_admin_password():
    return "1234"

def make_secure(func):
    def secure_function():
        if users["access_lvl"] == "admin":
            return func()
        else:
            "no admin permissions"
    return secure_function

get_admin_password = make_secure(get_admin_password)

print(get_admin_password())