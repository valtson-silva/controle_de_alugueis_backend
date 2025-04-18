from django.core.mail import EmailMessage
import pandas as pd
from celery import shared_task
from django.core.files.base import ContentFile
from io import BytesIO
from django.template.loader import render_to_string
from xhtml2pdf import pisa
from .models import Payments
from decouple import config

@shared_task
def send_report_by_email():
    # Gera o relatório PDF e o envia por email 
    
    payments = Payments.objects.all().values(
        "value", "due_date", "tenant__name", "status"
    )
    df = pd.DataFrame(payments)
    
    html_string = render_to_string("report.html", {"df": df.to_html(classes="table table-striped", index=False)})
    
    result= BytesIO()
    pisa_status = pisa.CreatePDF(html_string, dest=result)
    
    if pisa_status.err:
        return "Erro na geração do PDF"
    

    email = EmailMessage(
        subject="Relatório de Pagamentos",
        body="Segue em anexo o relatório solicitado.",
        from_email=config("EMAIL_HOST_USER"),
        to=[config("EMAIL_HOST_USER")]
    )
    email.attach("relatorio.pdf", result.getvalue(), "application/pdf")
    email.send()
    
    return "Relatório enviado com sucesso!"
    