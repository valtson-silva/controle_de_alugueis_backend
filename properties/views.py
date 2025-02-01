from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Properties
from .serializers import PropertiesSerializer

class PropertiesCreateView(APIView):
    # Verifica se o usuário está autenticado
    permission_classes = [IsAuthenticated]
    
    def post(self, request):
        # Serializa os dados recebidos no corpo da requisição
        serializer = PropertiesSerializer(data=request.data)
        # Verifica se os dados enviados são válidos
        if serializer.is_valid():
            # Salva a propriedade no banco de dados
            serializer.save()
            # Retorna a propriedade e o status 201
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            # Retorna os erros e o status 400
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
class PropertiesListView(APIView):
    # Verifica se o usuário está autenticado
    permission_classes = [IsAuthenticated]
    
    def get(self, request):
            # Obtém todas as propriedades
            properties = Properties.objects.all()
            # Serializa todas as propriedades
            serializer = PropertiesSerializer(properties, many=True)
            # Retorna todas as propriedade com o status 200
            return Response(serializer.data, status=status.HTTP_200_OK)
        
class PropertiesDetailView(APIView):
    # Verifica se o usuário está autenticado
    permission_classes = [IsAuthenticated]
    
    def get(self, request, id):
        try:
            # Tenta obter a propriedade pelo ID
            estate = Properties.objects.get(id=id)
            # Serializa a propriedade obtida
            serializer = PropertiesSerializer(estate)
            # Retorna a propriedade e o status 200
            return Response(serializer.data, status=status.HTTP_200_OK)
        except:
            # Retorna error e o status 404
            return Response({"error": "Não existe propriedade com esse ID."}, status=status.HTTP_404_NOT_FOUND)
        
class PropertiesUpdateView(APIView):
    # Verifica se o usuário está autenticado
    permission_classes = [IsAuthenticated]
    
    def put(self, request, id):
        try:
            # Tenta obter a propriedade pelo ID
            estate = Properties.objects.get(id=id)
            # Serializa os dados recebidos no corpo da requisição
            serializer = PropertiesSerializer(estate, data=request.data)
            # Verifica se os dados enviados são válidos
            if serializer.is_valid():
                # Salva as alterações no banco de dados
                serializer.save()
                # Retorna a propriedade e o status 200
                return Response(serializer.data, status=status.HTTP_200_OK)
            else:
                # Retorna error e o status 400
                return Response({"error": "Dados informados inválidos."}, status=status.HTTP_400_BAD_REQUEST)
        except:
            return Response({"error": "Não existe propriedade com esse ID."}, status=status.HTTP_404_NOT_FOUND)
        
        
class PropertiesDeleteView(APIView):
    # Verifica se o usuário está autenticado
    permission_classes = [IsAuthenticated]
    
    def delete(self, request, id):
        try:
             # Tenta obter a propriedade pelo ID
            estate = Properties.objects.get(id=id)
            # Deleta a propriedade do banco de dados
            estate.delete()
            # Retorna sucesso e o status 200
            return Response({"success": "Propriedade deletada com sucesso."}, status=status.HTTP_200_OK)
        except:
            # Retorna error e o status 404
            Response({"error": "Não existe propriedade com esse ID."}, status=status.HTTP_404_NOT_FOUND)
