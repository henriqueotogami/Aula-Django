# Aula Framework Django
## Bootcamp Desenvolvedor Python Full Stack
### Digital Innovation One 
[(clique aqui para ver o meu perfil na plataforma)](https://web.digitalinnovation.one/users/henrique_map)
### [Rafael Galleani](https://www.github.com/rafegal)
---------------------------------------------
### IDE: Visual Studio Code
#### Tema: Monokai Pro
#### Extensões: Code Spell Checker, GitLens, Grammarly, Markdown All in One, Python
---------------------------------------------
## Criação da Virtual Environment (Venv)
### Motivo: Isolamento das instalações de dependências neste projeto
### Etapas:
Endereço da pasta do projeto
```
C:\Users\henrique\Aula-Django>
```
- [x] Criação de virtual environment na pasta do projeto com o seguinte comando no terminal: 
```
py -m venv aula_django
```
### ou
```
python -m venv aula_django
```
- [x] Ativação da virtual environment:
```
cd .\aula_django\
```
### e depois
```
.\Scripts\activate
```
### Note que aparece no canto esquerdo do terminal o nome da virtual environment criada (aula_django)
```
(aula_django) C:\Users\henrique\Aula-Django\aula_django>
```
## Django
- [x] Instalação
```
(aula_django) C:\Users\henrique\Aula-Django\aula_django> pip install django
```
- [x] Inicialização
```
(aula_django) C:\Users\henrique\Aula-Django> django-admin startproject primeiro_projeto
```
## Python
- [x] Selecionar a versão do interpretador Python da Virtual Environment
- [x] Pressionar o atalho do VSCode CTRL + SHIFT + P e digitar "Selecionar interpretador"
### Deve aparecer a mensagem abaixo na Barra de Status do VSCode
```
Python 3.8.1 64-bit ('aula_django': venv)
```
- [x] Abrir o menu Explorador (CTRL + SHIFT + E), navegar na pasta "primeiro_projeto" e abrir o arquivo "manage.py"
- [x] Abrir o menu superior Executar, clicar em "adicionar configuração" e selecionar "Django" na janela "Select a debug configuration". Confirme o endereço "${workspaceFolder}\manage.py".
- [x] Automaticamente, abrirá um arquivo "launch.json" que o VSCode criou. Note que o argumento "runserver" está presente em "args".
-------------------------------------------------------------------------------------------------
## Depois de configurado, siga a etapa abaixo no terminal
### obs: ainda não consegui configurar os arquivos de debug JSON para fazer isso automaticamente

```
C:\Users\henrique\Aula-Django> cd.\aula_django

C:\Users\henrique\Aula-Django\aula_django> .\Scripts\activate

(aula_django) C:\Users\henrique\Aula-Django\aula_django> cd..

(aula_django) C:\Users\henrique\Aula-Django> cd.\primeiro_projeto

(aula_django) C:\Users\henrique\Aula-Django\primeiro_projeto> py manage.py runserver
Watching for file changes with StatReloader
Performing system checks...

System check identified no issues (0 silenced).

You have 18 unapplied migration(s). Your project may not work properly until you apply the migrations for app(s): admin, auth, contenttypes, sessions.
Run 'python manage.py migrate' to apply them.
August 28, 2020 - 18:20:01
Django version 3.1, using settings 'primeiro_projeto.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CTRL-BREAK.
```
 
### Após ativar a Virtual Environment, iremos criar um "core" para a aplicação

```
(aula_django) C:\Users\henrique\Aula-Django> django-admin startapp core
```

### Adicionar "core" ao arquivo settings.py que está na pasta ```C:\Users\Henrique\Aula-Django\primeiro_projeto``` em "Installed_Apps"

### Criar uma nova rota no arquivo urls.py que está na pasta ```C:\Users\Henrique\Aula-Django\primeiro_projeto``` em urlpatterns e importar ```from core import views```

### Criar uma nova função "hello" e importar "HttpResponse" no arquivo views.py que está na pasta ```C:\Users\Henrique\Aula-Django\primeiro_projeto\core```

```
def hello(request):
    return HttpResponse('Hello world')
```

-----------------------------------------------------------------------------------------
## Henrique Matheus Alves Pereira