from playwright.sync_api import Page, expect


class LoginPage:
    """
    Classe responsável pelas ações da tela de login.

    Centraliza todas as operações relacionadas à autenticação
    do usuário, facilitando a manutenção e reutilização dos testes.

    Esta classe segue o padrão Page Object Model (POM),
    amplamente utilizado em projetos de automação.
    """

    def __init__(self, page: Page):
        """
        Construtor da classe.

        Recebe a instância da página atual do Playwright,
        permitindo que os métodos realizem interações
        com os elementos da interface.
        """

        self.page = page

    def abrir_site(self):
        """
        Acessa a página inicial de autenticação.

        Este método é responsável por iniciar o fluxo
        de login carregando a URL do sistema.
        """

        self.page.goto(
            "https://login.unopar.br/"
        )

    def preencher_usuario(self, usuario):
        """
        Preenche o campo de usuário.

        Antes de preencher o valor, é realizada uma validação
        para garantir que o campo esteja visível e pronto
        para receber dados.
        """

        # Localiza o campo de usuário através do data-testid
        campo_usuario = self.page.get_by_test_id(
            "login-input"
        )

        # Aguarda o campo ficar visível
        expect(campo_usuario).to_be_visible()

        # Preenche o usuário informado
        campo_usuario.fill(usuario)

    def clicar_avancar(self):
        """
        Aciona o botão responsável por avançar
        para a próxima etapa do login.

        O método garante que o botão esteja habilitado
        antes da interação.
        """

        # Localiza o botão de avanço
        botao = self.page.get_by_test_id(
            "submit-button"
        )

        # Valida se o botão está habilitado
        expect(botao).to_be_enabled()

        # Executa o clique
        botao.click()

    def preencher_senha(self, senha):
        """
        Preenche o campo de senha.

        O método aguarda a exibição do campo antes
        de inserir a credencial do usuário.
        """

        # Localiza o campo de senha
        campo_senha = self.page.get_by_test_id(
            "login-pass"
        )

        # Aguarda o campo ficar disponível
        expect(campo_senha).to_be_visible()

        # Insere a senha
        campo_senha.fill(senha)

    def realizar_login(self, usuario, senha):
        """
        Executa o fluxo completo de autenticação.

        O método encapsula todas as etapas necessárias
        para realizar o login:

        1. Preenchimento do usuário
        2. Clique no botão avançar
        3. Preenchimento da senha
        4. Confirmação do login

        Dessa forma, o teste principal fica mais limpo
        e reutilizável.
        """

        # Preenche o usuário informado
        self.preencher_usuario(usuario)

        # Avança para a etapa de senha
        self.clicar_avancar()

        # Preenche a senha
        self.preencher_senha(senha)

        # Finaliza o processo de login
        self.clicar_avancar()