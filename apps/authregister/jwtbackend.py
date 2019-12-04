from rest_framework.authentication import get_authorization_header, BaseAuthentication
from apps.authregister.models import Customers
from rest_framework import status, exceptions
import os
import jwt, json
from rest_framework.response import Response

class JWTAuthentication(BaseAuthentication):

    def authenticate(self,request):
        auth = get_authorization_header(request).split()

        if not auth:
            return None
        if len(auth) == 1:
            return None
        elif len(auth) > 2:
            return None

        try:
            token = auth[1]
            if token == "null":
                raise exceptions.AuthenticationFailed('Null token not allowed')
        except UnicodeError:
            msg = 'Invalid token header. Token string should not contain invalid characters.'
            raise exceptions.AuthenticationFailed(msg)

        return self.authenticate_credentials(token)

    def authenticate_credentials(self,token):

        try:
            payload = jwt.decode(token,os.environ["SECRETKEY"])
        except jwt.ExpiredSignatureError:
            return None
        else:
            email = payload["email"]
            customerId = payload["id"]
            customer = Customers.objects.get(email = email)
            customer.is_authenticated = True
            return (customer,token)
