from django.shortcuts import render
from django.contrib.auth import login, logout, authenticate
from .serializers import UserSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

class UserRegisterView(APIView):
    # Registra usuários no banco de dados
    
    def get(self, request):
        return render(request, 'register.html')
    
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        
        if serializer.is_valid():
            serializer.save()
            
            return Response({"message": "Registro realizado com sucesso."}, status=status.HTTP_201_CREATED)
        else:
            return Response({"message": "Dados informados inválidos."}, status=status.HTTP_400_BAD_REQUEST)
 
class UserLogarView(APIView):
    # Faz o login de usuários
    
    def get(self, request):
        return render(request, 'login.html')
            
    def post(self, request):
        username = request.POST['username']
        password = request.POST['password']
        
        user = authenticate(
            request,
            username=username,
            password=password
        )
        
        if user is not None:
            login(request, user)
            
            return Response({"message": "Login realizado com sucesso."}, status=status.HTTP_200_OK)
        else:
            return Response({"message": "Credenciais inválidas."}, status=status.HTTP_401_UNAUTHORIZED)
        
class LogoutView(APIView):
    # Faz o logout de usuários
    
    permission_classes = [IsAuthenticated]
    
    def post(self, request):
        logout(request)
        
        return Response({"message": "Logout realizado com sucesso."}, status=status.HTTP_200_OK)
        
