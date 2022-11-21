import functools

user={"username":"jose","access_level":"admin"}

def make_secure(access_level):
    def decorator(func):
        @functools.wraps(func)
        def secure_function(*args, **kwargs):
            if user["access_level"]==access_level:
                return func(*args,**kwargs)   
            else:
                return f"no {access_level} permission for {user['username']} "

        return secure_function 
    return decorator

@make_secure("admin")
def get_admin_password():
    return "admin: 1234"

@make_secure("user")
def get_dashboard_password():
    return "user: user_password"


print(get_admin_password())
print(get_dashboard_password())

user={"username":"anna","access_level":"user"}

print(get_admin_password())
print(get_dashboard_password())



