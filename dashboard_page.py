from playwright.sync_api import Page, expect


class DashboardPage:
    """
    Classe responsável pelas ações da página Dashboard.

    Aqui ficam centralizadas todas as interações realizadas
    após o usuário concluir o processo de autenticação.
    """

    def __init__(self, page: Page):
        """
        Construtor da classe.

        Recebe o objeto Page do Playwright para permitir
        que os métodos interajam com a página atual.
        """

        self.page = page

    def pular_mfa(self):
        """
        Realiza o bypass da etapa de autenticação multifator (MFA).

        O método localiza o botão responsável por ignorar
        a validação adicional e garante que ele esteja visível
        antes da interação.
        """

        # Localiza o botão "Pular MFA"
        botao = self.page.get_by_test_id(
            "skip-mfa"
        )

        # Aguarda o botão ficar visível na tela
        expect(botao).to_be_visible()

        # Executa o clique
        botao.click()

    def fechar_popup(self):
        """
        Fecha o modal ou pop-up exibido após o login.

        Alguns sistemas apresentam avisos, notificações ou
        mensagens informativas que podem bloquear elementos
        da interface.
        """

        # Localiza o botão de fechamento do modal
        botao_fechar = self.page.get_by_role(
            "button",
            name="close"
        )

        # Valida se o botão está disponível
        expect(botao_fechar).to_be_visible()

        # Fecha o pop-up
        botao_fechar.click()

    def abrir_estudar(self):
        """
        Acessa a área de estudos da plataforma.

        O clique no link "Estudar" abre uma nova aba.
        Por isso utilizamos expect_popup() para capturar
        a nova janela criada pelo navegador.
        """

        # Aguarda a abertura de uma nova aba
        with self.page.expect_popup() as popup:

            # Clica no link responsável por abrir
            # o ambiente de estudos
            self.page.get_by_role(
                "link",
                name="Estudar",
                exact=True
            ).click()

        # Retorna a referência da nova aba
        return popup.value

    def listar_links(self):
        """
        Obtém todos os links disponíveis na página atual.

        Pode ser utilizado para auditoria de navegação,
        validação de menus ou inspeção dos elementos
        disponíveis ao usuário.
        """

        # Captura todos os elementos do tipo link (<a>)
        links = self.page.get_by_role(
            "link"
        ).all()

        # Percorre cada link encontrado
        for link in links:

            # Exibe informações do locator no terminal
            print(link)