from abc import ABC, abstractmethod


# A classe base de comando define a interface comum para todos os comandos
# concretos.
class Command(ABC):
    def __init__(self, app, editor):
        self.app = app
        self.editor = editor
        self.backup = None

    # Fazer um backup do estado do editor.
    def save_backup(self):
        self.backup = self.editor.text

    # Restaurar o estado do editor.
    def undo(self):
        self.editor.text = self.backup

    # O método de execução é declarado abstrato para forçar todos
    # os comandos concretos a fornecerem suas próprias implementações.
    # O método deve retornar True ou False dependendo se o comando
    # altera o estado do editor.
    @abstractmethod
    def execute(self):
        pass


# Os comandos concretos vão aqui.
class CopyCommand(Command):
    # O comando de cópia não é salvo no histórico, pois ele não
    # altera o estado do editor.
    def execute(self):
        self.app.clipboard = self.editor.get_selection()
        return False


class CutCommand(Command):
    # O comando de corte altera o estado do editor, portanto,
    # ele deve ser salvo no histórico. E será salvo desde que
    # o método retorne True.
    def execute(self):
        self.save_backup()
        self.app.clipboard = self.editor.get_selection()
        self.editor.delete_selection()
        return True


class PasteCommand(Command):
    def execute(self):
        self.save_backup()
        self.editor.replace_selection(self.app.clipboard)
        return True


# A operação de desfazer também é um comando.
class UndoCommand(Command):
    def execute(self):
        self.app.undo()
        return False


# O histórico de comandos global é apenas uma pilha.
class CommandHistory:
    def __init__(self):
        self.history = []

    # Último a entrar...
    def push(self, command):
        self.history.append(command)

    # ...primeiro a sair
    def pop(self):
        if self.history:
            return self.history.pop()
        return None


# A classe editor tem operações reais de edição de texto.
# Ela desempenha o papel de receptor: todos os comandos acabam delegando
# a execução aos métodos do editor.
class Editor:
    def __init__(self):
        self.text = ""

    def get_selection(self):
        # Retornar texto selecionado.
        return "selected text"

    def delete_selection(self):
        # Excluir texto selecionado.
        self.text = self.text.replace("selected text", "")

    def replace_selection(self, text):
        # Inserir o conteúdo da área de transferência na posição atual.
        self.text += text


# A classe aplicação configura as relações dos objetos. Ela atua como um
# remetente: quando algo precisa ser feito, ela cria um objeto de comando
# e o executa.
class Application:
    def __init__(self):
        self.clipboard = ""
        self.editors = [Editor()]
        self.active_editor = self.editors[0]
        self.history = CommandHistory()

    # O código que atribui comandos aos objetos de UI pode ser parecido com
    # este.
    def create_ui(self):
        copy = lambda: self.execute_command(  # noqa
            CopyCommand(self, self.active_editor)
        )

        cut = lambda: self.execute_command(  # noqa
            CutCommand(self, self.active_editor)
        )

        paste = lambda: self.execute_command(  # noqa
            PasteCommand(self, self.active_editor)
        )

        undo = lambda: self.execute_command(  # noqa
            UndoCommand(self, self.active_editor)
        )

        # Simular atribuição de comandos a botões e atalhos.
        # No código real, isso seria feito através de uma biblioteca de UI.
        copy_button = copy
        cut_button = cut
        paste_button = paste
        undo_button = undo

        # Simular pressionar os atalhos.
        shortcuts = {  # noqa
            "Ctrl+C": copy,
            "Ctrl+X": cut,
            "Ctrl+V": paste,
            "Ctrl+Z": undo
        }

        # Para fins de exemplo, executando os comandos manualmente.
        copy_button()
        cut_button()
        paste_button()
        undo_button()

    # Executar um comando e verificar se ele deve ser adicionado ao histórico.
    def execute_command(self, command):
        if command.execute():
            self.history.push(command)

    # Pegar o comando mais recente do histórico e executar seu método de
    # desfazer.
    # Note que não sabemos a classe desse comando. Mas não precisamos,
    # pois o comando sabe como desfazer sua própria ação.
    def undo(self):
        command = self.history.pop()
        if command is not None:
            command.undo()


if __name__ == "__main__":
    app = Application()
    app.create_ui()
