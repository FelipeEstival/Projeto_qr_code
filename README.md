# QR Code Generator

Aplicação web desenvolvida com Django para gerar QR Codes a partir de URLs. O sistema permite criar códigos QR de forma rápida e simples, com opção de visualização e download da imagem gerada.

---

## Você pode acessar

Teste você mesmo a ferramenta
https://felipeestival.pythonanywhere.com/qrcode/

---

## Funcionalidades

* Geração instantânea de QR Codes a partir de URLs
* Visualização do QR Code diretamente na página
* Download da imagem em formato PNG
* Interface responsiva e intuitiva
* Validação básica de entrada

---

## Tecnologias Utilizadas

### Backend

* Python
* Django
* qrcode
* Pillow

### Frontend

* HTML5
* CSS3
* JavaScript

---

## Instalação

Clone o repositório:

```bash
git clone https://github.com/seu-usuario/projeto-qrcode.git
```

Acesse a pasta do projeto:

```bash
cd projeto-qrcode
```

Instale as dependências:

```bash
pip install -r requirements.txt
```

Inicie o servidor:

```bash
python manage.py runserver
```

---

## Acesso

Após iniciar o servidor, abra:

```text
http://127.0.0.1:8000/qrcode
```

---

## Estrutura do Projeto

```text
Projeto_qr_code/
│
├── projeto_qrcode/
│   ├── projeto_qrcode_django/
│   │   ├── settings.py
│   │   ├── urls.py
│   │   ├── views.py
│   │   └── ...
│   │
│   ├── templates/
│   │   └── tarefas/
│   │       └── index.html
│   │
│   └── manage.py
│
└── README.md
```

---

## Contribuição

Contribuições são bem-vindas. Caso encontre algum problema ou tenha sugestões de melhoria, abra uma issue ou envie um pull request.

---

## Autor

**Felipe Estival**

Desenvolvido como projeto de estudos utilizando Django, Python e desenvolvimento web.
