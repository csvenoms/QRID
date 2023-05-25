from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
class CustomAuthToken(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        # Call the parent class's post method to get a token
        response = super(CustomAuthToken, self).post(request, *args, **kwargs)
        # Get the token and the user object
        token = Token.objects.get(key=response.data['token'])
        user = token.user
        # Add the user object to the response data
        data = {'token': token.key, 'user_id': user.pk, 'email': user.email, 'roll':user.roll_id, 'name':user.first_name,'lname':user.last_name,'id': user.student_id }
        return Response(data)


from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response

class MyView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request, format=None):
        content = {
            'user_id': request.user.pk,
            'email': request.user.email,
        }
        return Response(content)
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

class Logout(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request):
        request.user.auth_token.delete()
        return Response({'message': 'Logged out successfully.'})