from pathlib import Path
import re

# Script temporário para extrair apenas o conteúdo do <body> de um HTML
# gerado automaticamente. Ele existe para facilitar a migração quando o
# arquivo original estava em uma única linha e continha muitas classes e
# spans de formatação do Google Docs ou de exportações de editores.

# Caminho do HTML original que será inspecionado.
path = Path('GuiaRpidoConexoUazapi.html')
text = path.read_text(encoding='utf-8')

# Busca o conteúdo entre as tags <body> e </body> usando expressão regular.
# Isso evita qualquer processamento complexo de HTML quando o caso é apenas
# inspecionar o conteúdo interno e limpar wrappers desnecessários.
body = re.search(r'(<body[^>]*>)(.*?)(</body>)', text, flags=re.S | re.I)
if not body:
    raise SystemExit('No body found')
body_html = body.group(2)

# Limpeza básica do HTML extraído:
# - remove tags <span> geradas automaticamente;
# - remove atributos class que não interessam para o novo layout;
# - elimina parágrafos vazios;
# - adiciona quebras de linha para tornar o HTML legível.
body_html = re.sub(r'<span[^>]*>', '', body_html)
body_html = re.sub(r'</span>', '', body_html)
body_html = re.sub(r'\s*class="[^"]*"', '', body_html)
body_html = re.sub(r'<p>\s*</p>', '', body_html)
body_html = re.sub(r'>\s*<', '>' + '\n' + '<', body_html)

# Salva o resultado em um arquivo temporário para inspeção manual.
# Este arquivo pode ser apagado quando a migração estiver concluída.
Path('tmp_body_cleaned.html').write_text(body_html, encoding='utf-8')
print('Saved tmp_body_cleaned.html')
print(body_html[:4000])
