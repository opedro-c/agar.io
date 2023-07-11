from werkzeug.exceptions import HTTPException


class DataAlreadyInUse(HTTPException):
    code = 400
    description = 'Someone already took your email or address'