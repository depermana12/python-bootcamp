# decorator allow us to easily modify functions

import functools

user = {"username": "jose", "access_level": "guest"}


def make_secure(access_level):
    def decorator(func):
        @functools.wraps(func)
        def secure_function(*args, **kwargs):
            if user["access_level"] == access_level:
                return func(*args, **kwargs)
            else:
                return f"No {access_level} permissions for {user['username']}."

        return secure_function

    return decorator


@make_secure("admin")
def get_admin_password():
    return "admin: 1234"


@make_secure("user")
def get_dashboard_passwords():
    return "user: user_password"


print(get_admin_password())
print(get_dashboard_passwords())

user = {"username": "anna", "access_level": "admin"}

print(get_admin_password())
print(get_dashboard_passwords())
