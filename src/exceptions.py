from werkzeug.exceptions import HTTPException
from werkzeug.sansio.response import Response


class DataAlreadyInUse(HTTPException):
    code = 400
    description = 'Someone already took your email or address'