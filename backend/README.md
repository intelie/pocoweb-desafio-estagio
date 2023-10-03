# Desafio de backend

- [Índice](#indice)
  - [Descrição do desafio](#desafio)
  - [Configurando ambiente](#crie-um-ambiente-virtual-para-isolar-localmente-nossas-dependências)
  - [Instalando dependências](#instale-as-dependências)
  - [Executando migrações](#execute-as-migrações)
  - [Carregando dados iniciais](#carregue-os-dados-iniciais)
  - [Criando um usuário admin](#crie-um-usuário-admin)
  - [Rodando o projeto](#rodando-o-projeto)
  - [Ir para o desafio de frontend](../frontend/README.md)

## Desafio

O desafio de backend consiste em resolver os problemas descritos nesse arquivo [Views.py](explorer/views.py)


## Crie um ambiente virtual para isolar localmente nossas dependências

```bash
python3 -m venv env

source env/bin/activate  # On Windows use "env\Scripts\activate"
```

## Instale as dependências

```bash
pip install -r requirements.txt
```

## Execute as migrações

```bash
python manage.py migrate
```

## Carregue os dados iniciais

```bash
python manage.py loaddata explorer
```

## Crie um usuário admin

```bash
python manage.py createsuperuser --email admin@example.com --username admin
```

## Rodando o projeto

```bash
python manage.py runserver
```
