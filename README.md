# Projeto de Guias de Integração de APIs

Este projeto organiza documentos de integração de APIs por pasta, com um menu principal para navegar entre os guias disponíveis.

## Estrutura geral do projeto

- `index.html`
  - Menu principal do projeto.
  - Lista as APIs disponíveis e direciona para cada guia específico.
  - Usa CSS global com classe `home-page`.

- `css/styles.css`
  - Arquivo CSS global compartilhado por todas as páginas.
  - Contém variáveis CSS e estilos para página principal e guias de API.
  - Facilita manutenção e consistência visual.

- `js/`
  - Pasta reservada para scripts JavaScript (uso futuro).

- `assets/`
  - Pasta reservada para assets globais (uso futuro).

- `reference/`
  - Pasta para arquivos de referência temporários (HTML e imagens).
  - Usada para receber os arquivos de nova API antes de criar o guia final.
  - Após criar o guia, os arquivos podem ser removidos desta pasta.

- `molde-api/`
  - Template para novos guias de API.
  - Contém:
    - `index.html` — modelo base com placeholders.
    - `images/` — pasta vazia para imagens.
  - Usa CSS global com classe `api-guide`.

- `Uazapi/`
  - Pasta da API Uazapi.
  - Contém:
    - `uazapi.html` — guia de integração formatado.
    - `images/` — imagens usadas pelo guia.

- `write_formatted_guia.py`
  - Script Python que gera o HTML do guia Uazapi e grava em `Uazapi/uazapi.html`.
  - Ele também garante que a pasta `Uazapi/` exista antes de escrever.
  - Use como modelo para criar novos scripts de guia para outras APIs.

- `tmp_extract_body.py`
  - Script auxiliar para extrair e limpar o conteúdo do `<body>` de HTML.
  - Útil quando o HTML fornecido está em formato ruim (uma linha só, muitas tags extras).
  - Remove tags `<span>`, classes desnecessárias e torna o HTML mais legível.
  - Gera `tmp_body_cleaned.html` para inspeção manual antes de usar no guia final.

## Como adicionar um novo guia de API

A ideia é organizar por pasta de API, com cada pasta contendo seu próprio HTML e imagens.

### 1. Receber arquivos de referência

Os arquivos HTML e imagens da nova API são fornecidos diretamente:

1. Coloque o arquivo HTML de referência em `reference/`
2. Coloque as imagens em `reference/images/` (ou subpasta específica da API)

### 1.1. Opcional: Limpar o HTML fornecido

Se o HTML fornecido estiver em formato ruim (uma linha só, muitas tags extras):

1. Renomeie o arquivo HTML para algo como `google_export.html` e coloque em `reference/`.
2. Execute o script:

```powershell
cd "c:\Users\wes\Doc CRMDataCrazy"
python tmp_extract_body.py
```

3. O script gera `tmp_body_cleaned.html` com o HTML limpo.
4. Use esse arquivo como referência para criar o guia.
5. Após criar o guia, delete `tmp_body_cleaned.html` se não precisar mais dele.

### 2. Criar a pasta da nova API

Por exemplo, para uma nova API chamada `NovaApi`:

- Crie `NovaApi/`
- Crie `NovaApi/images/`
- Crie `NovaApi/index.html` (ou `novaapi.html`)

### 3. Criar o guia formatado

Para novos guias, você pode usar dois caminhos:

- copiar o template `molde-api/index.html` para `NovaApi/index.html` e substituir os placeholders pelo conteúdo real da API;
- ou criar um novo script Python baseado em `write_formatted_guia.py` se quiser gerar o HTML automaticamente.

Se usar o template, siga estes passos:

1. Copie `molde-api/index.html` para `NovaApi/index.html`.
2. **Importante**: O template já usa CSS global (`../css/styles.css`) e classe `api-guide` no `<body>`. Não remova essas referências.
3. Copie as imagens de `reference/` para `NovaApi/images/`.
4. Substitua os placeholders no arquivo HTML:
   - `{{API_DISPLAY_NAME}}`
   - `{{API_SUBTITLE}}`
   - `{{API_VERSION}}`
   - `{{UPDATE_DATE}}`
   - `{{API_OVERVIEW}}`
   - `{{SECTION_OBJETIVO}}`
   - `{{SECTION_SOBRE_API}}`
   - `{{REQUIREMENT_1}}`, `{{REQUIREMENT_2}}`, `{{REQUIREMENT_3}}`
   - `{{SECTION_SETUP_ACCESS}}`
   - `{{SECTION_PANEL_AND_SERVER}}`
   - `{{SECTION_INSTANCE_CREATION}}`
   - `{{SECTION_CRM_SETUP}}`
   - `{{SECTION_VALIDATION}}`
   - `{{SECTION_CONCLUSION}}`
5. Use o conteúdo do HTML de referência em `reference/` para preencher as seções.
6. Ajuste quaisquer imagens e legendas necessárias para o novo guia.
7. Atualize a seção de vídeo embed com o link embed do YouTube ou Vimeo.
8. Verifique o link relativo para `../index.html`.

Se preferir usar o script Python, copie `write_formatted_guia.py` para `write_formatted_novaapi.py` e altere:

- `output_path = Path("NovaApi/index.html")` (ou `NovaApi/novaapi.html`)
- o conteúdo da string `html` com o layout e textos da nova API.
- **Importante**: Inclua o link para CSS global: `<link rel="stylesheet" href="../css/styles.css">`
- Adicione a classe `api-guide` no `<body>`.

### 4. Limpar arquivos de referência

Após criar o guia final, remova os arquivos temporários da pasta `reference/`.

### 5. Adicionar ao menu principal

Abra `index.html` na raiz e adicione um novo card no `<section class="cards">`:

```html
<article class="card">
  <h2>NovaApi</h2>
  <p>Guia passo a passo para conectar a API NovaApi ao CRM.</p>
  <a href="NovaApi/index.html">Abrir guia da NovaApi</a>
</article>
```

## Recomendações de uso

- Use `write_formatted_guia.py` como referência e modelo para novas APIs.
- Mantenha cada guia dentro da sua própria pasta API.
- Use a pasta `reference/` para arquivos temporários de novas APIs.
- Após criar o guia, limpe os arquivos de `reference/`.
- Use `tmp_extract_body.py` quando o HTML fornecido estiver em formato ruim.
- **Sempre use o CSS global** (`css/styles.css`) em novos arquivos HTML.
- Não inclua CSS inline nos arquivos HTML - use o CSS global para consistência.
- Use as classes CSS apropriadas no `<body>`: `home-page` (menu principal) ou `api-guide` (guias de API).

## Exemplo de estrutura final

```
Doc CRMDataCrazy/
├── index.html
├── README.md
├── KNOWLEDGE_BASE.md
├── write_formatted_guia.py
├── css/
│   └── styles.css
├── js/
├── assets/
├── reference/
│   └── (arquivos temporários para criação de novos guias)
├── molde-api/
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

## Observações

- O projeto foi pensado para ser escalável: cada API tem sua própria pasta e recursos.
- Para cada nova API, mantenha a mesma lógica de estrutura e adicione o card correspondente no menu principal.
- O CSS global centraliza todos os estilos, facilitando manutenção e garantindo consistência visual.
- Consulte `KNOWLEDGE_BASE.md` para documentação detalhada destinada a IAs e servidores de contexto.
