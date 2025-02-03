# Sistema back-end para controle de aluguéis

## 📖  Descrição

Este é um backend para gerenciar aluguéis de propriedades desenvolvido usando Django e Django REST Framework. O sistema permite o cadastro e gerenciamento de inquilinos, imóveis, contratos e pagamentos, além de funcionalidades avançadas como relatórios financeiros e envio de e-mails automáticos aos inquilinos sobre as datas de vencimento dos aluguéis.

<br/>

## 🛠️ Funcionalidades

- CRUD de propriedades, inquilinos, contratos e pagamentos
- Autenticação de usuários (registro, login e logout)
- Relatórios de aluguéis pagos/pendentes
- Envio automático de e-mails para lembrar inquilinos sobre vencimentos
- Testes automatizados com Pytest
<br/>

## 📡 Tecnologias utilizadas 
<div align="center"> 
<img align="left" alt="Python" height="30" width="30" src="https://s3.dualstack.us-east-2.amazonaws.com/pythondotorg-assets/media/files/python-logo-only.svg">
<img align="left" alt="Django" height="30" width="45" src="https://static.djangoproject.com/img/logos/django-logo-negative.svg">
<img align="left" alt="Postgresql" height="30" width="30" src="https://raw.githubusercontent.com/devicons/devicon/master/icons/postgresql/postgresql-original.svg">
<img align="left" alt="celery" height="32" width="35" src="https://docs.celeryq.dev/en/stable/_static/celery_512.png">
</div>
<br/><br/>

## ⏳ Inicialização

Esse projeto foi desenvolvido em ambiente Windows, utilizando as tecnologias citadas anteriormente. Sugiro que você prepare o seu ambiente seguindo os passos abaixo:

A preparação do ambiente consiste em instalar as tecnologias citadas anteriormente de acordo com seu sistema operacional.

Para instalar o Python, acesse: https://www.python.org/downloads/

Para instalar o Postgresql, acesse: https://www.postgresql.org/download/

Execute esse comando no terminal para instalar o Django e todas as bibliotecas, que estão no projeto:
```
pip install -r requirements.txt
```

Execute esse comando no terminal para rodar o pytest:
```
pytest
```

<br/>

## 🔮 Implementações futuras
1. Implementar registro automático de pagamentos e cálculo de atrasos.

2. Implementar a integração com API de pagamento.

3. Implementar sistema de multas para pagamentos atrasados.

<br/>

## 🔎 Status do Projeto

![Badge em Desenvolvimento](https://img.shields.io/badge/Status-Em%20Desenvolvimento-green)
