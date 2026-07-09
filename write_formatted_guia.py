from pathlib import Path

# Este script gera o arquivo HTML formatado do guia da API Uazapi.
# Ele é útil para criar um guia limpo a partir do conteúdo extraído e
# para manter o documento atualizado sempre que a estrutura de layout mudar.
#
# Estrutura do projeto:
#   /index.html          -> menu principal entre APIs
#   /Uazapi/index.html   -> guia da API Uazapi
#   /Uazapi/images/      -> imagens do guia Uazapi
#
# Para criar outros guias de API, copie este script e altere o conteúdo
# HTML e o caminho de saída para a pasta da nova API.

# Define o arquivo de saída desta geração de guia.
# Este script grava o guia diretamente na pasta Uazapi para manter a
# organização do projeto por API.
output_path = Path("Uazapi/index.html")
output_path.parent.mkdir(parents=True, exist_ok=True)

# Configurações iniciais do guia.
# Aqui definimos todo o HTML do guia Uazapi como uma string multilinha.
# O conteúdo HTML está codificado diretamente no script para permitir uma
# atualização rápida sem necessidade de um gerador externo separado.
html = '''<!DOCTYPE html>
<html lang="pt-BR">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Guia Rápido de Integração — Uazapi + CRM DataCrazy</title>
  <style>
    :root {
      color-scheme: light;
      color: #1d2939;
      background: #f2f4f8;
      font-family: Inter, system-ui, -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
      line-height: 1.65;
    }
    * { box-sizing: border-box; }
    body {
      margin: 0;
      min-height: 100vh;
      background: #f2f4f8;
    }
    a { color: #0057d9; text-decoration: none; }
    a:hover { text-decoration: underline; }
    img { max-width: 100%; height: auto; display: block; border-radius: 12px; }
    main { width: min(1120px, calc(100% - 32px)); margin: 0 auto; padding: 24px 0 48px; }
    header.hero {
      background: linear-gradient(180deg, #004aae 0%, #0d72d1 100%);
      color: white;
      border-radius: 24px;
      padding: 36px 32px;
      box-shadow: 0 24px 60px rgba(15, 23, 42, 0.18);
    }
    .hero .eyebrow {
      text-transform: uppercase;
      letter-spacing: 0.18em;
      font-size: 0.82rem;
      opacity: 0.86;
      margin-bottom: 16px;
    }
    .hero h1 {
      margin: 0;
      font-size: clamp(2rem, 5vw, 3.2rem);
      line-height: 1.02;
    }
    .hero .subtitle {
      margin: 18px 0 0;
      max-width: 720px;
      font-size: 1.05rem;
      opacity: 0.92;
    }
    .hero .meta {
      display: flex;
      flex-wrap: wrap;
      gap: 12px;
      margin-top: 22px;
      font-size: 0.95rem;
      color: #dbeafe;
    }
    section {
      margin-top: 32px;
      padding: 24px;
      background: white;
      border-radius: 20px;
      box-shadow: 0 16px 45px rgba(15, 23, 42, 0.08);
    }
    section h2 {
      font-size: 1.55rem;
      margin-top: 0;
      color: #0f172a;
    }
    section h3 {
      font-size: 1.15rem;
      margin-bottom: 0.8rem;
      color: #1d2939;
    }
    .overview, .note {
      background: #f8fbff;
      border-left: 4px solid #0f62ff;
    }
    .overview p, .note p {
      margin: 0;
    }
    .toc ol,
    .toc ul,
    .steps {
      padding-left: 1.3rem;
      margin: 0;
    }
    .toc li,
    .steps li {
      margin-bottom: 0.8rem;
    }
    .toc ol {
      counter-reset: item;
    }
    .toc li {
      list-style: none;
      margin-bottom: 0.85rem;
    }
    .toc li::before {
      content: counter(item) ". ";
      counter-increment: item;
      font-weight: 700;
      color: #0057d9;
    }
    .figure {
      margin: 24px 0;
      border: 1px solid #e2e8f0;
      border-radius: 18px;
      overflow: hidden;
      background: #ffffff;
    }
    .figure figcaption {
      padding: 14px 18px;
      background: #f8fafc;
      color: #475569;
      font-size: 0.95rem;
    }
    .grid {
      display: grid;
      gap: 20px;
    }
    .note {
      padding: 18px 20px;
      border-radius: 18px;
      color: #0f172a;
    }
    .note strong { color: #0f172a; }
    .footer {
      margin-top: 34px;
      text-align: center;
      font-size: 0.95rem;
      color: #64748b;
    }
    @media (max-width: 700px) {
      section { padding: 20px; }
      .hero { padding: 28px 20px; }
    }
  </style>
</head>
<body>
  <main>
    <header class="hero">
      <p class="eyebrow">Guia Rápido</p>
      <h1>Uazapi + CRM DataCrazy</h1>
      <p class="subtitle">Integração da API de WhatsApp com o CRM DataCrazy, detalhada passo a passo.</p>
      <div class="meta">
        <span>Versão 1.1</span>
        <span>Atualizado em 08/07/2026</span>
      </div>
    </header>

    <section class="overview">
      <h2>O que você encontra aqui</h2>
      <p>Este documento apresenta os principais passos para conectar a API de WhatsApp da Uazapi ao CRM DataCrazy, incluindo cadastro, aquisição de servidor, criação de instância e validação de integração.</p>
    </section>

    <section id="sumario" class="toc">
      <h2>Sumário</h2>
      <ol>
        <li><a href="#objetivo">Objetivo</a></li>
        <li><a href="#sobre-api-whatsapp">Sobre a API de WhatsApp</a></li>
        <li><a href="#pre-requisitos">Pré-requisitos</a></li>
        <li><a href="#configuracao-da-api">Configuração da API</a></li>
        <li><a href="#configuracao-crm-datacrazy">Configuração no CRM DataCrazy</a></li>
        <li><a href="#validacao-integracao">Validação da integração</a></li>
        <li><a href="#conclusao">Conclusão</a></li>
      </ol>
    </section>

    <section id="objetivo">
      <h2>1. Objetivo</h2>
      <p>Este guia apresenta, de forma rápida e objetiva, o processo de integração da API de WhatsApp da Uazapi ao CRM DataCrazy.</p>
    </section>

    <section id="sobre-api-whatsapp">
      <h2>2. Sobre a API de WhatsApp</h2>
      <p>A API de WhatsApp funciona como uma ponte segura entre o seu número de telefone e o CRM DataCrazy. Ela permite que o sistema envie notificações automáticas e receba mensagens dos clientes de forma centralizada, sem a necessidade de usar o aplicativo do WhatsApp no celular para responder.</p>
    </section>

    <section id="pre-requisitos">
      <h2>3. Pré-requisitos</h2>
      <ul>
        <li>Acesso de administrador ao CRM DataCrazy;</li>
        <li>Número de telefone ativo, preferencialmente com WhatsApp Business instalado;</li>
        <li>Forma de pagamento disponível (Pix ou cartão de crédito) para contratar o serviço da API.</li>
      </ul>
    </section>

    <section id="configuracao-da-api">
      <h2>4. Configuração da API</h2>

      <article>
        <h3>4.1 Criando seu acesso</h3>
        <p>Para criar sua conta na Uazapi, acesse o link abaixo:</p>
        <p><a href="https://uazapi.dev/interno?p=conecte" target="_blank" rel="noopener noreferrer">https://uazapi.dev/interno?p=conecte</a></p>
        <p>Na tela de cadastro da Uazapi, siga os passos abaixo:</p>
        <ul>
          <li>Informe um e-mail ao qual você tenha acesso;</li>
          <li>Aceite os termos de uso da Uazapi;</li>
          <li>Clique em Entrar.</li>
        </ul>
        <figure class="figure">
          <img src="images/image9.png" alt="Tela de cadastro Entrar com e-mail">
          <figcaption>Tela de cadastro — Entrar com e-mail.</figcaption>
        </figure>
        <p>Em seguida, confirme o código de verificação enviado para o seu e-mail. Esse processo pode levar alguns minutos; aguarde e verifique sua caixa de entrada.</p>
        <figure class="figure">
          <img src="images/image11.png" alt="Confirmação do código de verificação">
          <figcaption>Confirmação do código de verificação.</figcaption>
        </figure>
      </article>

      <article>
        <h3>4.2 Conhecendo o painel da Uazapi e adquirindo um servidor</h3>
        <p>A Uazapi disponibiliza um servidor gratuito para testes. As instâncias criadas no servidor gratuito são removidas automaticamente após 1 hora, mas o processo de configuração com o CRM DataCrazy é o mesmo dos servidores pagos.</p>
        <p>Para seguir com a integração permanente:</p>
        <ol class="steps">
          <li>Clique em “Preencha seu nome” ou em “Assinar” no canto esquerdo da tela para acessar o seu perfil na Uazapi.</li>
          <li>Na área de perfil, clique em “Nova assinatura”.</li>
          <li>Escolha o plano que melhor se encaixa no seu caso.</li>
        </ol>
        <figure class="figure">
          <img src="images/image10.png" alt="Servidor gratuito para testes">
          <figcaption>Servidor gratuito para testes.</figcaption>
        </figure>
        <figure class="figure">
          <img src="images/image13.png" alt="Acesso ao perfil e botão Assinar">
          <figcaption>Acesso ao perfil — “Assinar”.</figcaption>
        </figure>
        <figure class="figure">
          <img src="images/image12.png" alt="Perfil com opção Nova assinatura">
          <figcaption>Perfil — botão “Nova assinatura”.</figcaption>
        </figure>
        <figure class="figure">
          <img src="images/image15.png" alt="Seleção do plano Uazapi">
          <figcaption>Seleção do plano.</figcaption>
        </figure>
        <p>Você pode comparar os planos diretamente no site da Uazapi:</p>
        <p><a href="https://uazapi.dev/" target="_blank" rel="noopener noreferrer">https://uazapi.dev/</a></p>
        <figure class="figure">
          <img src="images/image14.png" alt="Comparativo de planos Uazapi">
          <figcaption>Comparativo de planos Uazapi.</figcaption>
        </figure>
        <p>Após escolher o plano, avance para o pagamento e complete a assinatura.</p>
        <figure class="figure">
          <img src="images/image17.png" alt="Resumo do plano escolhido">
          <figcaption>Resumo do plano escolhido.</figcaption>
        </figure>
        <figure class="figure">
          <img src="images/image16.png" alt="Tela de pagamento Uazapi">
          <figcaption>Tela de pagamento.</figcaption>
        </figure>
        <p>Depois da compra, cadastre os dados para utilizar o servidor. O nome pode ser o da sua empresa e serve apenas para identificação.</p>
        <figure class="figure">
          <img src="images/image20.png" alt="Cadastro dos dados do servidor">
          <figcaption>Cadastro dos dados do servidor.</figcaption>
        </figure>
        <p>Aqui você define o subdomínio do servidor. Ele deve conter mais de 5 caracteres e será usado para identificar a instância.</p>
        <figure class="figure">
          <img src="images/image18.png" alt="Definição do subdomínio do servidor">
          <figcaption>Definição do subdomínio do servidor.</figcaption>
        </figure>
        <p>Aguarde alguns instantes enquanto o servidor é estruturado. Atualize a página até o status ficar verde e exibir “online”.</p>
        <figure class="figure">
          <img src="images/image19.png" alt="Servidor em estruturação">
          <figcaption>Servidor em estruturação (status offline).</figcaption>
        </figure>
        <figure class="figure">
          <img src="images/image21.png" alt="Servidor pronto online">
          <figcaption>Servidor pronto (status online).</figcaption>
        </figure>
      </article>

      <article>
        <h3>4.3 Criando a instância</h3>
        <p>Clique em “Nova instância”. Preencha o nome desejado e selecione “Criar”.</p>
        <figure class="figure">
          <img src="images/image22.png" alt="Botão Nova instância">
          <figcaption>Botão “Nova instância”.</figcaption>
        </figure>
        <figure class="figure">
          <img src="images/image23.png" alt="Criação da instância">
          <figcaption>Criação da instância.</figcaption>
        </figure>
        <p>Para conectar, clique no nome da instância ou na linha azul abaixo.</p>
        <figure class="figure">
          <img src="images/image24.png" alt="Instância criada para conectar">
          <figcaption>Instância criada — clique para conectar.</figcaption>
        </figure>
        <p>No painel, clique em “Conectar”.</p>
        <figure class="figure">
          <img src="images/image25.png" alt="Painel da instância e botão Conectar">
          <figcaption>Painel da instância — botão “Conectar”.</figcaption>
        </figure>
        <p>Em seguida, clique em “Gerar QR Code”.</p>
        <figure class="figure">
          <img src="images/image26.png" alt="Geração do QR Code">
          <figcaption>Geração do QR Code.</figcaption>
        </figure>
        <p>Leia o QR Code com o seu dispositivo para finalizar a conexão.</p>
        <figure class="figure">
          <img src="images/image27.png" alt="QR Code para conexão do WhatsApp">
          <figcaption>QR Code para conexão do WhatsApp.</figcaption>
        </figure>
      </article>
    </section>

    <section id="configuracao-crm-datacrazy">
      <h2>5. Configuração no CRM DataCrazy</h2>
      <article>
        <h3>5.1 Conectando a Uazapi ao CRM DataCrazy</h3>
        <p>Após a compra e a conexão da instância na Uazapi, você precisará apenas de dois dados para concluir a integração no CRM DataCrazy: a URL do servidor (Server URL) e o token da instância (Instance Token).</p>
        <figure class="figure">
          <img src="images/image28.png" alt="Dados da instância com Server URL e Instance Token">
          <figcaption>Dados da instância — Server URL e Instance Token.</figcaption>
        </figure>
        <p>No CRM DataCrazy, acesse <strong>Configurações &gt; Conexões</strong>.</p>
        <figure class="figure">
          <img src="images/image1.png" alt="Tela de conexões do CRM DataCrazy">
          <figcaption>Tela de Conexões do CRM DataCrazy.</figcaption>
        </figure>
        <p>Clique no botão azul “Criar” para adicionar uma nova conexão.</p>
        <figure class="figure">
          <img src="images/image2.png" alt="Botão Criar nova conexão">
          <figcaption>Botão “Criar” nova conexão.</figcaption>
        </figure>
        <p>Nas opções de API para WhatsApp, selecione a Uazapi.</p>
        <figure class="figure">
          <img src="images/image3.png" alt="Seleção da API Uazapi">
          <figcaption>Seleção da API Uazapi.</figcaption>
        </figure>
        <p>Preencha o nome da conexão e os dados fornecidos pela Uazapi: URL do servidor e token da instância.</p>
        <figure class="figure">
          <img src="images/image4.png" alt="Cadastro da conexão com dados da Uazapi">
          <figcaption>Cadastro da conexão — dados da Uazapi.</figcaption>
        </figure>
        <p>Após preencher, clique em “Finalizar”.</p>
        <figure class="figure">
          <img src="images/image5.png" alt="Confirmação dos dados e botão Finalizar">
          <figcaption>Confirmação dos dados — botão “Finalizar”.</figcaption>
        </figure>
        <p>Se tudo estiver correto, o número será conectado com sucesso.</p>
        <figure class="figure">
          <img src="images/image6.png" alt="Conexão concluída com sucesso">
          <figcaption>Conexão concluída com sucesso.</figcaption>
        </figure>
      </article>
    </section>

    <section id="validacao-integracao">
      <h2>6. Validação da integração</h2>
      <p>Para testar, envie uma mensagem “Oi” para o número conectado e responda pelo CRM DataCrazy através do chat ao vivo.</p>
      <figure class="figure">
        <img src="images/image7.png" alt="Departamentos com acesso ao chat ao vivo">
        <figcaption>Departamentos — acesso ao chat ao vivo.</figcaption>
      </figure>
      <figure class="figure">
        <img src="images/image8.png" alt="Teste de mensagem no chat ao vivo do CRM">
        <figcaption>Teste de mensagem no chat ao vivo do CRM.</figcaption>
      </figure>
    </section>

    <section id="conclusao">
      <h2>7. Conclusão</h2>
      <p>Com os passos acima, a integração entre a Uazapi e o CRM DataCrazy está concluída: o número do WhatsApp está conectado e pronto para enviar e receber mensagens diretamente pelo CRM.</p>
      <p>Em caso de dúvidas durante o processo, consulte a documentação oficial da Uazapi ou entre em contato com o suporte do DataCrazy.</p>
    </section>

    <footer class="footer">
      <p>Guia rápido de integração — Uazapi + CRM DataCrazy</p>
    </footer>
  </main>
</body>
</html>
'''

# Escreve o HTML gerado no arquivo de saída dentro da pasta Uazapi.
# Essa etapa grava o guia no local correto do projeto para que o menu
# principal aponte para /Uazapi/index.html.
output_path.write_text(html, encoding='utf-8')
print(f'Arquivo atualizado: {output_path}')
