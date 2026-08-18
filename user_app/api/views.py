from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from user_app.api.serializers import RegistrationSerializer

# Function-based view for user registration
@api_view(['POST',])
def registration_view(request):
    if request.method == 'POST':
        serializer = RegistrationSerializer(data=request.data)

        data = {}

        if serializer.is_valid():
            account = serializer.save()

            data['response'] = "Registration successful!"
            data['username'] = account.username
            data['email'] = account.email

            token, _ = Token.objects.get_or_create(user=account)
            data['token'] = token.key

            return Response(data, status=status.HTTP_201_CREATED)
        
        else:
            data = serializer.errors
        
        return Response(data, status=status.HTTP_400_BAD_REQUEST)