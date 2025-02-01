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
        # Serializa os dados enviados no corpo da requisição
        serializer = TenantsSerializer(data=request.data)
        # Verifica se os dados são válidos
        if serializer.is_valid():
            # Salva o inquilino no banco de dados
            serializer.save()
            # Retorna o inquilino e status 201
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            # Retorna error e o status 400
            return Response({"error": "Dados informados inválidos."}, status=status.HTTP_400_BAD_REQUEST)
        
class TenantsListView(APIView):
    # Mostra todos os inquilinos salvos
    
     # Verifica se o usuário está autenticado
    permission_classes = [IsAuthenticated]
    
    def get(self, request):
        # Obtém todos inquilinos salvos no banco de dados
        tenants = Tenants.objects.all()
        # Serializa todos os inquilinos obtidos
        serializer = TenantsSerializer(tenants, many=True)
        # Retorna todos os inquilinos e o status 200
        return Response(serializer.data, status=status.HTTP_200_OK)

class TenantsDetailView(APIView):
    # Mostra as informações de um inquilino
    
    # Verifica se o usuário está autenticado
    permission_classes = [IsAuthenticated]
    
    def get(self, request, id):
        try:
            # Tenta obter o inquilino pelo ID
            tenant = Tenants.objects.get(id=id)
            # Serializa o inquilino obtido
            serializer = TenantsSerializer(tenant)
            # Retorna o inquilino e o status 200
            return Response(serializer.data, status=status.HTTP_200_OK)
        except:
            # Retorna error e o status 404
            return Response({"error": "Não existe inquilino com esse ID."}, status=status.HTTP_404_NOT_FOUND)

class TenantsUpdateView(APIView):
    # Atualiza as informações de um inquilino
    
    # Verifica se o usuário está autenticado
    permission_classes = [IsAuthenticated]
    
    def put(self, request, id):
        try:
            # Tenta obter o inquilino pelo ID
            tenant = Tenants.objects.get(id=id)
            # Serializa o inquilino com suas alterações
            serializer = TenantsSerializer(tenant, data=request.data)
            # Verifica se os dados são válidos
            if serializer.is_valid():
                # Salva as alterações
                serializer.save()
                # Retorna o inquilino e o status 200
                return Response(serializer.data, status=status.HTTP_200_OK)
            else:
                # Retorna error e o status 400
                return Response({"error": "Dados informados inválidos."}, status=status.HTTP_400_BAD_REQUEST)
        except:
            # Retorna error e o status 404
            return Response({"error": "Não existe inquilino com esse ID."}, status=status.HTTP_404_NOT_FOUND)

class TenantsDeleteView(APIView):
    # Deleta um inquilino do banco de dados
    
    # Verifica se o usuário está autenticado
    permission_classes = [IsAuthenticated]
    
    def delete(self, request, id):
        try:
            # Tenta obter o inquilino pelo ID
            tenant = Tenants.objects.get(id=id)
            # Deleta o inquilino do banco de dados
            tenant.delete()
            # Retorna sucesso e o status 200
            return Response({"success": "Inquilino deletado com sucesso."}, status=status.HTTP_200_OK)
        except:
            # Retorna error e o status 404
            return Response({"error": "Não existe inquilino com esse ID."}, status=status.HTTP_404_NOT_FOUND)