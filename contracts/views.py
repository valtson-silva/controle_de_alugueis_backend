from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Contracts
from .serializers import ContractsSerializer
from django.db.models import Q

class ContractsCreateView(APIView):
    # Registra contrato no banco de dados
    
    # Verifica se o usuário está autenticado
    permission_classes = [IsAuthenticated]
    
    def post(self, request):
        # Serializa os dados recebidos no corpo da requisição
        serializer = ContractsSerializer(data=request.data)
        if serializer.is_valid():
            # Registra o contrato no banco de dados
            serializer.save()
            # Retorna o contrato e o status 201
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            # Retorna error e o status 400
            return Response({"error": "Dados informados inválidos."}, status=status.HTTP_400_BAD_REQUEST)
        
class ContractsListView(APIView):
    # Mostra todos os contratos salvos no banco de dados
    
    # Verifica se o usuário está autenticado
    permission_classes = [IsAuthenticated]
    
    def get(self, request):
        # Obtém todos os contratos
        contracts = Contracts.objects.all()
        # Serializa todos os contratos
        serializer = ContractsSerializer(contracts, many=True)
        # Retorna todos os contratos e o status 200
        return Response(serializer.data, status=status.HTTP_200_OK)
    
class ContractsDetailView(APIView):
    # Mostra as informações de um contrato
    
    # Verifica se o usuário está autenticado
    permission_classes = [IsAuthenticated]
    
    def get(self, request, id):
        try:
            # Tenta obter o contrato pelo ID
            contract = Contracts.objects.get(id=id)
            # Serializa o contrato obtido
            serializer = ContractsSerializer(contract)
            # Retorna o contrato e o status 200
            return Response(serializer.data, status=status.HTTP_200_OK) 
        except:
            # Retorna error e o status 404
            return Response({"error": "Não existe contrato com esse ID."}, status=status.HTTP_404_NOT_FOUND)
        
class ContractsPropertiesTenantsListView(APIView):
    # Mostra os contratos relacionados com inquilinos e propriedades
    
    # Verifica se o usuário está autenticado
    permission_classes = [IsAuthenticated]
    
    def get(self, request, properties_id, tenants_id):
        try:
            # Tenta obter os contratos
            contracts = Contracts.objects.filter(
                Q(properties=properties_id) & Q(tenants=tenants_id)
            )
            # Serializa os contratos
            serializer = ContractsSerializer(contracts, many=True)
            # Retorna os contratos e o status 200
            return Response(serializer.data, status=status.HTTP_200_OK)
        except:
            # Retorna error e o status 404
            return Response({"error": "Não existe contratos com essas especificações."}, status=status.HTTP_404_NOT_FOUND)
        
class ContractsUpdateView(APIView):
    # Salva as alterações no banco de dados
    
    # Verifica se o usuário está autenticado
    permission_classes = [IsAuthenticated]
    
    def put(self, request, id):
        try:
            # Temta obter o contrato pelo ID
            contract = Contracts.objects.get(id=id)
            # Serializa o contrato com as alterações
            serializer = ContractsSerializer(contract, data=request.data)
            # Verifica se é válido
            if serializer.is_valid():
                # Salva as alterações no banco de dados
                serializer.save()
                # Retorna o contrato e o status 200
                return Response(serializer.data, status=status.HTTP_200_OK)
            else:
                # Retorna error e o status 400
                return Response({"error": "Dados informados inválidos."}, status=status.HTTP_400_BAD_REQUEST)
        except:
            # Retorna error e o status 404
            return Response({"error": "Não existe contrato com esse ID."}, status=status.HTTP_404_NOT_FOUND)
        
class ContractsDeleteView(APIView):
    # Deleta um contrato do banco de dados
    
    # Verifica se o usuário está autenticado
    permission_classes = [IsAuthenticated]
    
    def delete(self, request, id):
        try:
            # Tenta obter o contrato pelo ID
            contract = Contracts.objects.get(id=id)
            # Deleta o contrato
            contract.delete()
            # Retorna sucesso e o status 200
            return Response({"success": "Contrato deletado com sucesso."}, status=status.HTTP_200_OK)
        except:
            # Retorna error e o status 404
            return Response({"error": "Não existe um contrato com esse ID."}, status=status.HTTP_404_NOT_FOUND)