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
        # Renderiza a página de registro
        return render(request, 'register.html')
    
    def post(self, request):
        
        serializer = UserSerializer(data=request.data)
        
        if serializer.is_valid():
            # Salva o usuário no banco de dados
            serializer.save()
            
            return Response({"message": "Registro realizado com sucesso."}, status=status.HTTP_201_CREATED)
        else:
            
            return Response({"message": "Dados informados inválidos."}, status=status.HTTP_400_BAD_REQUEST)
 
class UserLogarView(APIView):
    # Faz o login de usuários
    
    def get(self, request):
        # Renderiza a página de login
        return render(request, 'login.html')
            
    def post(self, request):
        # Obtém os dados do usuário
        username = request.POST['username']
        password = request.POST['password']
        # Faz a autenticação
        user = authenticate(
            request,
            username=username,
            password=password
        )
        
        if user is not None:
            # Faz o login do usuário
            login(request, user)
            
            return Response({"message": "Login realizado com sucesso."}, status=status.HTTP_200_OK)
        else:
            
            return Response({"message": "Credenciais inválidas."}, status=status.HTTP_401_UNAUTHORIZED)
        
class LogoutView(APIView):
    # Faz o logout de usuários
    
    # verifica se o usuário está logado
    permission_classes = [IsAuthenticated]
    
    def post(self, request):
        # Faz o logout
        logout(request)
        
        return Response({"message": "Logout realizado com sucesso."}, status=status.HTTP_200_OK)
        
