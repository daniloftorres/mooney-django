# Docker

    1.  Imagens
        1. Use imagens Docker oficiais e confiáveis
        2. Mantenha-as atualizadas

    2. Configurações de segurança:
        1. De preferencia sar usuários não root dentro de containers

    3. Volumes
        1. Assegure-se de que apenas os dados necessários estejam acessíveis aos containers
        2. Limite as permissões de arquivo para os volumes montados.

    4. Rede
        1. Use redes Docker personalizadas para controlar o acesso entre os serviços.

    5. Segredos e Configurações
        1. Variáveis de ambiente para configurações sensíveis
        2. Considere o uso de um gerenciador de segredos Docker para armazenar informações sensíveis.

# Nginx

    1.  Configuração
        1. Desabilitar a exposição da versão do Nginx
        2. Use cabeçalhos de segurança : (por exemplo, Strict-Transport-Security, X-Frame-Options, etc.)
        "analisar o que é isso: more_clear_headers  'Server' 'X-Powered-By' 'X-Runtime';"
        https://gist.github.com/dmxhZGp1c2hh/1f04f10fca5dd8823377

    2. HTTPS
        1. Configure o Nginx para usar HTTPS com certificados válidos
        2. Redirecione todo o tráfego HTTP para HTTPS.

# Postgres

    1.  Configuração
        1. Limite o acesso à rede
        2. Utilize métodos de autenticação fortes

    2. Backups
        1. Implemente uma política de backup e teste regularmente a restauração dos backups.

# Django

    1. Dependências
        1. Manter todas as dependências atualizadas

    2. Configurações de segurança:
        1. Ultilize configurações como :
            1. SECURE_SSL_REDIRECT
            2. SECURE_HSTS_SECONDS
            3. X_FRAME_OPTIONS
            4. CSRF_COOKIE_SECURE
            5. SESSION_COOKIE_SECURE

    3. Middlewares

    4. Autenticação e Permissões

    5. Modelos de Usuário Personalizado

    6. Testes de Segurança:
        1. Injeção SQL
        2. Cross-site scripting (XSS)
        3. cross-site request forgery (CSRF)

# Geral

    1. Atualizações e Patches
        1. Sistema Operacional
        2. Docker
        3. Todas dependencias do projeto

    2. Monitoramento e Logs
        1. Log de tudo
        2. Alerta de Anomalias

    3. Revisão de Código
        1. Revisão constante para detectar vulnerabilidades e gargalos.

    4. Ambiente de Desenvolvimento vs. Produção
        1. Manter dados sensiveis de produção separao de local e homolocação

    5. Backups
        1. Testes e melhorias constantes no fluxo de backup de sistemas criticos.
