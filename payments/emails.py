from django.core.mail import send_mail
from django.utils.timezone import now
from datetime import timedelta
from .models import Payments
from django.db.models import Q
from decouple import config

def send_email_reminder():
    # Envia emails para os inquilinos sobre pagamentos próximos
    
    limit_date = now().date() + timedelta(days=3)
    
    # Obtém os pagamentos pendentes
    pending_payments = Payments.objects.filter(
        Q(status="pendente") & Q(due_date__lte=limit_date)
    )
    
    # Itera sobre os pagamentos pendentes
    for payment in pending_payments:
        tenant_email = payment.tenant.email
        message = f"Olá, {payment.tenant.name},\nSeu aluguel vence em {payment.due_date},\nPor favor realize o pagamento o mais rápido possível. Obrigado."
        
        # Envia o email
        send_mail(
            "Lembrete de Vencimento do Aluguel",
            message,
            config('EMAIL_HOST_USER'),
            [tenant_email],
            fail_silently=False
        )
    