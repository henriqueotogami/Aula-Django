# Aula Framework Django

> Repositório do projeto desenvolvido no Bootcamp Desenvolvedor Full Stack Python (Digital Innovation One), cobrindo configuração inicial do Django, "Hello World" e o desenvolvimento de uma Agenda de Eventos.

## 📋 Sobre o Projeto

Este projeto reúne o material da aula de Framework Django do Bootcamp Desenvolvedor Full Stack Python. A aula foi dividida em duas partes: a primeira trata da configuração do ambiente (virtual environment, Django, VS Code) e de um primeiro exemplo "Hello World" no navegador; a segunda aborda o desenvolvimento de uma **Agenda de Eventos** com autenticação, CRUD de eventos e integração com o admin do Django.

**Instrutor:** [Rafael Galleani](https://www.github.com/rafegal)  
**Plataforma:** [Digital Innovation One](https://web.digitalinnovation.one/users/henrique_map)

## 📁 Estrutura do Projeto

### Projeto Django (`primeiro_projeto/`)
- **primeiro_projeto/** – Configurações do projeto (URLs, settings, WSGI/ASGI)
- **core/** – App principal com views (ex.: hello world) e estrutura para a Agenda de Eventos
- **manage.py** – Script de gerenciamento do Django

### Documentação
- **Configuration-steps.md** – Passo a passo detalhado de configuração (venv, Django, VS Code)
- **README.md** – Este arquivo

## 📂 Estrutura do repositório

```
README.md
Configuration-steps.md
aula_django/              # Virtual environment (venv)
primeiro_projeto/
  manage.py               # CLI do Django
  primeiro_projeto/       # Pacote do projeto
    __init__.py
    settings.py           # Configurações do projeto
    urls.py               # Rotas principais (admin, hello)
    wsgi.py
    asgi.py
  core/                   # App "core"
    __init__.py
    admin.py
    apps.py
    models.py
    views.py              # View hello(request, nome)
    tests.py
```

## 🛠️ Tecnologias Utilizadas

- **Python** – Linguagem de programação
- **Django** – Framework web (versão 3.1)
- **SQLite** – Banco de dados padrão do projeto
- **VS Code** – Editor (com extensões: Python, GitLens, Error Lens, etc.)
- **Tema sugerido:** Monokai Pro

## 📝 Funcionalidades Principais

### Parte 1 – Configuração e Hello World
- Servidor de desenvolvimento Django rodando localmente
- Rota dinâmica `hello/<nome>/` que exibe "Hello world" com o nome informado
- Ambiente isolado com virtual environment (venv)

### Parte 2 – Agenda de Eventos (escopo da aula)
- Tela de administrador para gerenciar usuários e eventos
- Autenticação de usuários (login/logout)
- Lista de eventos cadastrados após login
- Editar e excluir evento (somente do usuário logado)
- Evento: título, data, hora, descrição
- Eventos a menos de uma hora de vencer indicados em vermelho
- Eventos vencidos arquivados (não listados)
- Endpoint JSON com dados dos eventos por usuário
- Página de erro 404 customizada
- Configuração de time zone

## 🚀 Como Executar

### Pré-requisitos
- Python 3.8+
- Pip

### Passos

1. **Clone o repositório** (se ainda não tiver):
   ```bash
   git clone https://github.com/HenriqueMAP/Aula-Django.git
   cd Aula-Django
   ```

2. **Crie e ative o ambiente virtual:**
   ```bash
   # Criar
   python -m venv aula_django

   # Ativar (Linux/macOS)
   source aula_django/bin/activate

   # Ativar (Windows)
   .\aula_django\Scripts\activate
   ```

3. **Instale o Django:**
   ```bash
   pip install django
   ```

4. **Entre na pasta do projeto e rode o servidor:**
   ```bash
   cd primeiro_projeto
   python manage.py migrate
   python manage.py runserver
   ```

5. **Acesse no navegador:**
   - Admin: http://127.0.0.1:8000/admin/
   - Hello World: http://127.0.0.1:8000/hello/SeuNome/

Para um guia mais detalhado (incluindo configuração do VS Code e criação do app `core`), consulte [Configuration-steps.md](Configuration-steps.md).

## 📚 Conteúdos Abordados

- ✅ Virtual environment (venv) e isolamento de dependências
- ✅ Instalação e inicialização do Django (`startproject`, `startapp`)
- ✅ Estrutura de um projeto Django (settings, urls, apps)
- ✅ Views e URLs (rotas dinâmicas com parâmetros)
- ✅ Admin do Django e modelos
- ✅ Autenticação e sessões
- ✅ CRUD de eventos e regras de negócio (eventos vencidos, alertas)
- ✅ Templates e time zone
- ✅ API JSON e tratamento de erros (404)

## ⚙️ Como Funciona

### Hello World
A rota `hello/<nome>/` em `primeiro_projeto/urls.py` chama a view `core.views.hello`. A view recebe o parâmetro `nome` e retorna uma `HttpResponse` com a mensagem "Hello world" seguida do nome.

### Configuração
O arquivo [Configuration-steps.md](Configuration-steps.md) descreve a criação do venv, instalação do Django, criação do projeto `primeiro_projeto`, criação do app `core`, configuração do interpretador Python no VS Code e uso de `launch.json` para depuração do servidor Django.

## 📄 Licença

Este projeto está disponível para fins de estudo. Consulte o repositório e a plataforma Digital Innovation One para condições de uso do material do bootcamp.

## 📖 Referências

- [Documentação oficial do Django](https://docs.djangoproject.com/)
- [Configuration-steps.md](Configuration-steps.md) – Etapas de configuração deste projeto
- Código-fonte em `primeiro_projeto/` e `core/`

---

**Desenvolvido por:** Henrique Matheus Alves Pereira

### Hashtags
#Django #Python #FullStack #WebDevelopment #Bootcamp #DigitalInnovationOne #Backend #AgendaDeEventos #Learning #OpenSource #GitHub

### Meta Keywords
```
Django, Python, framework web, bootcamp, full stack, agenda de eventos,
Digital Innovation One, venv, virtual environment, configuração Django,
hello world, autenticação, CRUD, admin Django, backend, desenvolvimento web
```
