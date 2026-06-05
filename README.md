# Automação de Testes com Playwright

## Descrição

Projeto desenvolvido para estudos de automação de testes utilizando Python, Pytest e Playwright.

## Tecnologias Utilizadas

- Python
- Playwright
- Pytest

## Funcionalidades

- Abertura de navegador
- Navegação entre páginas
- Localização de elementos
- Preenchimento de formulários
- Cliques em botões
- Validações de elementos
- Manipulação de abas

## Estrutura

```text
tests/
README.md
requirements.txt
```

## Instalação

Criar ambiente virtual:

```bash
python -m venv venv
```

Ativar ambiente virtual:

```bash
venv\Scripts\activate
```

Instalar dependências:

```bash
pip install -r requirements.txt
```

Instalar navegadores:

```bash
playwright install
```

## Executar Testes

Todos os testes:

```bash
pytest
```

Um único teste:

```bash
pytest tests/test_login.py -v
```

## Autor

Adalberto Campos Junior
