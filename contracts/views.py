from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Contracts
from .serializers import ContractsSerializer
from django.db.models import Q

class ContractsCreateView(APIView):
    # Registra contrato no banco de dados
    
    permission_classes = [IsAuthenticated]
    
    def post(self, request):
        serializer = ContractsSerializer(data=request.data)
        
        if serializer.is_valid():
            serializer.save()
            
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response({"error": "Dados informados inválidos."}, status=status.HTTP_400_BAD_REQUEST)
        
class ContractsListView(APIView):
    # Mostra todos os contratos salvos no banco de dados
    
    permission_classes = [IsAuthenticated]
    
    def get(self, request):
        contracts = Contracts.objects.all()
        serializer = ContractsSerializer(contracts, many=True)
        
        return Response(serializer.data, status=status.HTTP_200_OK)
    
class ContractsDetailView(APIView):
    # Mostra as informações de um contrato
    
    permission_classes = [IsAuthenticated]
    
    def get(self, request, id):
        try:
            contract = Contracts.objects.get(id=id)
            serializer = ContractsSerializer(contract)
            return Response(serializer.data, status=status.HTTP_200_OK) 
        except:
            return Response({"error": "Não existe contrato com esse ID."}, status=status.HTTP_404_NOT_FOUND)
        
class ContractsPropertiesTenantsListView(APIView):
    # Mostra os contratos relacionados com inquilinos e propriedades
    
    permission_classes = [IsAuthenticated]
    
    def get(self, request, properties_id, tenants_id):
        try:
            contracts = Contracts.objects.filter(
                Q(properties=properties_id) & Q(tenants=tenants_id)
            )
            
            serializer = ContractsSerializer(contracts, many=True)
            
            return Response(serializer.data, status=status.HTTP_200_OK)
        except:
            return Response({"error": "Não existe contratos com essas especificações."}, status=status.HTTP_404_NOT_FOUND)
        
class ContractsUpdateView(APIView):
    # Salva as alterações no banco de dados
    
    permission_classes = [IsAuthenticated]
    
    def put(self, request, id):
        try:
            contract = Contracts.objects.get(id=id)
            serializer = ContractsSerializer(contract, data=request.data)
            
            if serializer.is_valid():
                serializer.save()
                
                return Response(serializer.data, status=status.HTTP_200_OK)
            else:
                return Response({"error": "Dados informados inválidos."}, status=status.HTTP_400_BAD_REQUEST)
        except:
            return Response({"error": "Não existe contrato com esse ID."}, status=status.HTTP_404_NOT_FOUND)
        
class ContractsDeleteView(APIView):
    # Deleta um contrato do banco de dados
    
    permission_classes = [IsAuthenticated]
    
    def delete(self, request, id):
        try:
            contract = Contracts.objects.get(id=id)
            contract.delete()
            
            return Response({"success": "Contrato deletado com sucesso."}, status=status.HTTP_200_OK)
        except:
            return Response({"error": "Não existe um contrato com esse ID."}, status=status.HTTP_404_NOT_FOUND)
