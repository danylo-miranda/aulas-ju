# Trilha de Aprendizagem Python + Django
---
Este repositório documenta uma trilha de aprendizado completa para desenvolvimento web com Python e Django, desde os fundamentos até tópicos avançados e deploy.

📋 Estrutura da Trilha
1. Fundamentos de Python
1.1 Introdução ao Python, ambiente virtual, pip, VS Code
Configuração do ambiente de desenvolvimento

Instalação do Python e gerenciamento de versões

Uso de ambientes virtuais (venv/virtualenv)

Gerenciamento de pacotes com pip

Configuração do VS Code para desenvolvimento Python

1.2 Tipos de dados, variáveis, operadores
Tipos de dados básicos (int, float, str, bool)

Estruturas de dados (list, tuple, dict, set)

Variáveis e convenções de nomenclatura

Operadores aritméticos, comparativos e lógicos

1.3 Estruturas de controle (if, for, while)
Condicionais (if, elif, else)

Loops (for, while)

Compreensão de listas e dicionários

Controle de fluxo (break, continue, pass)

1.4 Funções e módulos
Definição e chamada de funções

Parâmetros e argumentos

Escopo de variáveis

Importação e criação de módulos

Funções lambda

1.5 POO básica (classes, herança, encapsulamento)
Classes e objetos

Métodos e atributos

Herança e polimorfismo

Encapsulamento e modificadores de acesso

Métodos especiais (init, str, etc.)

2. Introdução ao Django
2.1 Estrutura de projeto e apps
Criação de projeto Django

Estrutura de diretórios

Configuração de settings

Criação e organização de apps

Apps reutilizáveis

2.2 Models, ORM e migrações
Definição de modelos

Campos e relacionamentos

ORM do Django (consultas)

Sistema de migrações

Operações com o banco de dados

2.3 Views, URLs e Templates
Function-based views e Class-based views

Configuração de URLs

Sistema de templates

Contexto e renderização

Template tags e filters

2.4 Formulários e validação
Formulários Django

Validação de dados

ModelForms

Formulários customizados

Mensagens de erro e sucesso

2.5 Painel admin e autenticação
Customização do Django Admin

Sistema de autenticação

Permissões e grupos

Views de login/logout

Autenticação de usuários

3. Django Avançado + Boas Práticas
3.1 Estrutura de projeto modular
Arquitetura escalável

Separação de concerns

Apps modulares

Configurações por ambiente

Boas práticas de organização

3.2 Django REST Framework (API)
Criação de APIs REST

Serializers

ViewSets e Routers

Autenticação em APIs

Documentação automática

3.3 Tarefas assíncronas com Celery e Redis
Configuração do Celery

Tarefas assíncronas

Filas de mensagens

Integração com Redis

Monitoramento de tarefas

4. Controle de versão e CI/CD
4.1 Git e GitLab básico
Controle de versão com Git

Comandos essenciais

Fluxo de trabalho

GitLab/GitHub básico

Branches e merge requests

4.2 GitLab CI/CD pipelines
Configuração de CI/CD

Pipeline automation

Testes automatizados

Deploy automático

Variáveis de ambiente

4.3 Testes automáticos
Testes unitários

Testes de integração

Django Test Framework

Testes de API

Cobertura de testes

5. Contêineres com Docker
5.1 Introdução ao Docker
Conceitos de containers

Dockerfile

Imagens e containers

Docker Hub

Comandos básicos

5.2 Dockerizando um projeto Django
Configuração do Dockerfile

Multi-stage builds

Variáveis de ambiente

Volumes e dados persistentes

Otimização de imagens

5.3 Docker Compose e Redis
Orquestração com Docker Compose

Serviços múltiplos

Configuração de redes

Redis como serviço

Comunicação entre containers

5.4 Deploy com Docker + GitLab
Integração com GitLab CI/CD

Registry de imagens

Deploy em produção

Monitoramento

Logs e debugging

6. Projeto Final
Aplicação completa Django
Desenvolvimento de uma aplicação real

Integração de todos os conceitos aprendidos

Boas práticas de código

Documentação

Deploy em ambiente de produção

🚀 Começando
Pré-requisitos
Python 3.8+

Git

Editor de código (recomendado: VS Code)

Instalação
Clone o repositório:

bash
git clone [url-do-repositorio]
cd python-django-learning-track
Crie um ambiente virtual:

bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
# ou
venv\Scripts\activate  # Windows
Instale as dependências:

bash
pip install -r requirements.txt
📚 Recursos Adicionais
Documentação Oficial
Python Documentation

Django Documentation

Django REST Framework

Celery Documentation

Docker Documentation

Ferramentas Recomendadas
VS Code - Editor de código

Postman - Teste de APIs

PgAdmin - Gerenciamento de banco PostgreSQL

Redis Commander - Interface para Redis

🛠️ Tecnologias Utilizadas
Backend: Python, Django, Django REST Framework

Banco de Dados: PostgreSQL, SQLite (desenvolvimento)

Cache/Fila: Redis

Tarefas Assíncronas: Celery

Containerização: Docker, Docker Compose

CI/CD: GitLab CI/CD

Versionamento: Git

📖 Metodologia de Aprendizado
Cada tópico inclui:

📝 Teoria e conceitos fundamentais

💻 Exemplos práticos de código

🎯 Exercícios para fixação

🔍 Projetos práticos

📚 Links e recursos adicionais

🤝 Contribuindo
Contribuições são bem-vindas! Sinta-se à vontade para:

Reportar issues

Sugerir melhorias na trilha

Adicionar novos exemplos e exercícios

Corrigir erros na documentação

📄 Licença
Este projeto está sob a licença MIT. Veja o arquivo LICENSE para mais detalhes.