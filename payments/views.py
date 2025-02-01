from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Payments
from .serializers import PaymentsSerializer
from django.db.models import Q
from django.utils.timezone import now

class PaymentsCreateView(APIView):
    # Registra os pagamentos no banco de dados
    
    # Verifica se o usuário está autenticado
    permission_classes = [IsAuthenticated]
    
    def post(self, request):
        # Serializa os dados recebidos no corpo da requisição
        serializer = PaymentsSerializer(data=request.data)
        # Verifica se os dados enviados são válidos
        if serializer.is_valid():
            # Salva a propriedade no banco de dados
            serializer.save()
            # Retorna o pagamento e o status 201
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            # Retorna os erros e o status 400
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
class PaymentsListViews(APIView):
    # Mostra todos os pagamentos
    
    # Verifica se o usuário está autenticado
    permission_classes = [IsAuthenticated]
    
    def get(self, request):
            # Obtém todos os pagamentos
            payments = Payments.objects.all()
            # Serializa todos os pagamentos
            serializer = PaymentsSerializer(payments, many=True)
            # Retorna todos pagamentos com o status 200
            return Response(serializer.data, status=status.HTTP_200_OK)

class PaymentsDetailView(APIView):
    # Mostra as informações de um pagamento
    
    # Verifica se o usuário está autenticado
    permission_classes = [IsAuthenticated]
    
    def get(self, request, id):
        try:
            # Tenta obter o pagamento pelo ID
            payment = Payments.objects.get(id=id)
            # Serializa o pagamento obtido
            serializer = PaymentsSerializer(payment)
            # Retorna o pagamento e o status 200
            return Response(serializer.data, status=status.HTTP_200_OK)
        except:
            # Retorna error e o status 404
            return Response({"error": "Não existe pagamento com esse ID."}, status=status.HTTP_404_NOT_FOUND)
        
class PaymentsTenantsListView(APIView):
    # Mostra todos os pagamentos de um inquilino
    
    # Verifica se o usuário está autenticado
    permission_classes = [IsAuthenticated]
    
    def get(self, request, tenant_id):
        try:
            # Tenta obter todos os pagamentos relacionados a um inquilino
            payments = Payments.objects.filter(tenant=tenant_id)
            # Serializa todos os pagamentos
            serializer = PaymentsSerializer(payments, many=True)
            # Retorna todos os pagamentos obtidos e o status 200
            return Response(serializer.data, status=status.HTTP_200_OK)
        except:
            # Retorna error e o status 404
            return Response({"error": "Não existe pagamentos relacionados com esse inquilino."}, status=status.HTTP_404_NOT_FOUND)
            
class PaymentsUpdateView(APIView):
    # Atualiza as informações de um pagamento
    
    # Verifica se o usuário está autenticado
    permission_classes = [IsAuthenticated]
    
    def put(self, request, id):
        try:
            # Tenta obter o pagamento pelo ID
            payment = Payments.objects.get(id=id)
            # Serializa o pagamento obtido e as suas alterações
            serializer = PaymentsSerializer(payment, data=request.data)
            # Verifica se o pagamento é válido
            if serializer.is_valid():
                # Salva as alterações no banco de dados
                serializer.save()
                # Retorna o pagamento e o status 200
                return Response(serializer.data, status=status.HTTP_200_OK)
            else:
                # Retorna error e o status 400
                return Response({"error": "Dados Informados inválidos."}, status=status.HTTP_400_BAD_REQUEST)
        except:
            # Retorna error e o status 404
            return Response({"error": "Não existe pagamento com esse ID."}, status=status.HTTP_404_NOT_FOUND)
        
class PaymentsDeleteView(APIView):
    # Deleta um pagamento
    
    # Verifica se o usuário está autenticado
    permission_classes = [IsAuthenticated]
    
    def delete(self, request, id):
        try:
            # Tenta obter o pagamento pelo ID
            payment = Payments.objects.get(id=id)
            # Deleta o pagamento do banco de dados
            payment.delete()
            # Retorna mensagem de sucesso e o status 200
            return Response({"success": "Pagamento deletado com sucesso."}, status=status.HTTP_200_OK)
        except:
            # Retorna error e o status 404
            return Response({"error": "Não existe pagamento com esse ID."}, status=status.HTTP_404_NOT_FOUND)
        
class PayoutsReportView(APIView):
    # Mostra os relatórios de pagamentos
    
    # Verifica se o usuário está autenticado
    permission_classes = [IsAuthenticated]
    
    def get(self, request):
        # Obtém todos os pagamentos que já foram pagos
        paid = Payments.objects.filter(status="pago")
        # Obtém todos os pagamentos que estão pendentes
        pending = Payments.objects.filter(status="pendente")
        # Obtém todos os pagamentos que estão atrasados
        arrears = Payments.objects.filter(
            (Q(status="pendente") & Q(due_date__lt=now())) | Q(status="atrasado") 
        )
        # Retorna todo o relatório e o status 200
        return Response({
            "pagos": PaymentsSerializer(paid, many=True).data,
            "pendentes": PaymentsSerializer(pending, many=True).data,
            "atrasados": PaymentsSerializer(arrears, many=True).data
        }, status=status.HTTP_200_OK)
    