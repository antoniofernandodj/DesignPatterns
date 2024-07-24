from interface import GUIFactory, Button, Checkbox


class MacFactory(GUIFactory):
    def create_button(self):
        return MacButton()

    def create_checkbox(self):
        return MacCheckbox()


class MacButton(Button):
    def paint(self):
        return "Rendering a button in Mac style."


class MacCheckbox(Checkbox):
    def paint(self):
        return "Rendering a checkbox in Mac style."
