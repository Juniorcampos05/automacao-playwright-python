# Importa a classe responsável pelas ações da tela de login
from pages.login_page import LoginPage

# Importa a classe responsável pelas ações do dashboard
from pages.dashboard_page import DashboardPage


def test_fluxo_completo(page):
    """
    Cenário de teste responsável por validar o fluxo completo
    de autenticação e acesso ao ambiente acadêmico.

    Fluxo validado:

    1. Acesso à página de login
    2. Autenticação do usuário
    3. Tratamento de MFA
    4. Fechamento de pop-up inicial
    5. Acesso à área de estudos
    6. Abertura de nova aba
    7. Carregamento do dashboard
    8. Coleta dos links disponíveis na página
    """

    # Cria uma instância da página de login
    login = LoginPage(page)

    # Cria uma instância da página dashboard
    dashboard = DashboardPage(page)

    # Acessa a URL inicial da aplicação
    login.abrir_site()

    # Executa o fluxo completo de autenticação
    # utilizando as credenciais informadas
    login.realizar_login(
        "USUARIO_TESTE",
        "SENHA_TESTE"
    )

    # Ignora a etapa de autenticação multifator (MFA)
    dashboard.pular_mfa()

    # Fecha mensagens ou modais exibidos após o login
    dashboard.fechar_popup()

    # Acessa a área de estudos e captura a nova aba aberta
    nova_aba = dashboard.abrir_estudar()

    # Aguarda o carregamento completo da nova aba
    # antes de continuar as validações
    nova_aba.wait_for_load_state()

    # Obtém todos os links disponíveis na página
    # para inspeção ou futuras validações
    dashboard.listar_links()