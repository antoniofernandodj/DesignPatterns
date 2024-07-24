from __future__ import annotations
from abc import ABC, abstractmethod
from datetime import datetime
from random import sample
from string import ascii_letters
from typing import List

"""
 Applicability
 Use the Memento pattern when you want to produce snapshots of the object's
 state to be able to restore a previous state of the object.

 The Memento pattern lets you make full copies of an object's state, including
 private fields, and store them separately from the object. While most people
 remember this pattern thanks to the “undo” use case, it's also indispensable
 when dealing with transactions (i.e., if you need to roll back an operation
 on error).

 Use the pattern when direct access to the object's fields/getters/setters
 violates its encapsulation.

 The Memento makes the object itself responsible for creating a snapshot of
 its state. No other object can read the snapshot, making the original
 object's state data safe and secure.

 How to Implement
Determine what class will play the role of the originator. It's important to
know whether the program uses one central object of this type or multiple
smaller ones.

Create the memento class. One by one, declare a set of fields that mirror the
fields declared inside the originator class.

Make the memento class immutable. A memento should accept the data just once,
via the constructor. The class should have no setters.

If your programming language supports nested classes, nest the memento inside
the originator. If not, extract a blank interface from the memento class and
make all other objects use it to refer to the memento. You may add some
metadata operations to the interface, but nothing that exposes the
originator's state.

Add a method for producing mementos to the originator class. The originator
should pass its state to the memento via one or multiple arguments of the
memento's constructor.

The return type of the method should be of the interface you extracted in the
previous step (assuming that you extracted it at all). Under the hood, the
memento-producing method should work directly with the memento class.

Add a method for restoring the originator's state to its class. It should
accept a memento object as an argument. If you extracted an interface in the
previous step, make it the type of the parameter. In this case, you need to
typecast the incoming object to the memento class, since the originator needs
full access to that object.

The caretaker, whether it represents a command object, a history, or something
entirely different, should know when to request new mementos from the
originator, how to store them and when to restore the originator with a
particular memento.

The link between caretakers and originators may be moved into the memento
class. In this case, each memento must be connected to the originator that had
created it. The restoration method would also move to the memento class.
However, this would all make sense only if the memento class is nested into
originator or the originator class provides sufficient setters for overriding
its state.

 Pros and Cons

 Pros:
 You can produce snapshots of the object's state without violating its
 encapsulation.
 You can simplify the originator's code by letting the caretaker maintain the
 history of the originator's state.

 Cons:
 The app might consume lots of RAM if clients create mementos too often.
 Caretakers should track the originator's lifecycle to be able to destroy
 obsolete mementos.
 Most dynamic programming languages, such as PHP, Python and JavaScript, can't
 guarantee that the state within the memento stays untouched.
 Relations with Other Patterns
You can use Command and Memento together when implementing “undo”. In this
case, commands are responsible for performing various operations over a target
object, while mementos save the state of that object just before a command
gets executed.

You can use Memento along with Iterator to capture the current iteration state
and roll it back if necessary.

Sometimes Prototype can be a simpler alternative to Memento. This works if the
object, the state of which you want to store in the history, is fairly
straightforward and doesn't have links to external resources, or the
links are easy to re-establish.

"""


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

    def __init__(self, state: str) -> None:
        self._state = state
        print(f"Originator: My initial state is: {self._state}")
        self.restored: List[Memento] = []

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

    def save(self) -> Memento:
        """
        Saves the current state inside a memento.
        """
        if self._state is None:
            raise AttributeError

        return Snapshot(self._state)

    def restore(self, memento: Memento) -> None:
        """
        Restores the Originator's state from a memento object.
        """
        self._state = memento.state
        print(f"Originator: My state has changed to: {self._state}")
        self.restored.append(memento)

    def unrestore(self, memento: Memento) -> None:
        """
        Unrestores the Originator's state to a memento object.
        """
        ...


class Memento(ABC):
    """
    The Memento interface provides a way to retrieve the memento's metadata,
    such as creation date or name. However, it doesn't expose the Originator's
    state.
    """
    state: str
    date: str

    @property
    @abstractmethod
    def name(str):
        raise NotImplementedError('name')


class Snapshot(Memento):
    def __init__(self, state: str) -> None:
        self.state = state
        self.date = str(datetime.now())[:19]

    @property
    def name(self) -> str:
        """
        The rest of the methods are used by the Caretaker to display metadata.
        """
        return f"{self.date} / ({self.state[0:9]}...)"

    def __repr__(self) -> str:
        return f"""
            Snapshot {{ state: {self.state}, date: {self.date}}}
        """.strip()


class Caretaker:
    """
    The Caretaker doesn't depend on the Concrete Memento class. Therefore, it
    doesn't have access to the originator's state, stored inside the memento.
    It works with all mementos via the base Memento interface.
    """

    def __init__(self, originator: Originator) -> None:
        self._history: List[Memento] = []
        self._originator = originator

    def backup(self) -> None:
        print("\nCaretaker: Saving Originator's state...")
        m = self._originator.save()
        self._history.append(m)

    def undo(self) -> None:
        if not len(self._history):
            return

        try:
            memento = self._history.pop()
            print(f"Caretaker: Restoring state to: {memento.name}")

            self._originator.restore(memento)
        except Exception:
            print('Cannot undo')

    def redo(self) -> None:
        try:
            memento = self._originator.restored.pop()
            print(f"Caretaker: Unrestoring state to: {memento.name}")
            self._history.append(memento)
            print(f"Caretaker: Received memento: {memento}")
        except Exception:
            print('Cannot redo')

    def show_history(self) -> None:
        print("Caretaker: Here's the list of mementos:")
        for memento in self._history:
            print(memento.name)


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
