# Molde de Guia de API

Este diretório é um exemplo de estrutura pronta para novos guias de API.

## Estrutura do molde

- `index.html`
  - guia de integração com a estrutura completa.
  - inclui uma seção de vídeo de apoio para embed do YouTube ou Vimeo.
  - suporta imagens locais em `images/`.

- `images/`
  - pasta vazia para armazenar as imagens da nova API.

## Como usar

1. Copie a pasta `molde-api/` para um novo diretório com o nome da API, por exemplo `NovaApi/`.
2. Renomeie `NovaApi/index.html` substituindo os placeholders:
   - `{{API_DISPLAY_NAME}}`
   - `{{API_SUBTITLE}}`
   - `{{API_VERSION}}`
   - `{{UPDATE_DATE}}`
   - `{{API_OVERVIEW}}`
   - `{{SECTION_OBJETIVO}}`
   - `{{SECTION_SOBRE_API}}`
   - `{{REQUIREMENT_1}}` / `{{REQUIREMENT_2}}` / `{{REQUIREMENT_3}}`
   - `{{SECTION_SETUP_ACCESS}}`
   - `{{SECTION_PANEL_AND_SERVER}}`
   - `{{SECTION_INSTANCE_CREATION}}`
   - `{{SECTION_CRM_SETUP}}`
   - `{{SECTION_VALIDATION}}`
   - `{{SECTION_CONCLUSION}}`
3. Copie as imagens relevantes para `NovaApi/images/`.
4. Atualize o `iframe` dentro da seção de vídeo com o link embed do YouTube ou Vimeo.
5. Ajuste qualquer texto adicional e verifique a navegação relativa para `../index.html`.
