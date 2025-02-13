from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from .models import Tenants
from .serializers import TenantsSerializer
from rest_framework import status


class TenantsCreateView(APIView):
    # Registra os inquilinos
    
    # Verifica se o usuário está autenticado
    permission_classes = [IsAuthenticated]
    
    def post(self, request):
        
        serializer = TenantsSerializer(data=request.data)
        
        if serializer.is_valid():
            
            serializer.save()
            
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            
            return Response({"error": "Dados informados inválidos."}, status=status.HTTP_400_BAD_REQUEST)
        
class TenantsListView(APIView):
    # Mostra todos os inquilinos salvos
    
    
    permission_classes = [IsAuthenticated]
    
    def get(self, request):
        
        tenants = Tenants.objects.all()
        
        serializer = TenantsSerializer(tenants, many=True)
        
        return Response(serializer.data, status=status.HTTP_200_OK)

class TenantsDetailView(APIView):
    # Mostra as informações de um inquilino
    
    
    permission_classes = [IsAuthenticated]
    
    def get(self, request, id):
        try:
            
            tenant = Tenants.objects.get(id=id)
            
            serializer = TenantsSerializer(tenant)
            
            return Response(serializer.data, status=status.HTTP_200_OK)
        except:
            
            return Response({"error": "Não existe inquilino com esse ID."}, status=status.HTTP_404_NOT_FOUND)

class TenantsUpdateView(APIView):
    # Atualiza as informações de um inquilino
    
    
    permission_classes = [IsAuthenticated]
    
    def put(self, request, id):
        try:
            
            tenant = Tenants.objects.get(id=id)
            
            serializer = TenantsSerializer(tenant, data=request.data)
            
            if serializer.is_valid():
                
                serializer.save()
                
                return Response(serializer.data, status=status.HTTP_200_OK)
            else:
                
                return Response({"error": "Dados informados inválidos."}, status=status.HTTP_400_BAD_REQUEST)
        except:
            
            return Response({"error": "Não existe inquilino com esse ID."}, status=status.HTTP_404_NOT_FOUND)

class TenantsDeleteView(APIView):
    # Deleta um inquilino do banco de dados
    
    
    permission_classes = [IsAuthenticated]
    
    def delete(self, request, id):
        try:
            
            tenant = Tenants.objects.get(id=id)
            
            tenant.delete()
            
            return Response({"success": "Inquilino deletado com sucesso."}, status=status.HTTP_200_OK)
        except:
            
            return Response({"error": "Não existe inquilino com esse ID."}, status=status.HTTP_404_NOT_FOUND)
