# 🍽️ Sistema de Receitas com Django
 
> Aplicação web completa para gerenciamento de receitas, com autenticação de usuários, CRUD completo, sistema de tags e arquitetura modular.
 
---
 
## 📋 Índice
 
- [Sobre o Projeto](#-sobre-o-projeto)
- [Funcionalidades](#-funcionalidades)
- [Estrutura do Projeto](#-estrutura-do-projeto)
- [Tecnologias Utilizadas](#-tecnologias-utilizadas)
- [Como Executar](#-como-executar)
- [Apps do Sistema](#-apps-do-sistema)
- [Arquitetura e Boas Práticas](#-arquitetura-e-boas-práticas)
- [Testes](#-testes)
- [Banco de Dados](#-banco-de-dados)
 
---
 
## 📖 Sobre o Projeto
 
Este projeto é uma aplicação web desenvolvida com **Django**, que implementa um sistema completo de receitas. O objetivo é consolidar boas práticas de desenvolvimento web com Python, incluindo autenticação, modularização de código, templates reutilizáveis e testes automatizados.
 
---
 
## ✅ Funcionalidades
 
- 🔐 **Autenticação completa** — registro, login e logout de usuários
- 📋 **CRUD de receitas** — criar, listar, visualizar, editar e excluir
- 🏷️ **Sistema de tags** — categorize e filtre receitas por tags
- 👤 **Perfil de usuário** — área autenticada com dashboard pessoal
- 📄 **Paginação** — listagem otimizada de receitas
- 💬 **Feedback ao usuário** — mensagens de validação e confirmação
- 🔒 **Rotas protegidas** — acesso restrito para usuários autenticados
 
---
 
## 🗂️ Estrutura do Projeto
 
```
projeto1/
│
├── authors/              # Autenticação e gerenciamento de usuários
│   ├── forms/
│   │   ├── login.py
│   │   └── register_form.py
│   ├── views/
│   ├── templates/
│   ├── tests/
│   └── signals.py
│
├── recipes/              # App principal — lógica de receitas
│   ├── forms/
│   │   └── recipe_form.py
│   ├── views/
│   ├── templates/
│   └── tests/
│
├── tag/                  # Sistema de tags
│
├── base_templates/       # Templates base reutilizáveis
│   └── templates/
│       ├── base.html
│       ├── pages/
│       │   ├── home.html
│       │   ├── recipe_detail.html
│       │   ├── dashboard.html
│       │   └── login/register
│       └── partials/
│           ├── header.html
│           ├── footer.html
│           └── ...
│
├── static/               # Arquivos estáticos (CSS, imagens)
│
├── db.sqlite3
├── manage.py
└── settings.py
```
 
---
 
## 🛠️ Tecnologias Utilizadas
 
| Tecnologia | Uso |
|-----------|-----|
| **Python 3.x** | Linguagem principal |
| **Django** | Framework web |
| **SQLite** | Banco de dados (desenvolvimento) |
| **pytest** | Testes automatizados |
| **HTML / CSS** | Templates e estilização |
 
---
 
## 🚀 Como Executar
 
### Pré-requisitos
 
- Python 3.10+
- pip
- Virtualenv (recomendado)
 
### Passo a passo
 
```bash
# 1. Clone o repositório
git clone https://github.com/seu-usuario/seu-repositorio.git
cd seu-repositorio
 
# 2. Crie e ative um ambiente virtual
python -m venv venv
source venv/bin/activate        # Linux/macOS
venv\Scripts\activate           # Windows
 
# 3. Instale as dependências
pip install -r requirements.txt
 
# 4. Aplique as migrações
python manage.py migrate
 
# 5. Crie um superusuário (opcional)
python manage.py createsuperuser
 
# 6. Inicie o servidor de desenvolvimento
python manage.py runserver
```
 
Acesse em: [http://127.0.0.1:8000](http://127.0.0.1:8000)
 
---
 
## 🧩 Apps do Sistema
 
### 👤 `authors` — Usuários e Autenticação
 
Responsável por toda a gestão de usuários da plataforma.
 
- Registro e login de novos usuários
- Logout seguro
- Perfil de usuário
- Dashboard com área autenticada
- **Signals** para automações pós-criação de usuário
- Formulários separados por responsabilidade (`login.py`, `register_form.py`)
 
---
 
### 🍽️ `recipes` — Receitas
 
App principal do sistema, contendo toda a lógica de receitas.
 
- Listagem com paginação
- Visualização detalhada de cada receita
- Criação, edição e exclusão
- Controle de publicação (rascunho / publicado)
- Relacionamento com autor e tags
- Formulário dedicado (`recipe_form.py`)
 
---
 
### 🏷️ `tag` — Tags
 
Módulo responsável por categorizar e organizar receitas.
 
- Criação de tags
- Associação com receitas (relação Many-to-Many)
- Filtro de receitas por tag
 
---
 
## 🏛️ Arquitetura e Boas Práticas
 
- **Separação por apps** — cada domínio possui seu próprio app Django
- **Views organizadas** — múltiplos arquivos ao invés de views monolíticas
- **Formulários centralizados** — validação e reutilização de forms por responsabilidade
- **Templates com herança** — `base.html` com partials reutilizáveis (`header`, `footer`, componentes)
- **Signals Django** — automações desacopladas do fluxo principal
- **Código limpo e legível** — seguindo princípios de manutenibilidade
 
---
 
## 🧪 Testes
 
Testes automatizados implementados com **pytest**.
 
```bash
# Executar todos os testes
pytest
 
# Executar testes com detalhes
pytest -v
 
# Executar testes de um app específico
pytest authors/tests/
pytest recipes/tests/
```
 
**O que é testado:**
- Validação de formulários
- Regras de negócio
- Comportamento das views
- Integridade dos dados
 
---
 
## 🗄️ Banco de Dados
 
### Principais relações
 
```
User (1) ──────────── (N) Recipe
                            │
                            │ (N)
                           Tag (M)
```
 
| Relação | Tipo |
|--------|------|
| Usuário → Receitas | One-to-Many |
| Receita → Tags | Many-to-Many |
 
---
 
## 📚 Aprendizados Consolidados
 
Este projeto cobre na prática:
 
- ✅ Arquitetura modular com apps separados
- ✅ Sistema completo de autenticação Django
- ✅ CRUD com boas práticas
- ✅ Relacionamentos no banco de dados (FK e M2M)
- ✅ Templates dinâmicos com herança e componentização
- ✅ Paginação de dados
- ✅ Organização profissional de código
- ✅ Testes automatizados com pytest
- ✅ Django Signals