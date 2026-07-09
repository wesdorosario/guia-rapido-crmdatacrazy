# Base de Conhecimento do Projeto

Este documento é a base de conhecimento para outras IAs ou servidores de contexto trabalharem neste projeto de documentação de APIs.

## Objetivo do projeto

Criar guias de integração de APIs de WhatsApp ao CRM DataCrazy, organizados por pasta de API. Cada guia deve conter:

- documentação técnica passo a passo
- imagens de apoio
- navegação clara entre o menu principal e os guias por API
- HTML limpo e responsivo

## Estrutura do projeto

```
Doc CRMDataCrazy/
├── index.html
├── README.md
├── KNOWLEDGE_BASE.md
├── write_formatted_guia.py
├── css/
│   └── styles.css          # CSS global compartilhado por todas as páginas
├── js/                     # Pasta para scripts JavaScript (futura)
├── assets/                 # Pasta para assets globais (futura)
├── reference/              # Pasta para arquivos de referência (HTML e imagens)
│   └── (arquivos temporários para criação de novos guias)
├── molde-api/              # Template para novos guias de API
│   ├── index.html
│   └── images/
├── Uazapi/
│   ├── uazapi.html
│   └── images/
│       ├── image1.png
│       ├── image2.png
│       └── ...
└── .venv/
```

### Arquivos principais

- `index.html`
  - menu principal do projeto.
  - lista as APIs disponíveis e direciona para cada guia específico.
  - usa CSS global com classe `home-page`.

- `css/styles.css`
  - arquivo CSS global compartilhado por todas as páginas.
  - contém variáveis CSS para cores, espaçamentos, bordas, sombras.
  - estilos específicos para página principal (`.home-page`) e guias de API (`.api-guide`).
  - facilita manutenção e consistência visual.

- `README.md`
  - explica a estrutura geral e como gerar novos guias.

- `KNOWLEDGE_BASE.md`
  - base de conhecimento destinada a IAs e servidores de contexto.
  - descreve o fluxo de trabalho e as convenções do projeto.

- `write_formatted_guia.py`
  - script Python utilizado para gerar o HTML final do guia Uazapi.
  - grava o arquivo em `Uazapi/uazapi.html`.
  - pode ser usado como modelo para outros guias de API.

- `molde-api/`
  - pasta modelo para gerar novos guias de API.
  - contém `index.html` com estrutura pronta de guia e seção de vídeo embed.
  - usa CSS global com classe `api-guide`.
  - contém `images/` vazia para armazenar imagens da nova API.

- `js/`
  - pasta reservada para scripts JavaScript (uso futuro).

- `assets/`
  - pasta reservada para assets globais (uso futuro).

- `reference/`
  - pasta para arquivos de referência temporários (HTML e imagens).
  - usada para receber os arquivos de nova API antes de criar o guia final.
  - após criar o guia, os arquivos podem ser removidos desta pasta.

- `tmp_extract_body.py`
  - script auxiliar para extrair e limpar o conteúdo do `<body>` de HTML.
  - útil quando o HTML fornecido está em formato ruim (uma linha só, muitas tags extras).
  - remove tags `<span>`, classes desnecessárias e torna o HTML mais legível.
  - gera `tmp_body_cleaned.html` para inspeção manual antes de usar no guia final.

### Pastas por API

Cada API deve ter sua própria pasta com este formato:

- `/<ApiName>/<api-name>.html` ou `index.html`
- `/<ApiName>/images/`

Exemplo atual:

- `Uazapi/uazapi.html`
- `Uazapi/images/`

## Fluxo de trabalho para novas APIs

### 1. Receber arquivos de referência

Os arquivos HTML e imagens da nova API são fornecidos diretamente e devem ser colocados na pasta `reference/`:

1. Coloque o arquivo HTML de referência em `reference/`
2. Coloque as imagens em `reference/images/` (ou subpasta específica da API)

### 2. Criar a estrutura da nova API

1. Crie a pasta `/<ApiName>/`.
2. Crie a pasta `/<ApiName>/images/`.

### 3. Criar o guia de API formatado

1. Copie `molde-api/index.html` para `/<ApiName>/index.html` (ou `<api-name>.html`).
2. **Importante**: O template já usa CSS global (`../css/styles.css`) e classe `api-guide` no `<body>`.
3. Copie as imagens de `reference/` para `/<ApiName>/images/`.
4. Substitua os placeholders do template pelo conteúdo da nova API (usando o HTML de referência).
5. Ajuste o texto, os títulos e as legendas de imagem conforme necessário.
6. Atualize a seção de vídeo embed em `/<ApiName>/index.html` com o `src` do YouTube ou Vimeo.
7. Use `write_formatted_guia.py` como referência adicional se quiser gerar o HTML com Python.

### 4. Limpar arquivos de referência

Após criar o guia final, remova os arquivos temporários da pasta `reference/`.

### 5. Atualizar o menu principal

Adicione um novo card em `index.html` apontando para a nova API:

```html
<article class="card">
  <h2>NovaApi</h2>
  <p>Guia passo a passo para conectar a API NovaApi ao CRM DataCrazy.</p>
  <a href="NovaApi/index.html">Abrir guia da NovaApi</a>
</article>
```

## Convenções de nomes e organização

- Pastas de API sempre com o nome da API em caixa baixa ou PascalCase, ex: `Uazapi`, `NovaApi`.
- Cada guia deve ficar em `<ApiName>/<api-name>.html` ou `<ApiName>/index.html`.
- As imagens devem ficar em `<ApiName>/images/`.
- Os links internos no HTML devem usar caminhos relativos para funcionar localmente.
- **CSS Global**: Todos os arquivos HTML devem usar `../css/styles.css` (ou `css/styles.css` para index.html na raiz).
- **Classes CSS**: 
  - Página principal: `<body class="home-page">`
  - Guias de API: `<body class="api-guide">`
- Não inclua CSS inline nos arquivos HTML - use o CSS global.

## Orientações para outras IAs

- Leia primeiro `README.md` e `KNOWLEDGE_BASE.md` para entender a estrutura.
- Use `index.html` como ponto de partida para descobrir quais APIs já existem.
- Verifique `Uazapi/uazapi.html` para exemplos de layout e formatação.
- Mantenha o projeto organizado e evite misturar arquivos de diferentes APIs.
- Use a pasta `reference/` para arquivos temporários de novas APIs.
- Use `tmp_extract_body.py` quando o HTML fornecido estiver em formato ruim.

## Observações

- A pasta `.venv` não deve ser usada para armazenar conteúdo do projeto, apenas para o ambiente Python.
- Arquivos temporários como `tmp_body_cleaned.html` podem ser apagados após a migração.
- O foco do projeto é documentação técnica clara para integrações de APIs.
