from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Properties
from .serializers import PropertiesSerializer

class PropertiesCreateView(APIView):
    # Registra uma propriedade no banco de dados

    
    # Verifica se o usuário está autenticado
    permission_classes = [IsAuthenticated]
    
    def post(self, request):
        
        serializer = PropertiesSerializer(data=request.data)
        
        if serializer.is_valid():
            
            serializer.save()
            
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
class PropertiesListView(APIView):
    # Mostra todas as propriedades


    permission_classes = [IsAuthenticated]
    
    def get(self, request):
            
            properties = Properties.objects.all()
            
            serializer = PropertiesSerializer(properties, many=True)
            
            return Response(serializer.data, status=status.HTTP_200_OK)
        
class PropertiesDetailView(APIView):
    # Mostra os detalhes de uma propriedade

    
    permission_classes = [IsAuthenticated]
    
    def get(self, request, id):
        try:
            
            estate = Properties.objects.get(id=id)
            
            serializer = PropertiesSerializer(estate)
            
            return Response(serializer.data, status=status.HTTP_200_OK)
        except:
            
            return Response({"error": "Não existe propriedade com esse ID."}, status=status.HTTP_404_NOT_FOUND)
        
class PropertiesUpdateView(APIView):
    # Atualiza as informações de uma propriedade
    
    
    permission_classes = [IsAuthenticated]
    
    def put(self, request, id):
        try:
            
            estate = Properties.objects.get(id=id)
            
            serializer = PropertiesSerializer(estate, data=request.data)
            
            if serializer.is_valid():
                
                serializer.save()
                
                return Response(serializer.data, status=status.HTTP_200_OK)
            else:
                
                return Response({"error": "Dados informados inválidos."}, status=status.HTTP_400_BAD_REQUEST)
        except:
            return Response({"error": "Não existe propriedade com esse ID."}, status=status.HTTP_404_NOT_FOUND)
        
        
class PropertiesDeleteView(APIView):
    # Deleta a propriedade do banco de dados
    
    
    permission_classes = [IsAuthenticated]
    
    def delete(self, request, id):
        try:
             
            estate = Properties.objects.get(id=id)
            
            estate.delete()
            
            return Response({"success": "Propriedade deletada com sucesso."}, status=status.HTTP_200_OK)
        except:
            
            Response({"error": "Não existe propriedade com esse ID."}, status=status.HTTP_404_NOT_FOUND)
