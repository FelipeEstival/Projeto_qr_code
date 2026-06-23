Projeto Gerador de QR Code

Este projeto é uma aplicação web desenvolvida com Django que permite aos usuários gerar QR Codes a partir de URLs fornecidas. A interface é intuitiva e o processo de geração é rápido, oferecendo a opção de baixar o QR Code gerado.

Funcionalidades

• Geração de QR Code: Converte qualquer URL em um QR Code visualmente escaneável.
• Interface Amigável: Design limpo e responsivo para uma experiência de usuário agradável.
• Download: Permite o download do QR Code gerado em formato PNG.

Tecnologias Utilizadas
O projeto foi construído utilizando as seguintes tecnologias:

Backend:
-Django: Framework web Python de alto nível para desenvolvimento rápido e design pragmático.
-Pillow: Biblioteca de processamento de imagens para Python, utilizada indiretamente pela biblioteca qrcode.
-qrcode: Biblioteca Python para gerar QR Codes.

Frontend:
-HTML5
-CSS3 (com um design moderno e responsivo)
-JavaScript (para interações assíncronas e exibição do QR Code)

Como Rodar o Projeto Localmente:

Certifique-se de ter o Python 3 e o pip instalados em sua máquina.

Rode localmente:
python manage.py runserver


Acesse a aplicação:
Abra seu navegador e navegue para http://127.0.0.1:8000/ 
(ou a porta indicada pelo Django).

Estrutura do Projeto
Plain Text

Projeto_qr_code/
├── projeto_qrcode/
│   ├── .vscode/                 # Configurações do VS Code
│   ├── projeto_qrcode_django/   # Aplicação Django principal
│   │   ├── __init__.py
│   │   ├── asgi.py
│   │   ├── settings.py          # Configurações do projeto Django
│   │   ├── urls.py              # Definições de URL do projeto
│   │   ├── views.py             # Lógica de geração do QR Code
│   │   └── wsgi.py
│   ├── templates/               # Diretório de templates HTML
│   │   └── tarefas/
│   │       └── index.html       # Frontend da aplicação
│   └── manage.py                # Utilitário de linha de comando do Django
└── README.md                    # Este arquivo



Contribuições são bem-vindas! Sinta-se à vontade para apontar problemas e sugestões
Autor Felipe Estival
