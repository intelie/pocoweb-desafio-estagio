# Desafio de frontend

- [Índice](#indice)
  - [Descrição do desafio](#desafio)
  - [Instalando dependências](#instale-as-dependências)
  - [Configurando ambiente](#configurando-ambiente)
  - [Rodando o projeto](#rodando-o-projeto)
  - [Ir para o desafio de backend](../backend/README.md)
  - [Rodando os testes unitários](#rodando-os-testes)

## Desafio

O desafio do frontend consistem em você editar o arquivo [Challenge.tsx](src/components/Challenge.tsx) e resolver os problemas descritos nele.

Também é obrigatório a criação de testes unitários para sua função que gera a estrutura de dados solicitada.
O projeto está configurado para usar o [vitest](https://vitest.dev/guide/) para rodar os testes.
Escrevemos um exemplo de teste [aqui](src/__tests__/exemple.spec.ts).

Você deve escrever seus testes unitários no arquivo [challenge.spec.ts](src/__tests__/challenge.spec.ts)

## Instale as dependências

```bash
yarn install # É necessário ter o node instalado e configurado para funcionar (https://nodejs.org/pt-br)
```

## Configurando ambiente

Crie um arquivo .env com base no .env-example e substitua as variáveis caso seja necessário

## Rodando o projeto

```bash
yarn dev
```

## Rodando os testes
```bash
yarn test
```