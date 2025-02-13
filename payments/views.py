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
        
        serializer = PaymentsSerializer(data=request.data)
        
        if serializer.is_valid():
            
            serializer.save()
            
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
class PaymentsListViews(APIView):
    # Mostra todos os pagamentos
    
    
    permission_classes = [IsAuthenticated]
    
    def get(self, request):
            
            payments = Payments.objects.all()
            
            serializer = PaymentsSerializer(payments, many=True)
            
            return Response(serializer.data, status=status.HTTP_200_OK)

class PaymentsDetailView(APIView):
    # Mostra as informações de um pagamento
    
    
    permission_classes = [IsAuthenticated]
    
    def get(self, request, id):
        try:
            
            payment = Payments.objects.get(id=id)
            
            serializer = PaymentsSerializer(payment)
            
            return Response(serializer.data, status=status.HTTP_200_OK)
        except:
            
            return Response({"error": "Não existe pagamento com esse ID."}, status=status.HTTP_404_NOT_FOUND)
        
class PaymentsTenantsListView(APIView):
    # Mostra todos os pagamentos de um inquilino
    
    
    permission_classes = [IsAuthenticated]
    
    def get(self, request, tenant_id):
        try:
            # Tenta obter todos os pagamentos relacionados a um inquilino
            payments = Payments.objects.filter(tenant=tenant_id)
            
            serializer = PaymentsSerializer(payments, many=True)
            
            return Response(serializer.data, status=status.HTTP_200_OK)
        except:
            
            return Response({"error": "Não existe pagamentos relacionados com esse inquilino."}, status=status.HTTP_404_NOT_FOUND)
            
class PaymentsUpdateView(APIView):
    # Atualiza as informações de um pagamento
    
    
    permission_classes = [IsAuthenticated]
    
    def put(self, request, id):
        try:
            
            payment = Payments.objects.get(id=id)
            
            serializer = PaymentsSerializer(payment, data=request.data)
            
            if serializer.is_valid():
                
                serializer.save()
                
                return Response(serializer.data, status=status.HTTP_200_OK)
            else:
                
                return Response({"error": "Dados Informados inválidos."}, status=status.HTTP_400_BAD_REQUEST)
        except:
            
            return Response({"error": "Não existe pagamento com esse ID."}, status=status.HTTP_404_NOT_FOUND)
        
class PaymentsDeleteView(APIView):
    # Deleta um pagamento
    
    
    permission_classes = [IsAuthenticated]
    
    def delete(self, request, id):
        try:
            
            payment = Payments.objects.get(id=id)
            
            payment.delete()
            
            return Response({"success": "Pagamento deletado com sucesso."}, status=status.HTTP_200_OK)
        except:
            
            return Response({"error": "Não existe pagamento com esse ID."}, status=status.HTTP_404_NOT_FOUND)
        
class PayoutsReportView(APIView):
    # Mostra os relatórios de pagamentos
    
    
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
    
