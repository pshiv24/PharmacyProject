from rest_framework_jwt.settings import api_settings


def my_jwt_response_handler(token, user=None, request=None):
    return {
        "token": token,
        "user": {
            "username": user.username,
            "is_admin": user.is_admin,
            "is_customer": user.is_customer,
        },
    }
