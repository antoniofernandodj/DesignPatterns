from interface import GUIFactory, Button, Checkbox


class WinFactory(GUIFactory):
    def create_button(self):
        return WinButton()

    def create_checkbox(self):
        return WinCheckbox()


class WinButton(Button):
    def paint(self):
        return "Rendering a button in Windows style."


class WinCheckbox(Checkbox):
    def paint(self):
        return "Rendering a checkbox in Windows style."