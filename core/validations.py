from rest_framework import exceptions
from core.response_format import message_response

def check_invalid(fields):
    if None in fields:
        raise exceptions.ValidationError(message_response("INVALID_INPUT", "400"), 400)

