from __future__ import annotations
from datetime import datetime
from random import sample
from string import ascii_letters
from typing import List


class Originator:
    """
    The Originator holds some important state that may change over time.
    It also defines a method for saving the state inside a
    memento and another method for restoring the state from it.
    """

    _state = None
    """
    For the sake of simplicity, the originator's state is
    stored inside a single variable.
    """

    class Snapshot:
        def __init__(self, state: str) -> None:
            self.state = state
            self.date = str(datetime.now())[:19]

        @property
        def name(self) -> str:
            """
            The rest of the methods are used by the Caretaker to display
            metadata.
            """
            return f"{self.date} / ({self.state[0:9]}...)"

        def __repr__(self) -> str:
            return f"""
                Snapshot {{ state: {self.state}, date: {self.date}}}
            """.strip()

    def __init__(self, state: str) -> None:

        self._state = state
        print(f"Originator: My initial state is: {self._state}")
        self.restored: List[Originator.Snapshot] = []

    def do_something(self) -> None:
        """
        The Originator's business logic may affect its internal state.
        Therefore, the client should backup the state before launching methods
        of the business logic via the save() method.
        """

        print("Originator: I'm doing something important.")
        self._state = self._generate_random_string(5)
        print(f"Originator: and my state has changed to: {self._state}")

    @staticmethod
    def _generate_random_string(length: int = 10) -> str:
        return "".join(sample(ascii_letters, length))

    def save(self) -> Snapshot:
        """
        Saves the current state inside a memento.
        """
        if self._state is None:
            raise AttributeError

        return Originator.Snapshot(self._state)

    def restore(self, snapshot: Snapshot) -> None:
        """
        Restores the Originator's state from a memento object.
        """
        self._state = snapshot.state
        print(f"Originator: My state has changed to: {self._state}")
        self.restored.append(snapshot)


class Caretaker:
    """
    The Caretaker doesn't depend on the Concrete Memento class. Therefore, it
    doesn't have access to the originator's state, stored inside the memento.
    It works with all mementos via the base Memento interface.
    """

    def __init__(self, originator: Originator) -> None:
        self._history: List[Originator.Snapshot] = []
        self._originator = originator

    def backup(self) -> None:
        print("\nCaretaker: Saving Originator's state...")
        m = self._originator.save()
        self._history.append(m)

    def undo(self) -> None:
        if not len(self._history):
            return

        try:
            snapshot = self._history.pop()
            print(f"Caretaker: Restoring state to: {snapshot.name}")

            self._originator.restore(snapshot)
        except Exception:
            print('Cannot undo')

    def redo(self) -> None:
        try:
            snapshot = self._originator.restored.pop()
            print(f"Caretaker: Unrestoring state to: {snapshot.name}")
            self._history.append(snapshot)
            print(f"Caretaker: Received memento: {snapshot}")
        except Exception:
            print('Cannot redo')

    def show_history(self) -> None:
        print("Caretaker: Here's the list of mementos:")
        for snapshot in self._history:
            print(snapshot.name)


if __name__ == "__main__":
    originator = Originator("Super-duper-super-puper-super.")
    caretaker = Caretaker(originator)

    for i in range(6):
        caretaker.backup()
        originator.do_something()

    print()
    caretaker.show_history()

    print("\nClient: Now, let's rollback!\n")
    caretaker.undo()

    print("\nClient: Once more!\n")
    caretaker.undo()

    print("\nClient: Once more!!\n")
    caretaker.undo()

    print('xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx')

    print("\nClient: Lets redo!\n")
    caretaker.redo()

    print("\nClient: Redo once more!\n")
    caretaker.redo()

    print("\nClient: Redo once more!\n")
    caretaker.redo()

    print('xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx')
