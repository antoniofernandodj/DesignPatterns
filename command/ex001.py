"""
Applicability
 Use the Command pattern when you want to parametrize objects with operations.

 The Command pattern can turn a specific method call into a stand-alone object.
 This change opens up a lot of interesting uses: you can pass commands as
 method arguments, store them inside other objects, switch linked commands at
 runtime, etc.

Here's an example: you're developing a GUI component such as a context menu,
and you want your users to be able to configure menu items that trigger
operations when an end user clicks an item.

 Use the Command pattern when you want to queue operations, schedule their
 execution, or execute them remotely.

 As with any other object, a command can be serialized, which means converting
 it to a string that can be easily written to a file or a database. Later,
 the string can be restored as the initial command object. Thus, you can
 delay and schedule command execution. But there's even more! In the same way,
 you can queue, log or send commands over the network.

 Use the Command pattern when you want to implement reversible operations.

 Although there are many ways to implement undo/redo, the Command pattern
 is perhaps the most popular of all.

To be able to revert operations, you need to implement the history of
performed operations. The command history is a stack that contains all
executed command objects along with related backups of the application's state.

This method has two drawbacks. First, it isn't that easy to save an
application's state because some of it can be private. This problem can be
mitigated with the Memento pattern.

Second, the state backups may consume quite a lot of RAM. Therefore,
sometimes you can resort to an alternative implementation: instead of
restoring the past state, the command performs the inverse operation.
The reverse operation also has a price: it may turn out to be hard or
even impossible to implement.

 How to Implement
Declare the command interface with a single execution method.

Start extracting requests into concrete command classes that implement
the command interface. Each class must have a set of fields for storing
the request arguments along with a reference to the actual receiver object.
All these values must be initialized via the command's constructor.

Identify classes that will act as senders. Add the fields for storing
commands into these classes. Senders should communicate with their commands
only via the command interface. Senders usually don't create command
objects on their own, but rather get them from the client code.

Change the senders so they execute the command instead of sending a request
to the receiver directly.

The client should initialize objects in the following order:

Create receivers.
Create commands, and associate them with receivers if needed.
Create senders, and associate them with specific commands.


Pros and Cons

Pros:
 Single Responsibility Principle. You can decouple classes that invoke
 operations from classes that perform these operations.
 Open/Closed Principle. You can introduce new commands into the app without
 breaking existing client code.
 You can implement undo/redo.
 You can implement deferred execution of operations.
 You can assemble a set of simple commands into a complex one.

Cons:
 The code may become more complicated since you're introducing a whole new
 layer between senders and receivers.
 Relations with Other Patterns
Chain of Responsibility, Command, Mediator and Observer address various
ways of connecting senders and receivers of requests:

Chain of Responsibility passes a request sequentially along a dynamic chain
of potential receivers until one of them handles it.
Command establishes unidirectional connections between senders and receivers.
Mediator eliminates direct connections between senders and receivers,
forcing them to communicate indirectly via a mediator object.
Observer lets receivers dynamically subscribe to and unsubscribe
from receiving requests.
Handlers in Chain of Responsibility can be implemented as Commands.
In this case, you can execute a lot of different operations over the same
context object, represented by a request.

However, there's another approach, where the request itself is a
Command object. In this case, you can execute the same operation
in a series of different contexts linked into a chain.

You can use Command and Memento together when implementing “undo”.
In this case, commands are responsible for performing various
operations over a target object, while mementos save the state of that
object just before a command gets executed.

Command and Strategy may look similar because you can use both to
parameterize an object with some action. However, they have very
different intents.

You can use Command to convert any operation into an object.
The operation's parameters become fields of that object. The
conversion lets you defer execution of the operation, queue it,
store the history of commands, send commands to remote services, etc.

On the other hand, Strategy usually describes different ways of doing
the same thing, letting you swap these algorithms within a single context
class.

Prototype can help when you need to save copies of Commands into history.

You can treat Visitor as a powerful version of the Command pattern.
Its objects can execute operations over various objects of different classes.

"""


from __future__ import annotations
from abc import ABC, abstractmethod


class Command(ABC):
    """
    The Command interface declares a method for executing a command.
    """

    @abstractmethod
    def execute(self) -> None:
        pass


class SimpleCommand(Command):
    """
    Some commands can implement simple operations on their own.
    """

    def __init__(self, payload: str) -> None:
        self._payload = payload

    def execute(self) -> None:
        print(f"SimpleCommand: See, I can do simple things like printing"
              f"({self._payload})")


class ComplexCommand(Command):
    """
    However, some commands can delegate more complex operations to other
    objects, called "receivers."
    """

    def __init__(self, receiver: Receiver, a: str, b: str) -> None:
        """
        Complex commands can accept one or several receiver objects along with
        any context data via the constructor.
        """

        self._receiver = receiver
        self._a = a
        self._b = b

    def execute(self) -> None:
        """
        Commands can delegate to any methods of a receiver.
        """

        print(
            "ComplexCommand: Complex stuff should "
            "be done by a receiver object", end=""
        )
        self._receiver.do_something(self._a)
        self._receiver.do_something_else(self._b)


class Receiver:
    """
    The Receiver classes contain some important business logic.
    They know how to perform all kinds of operations,
    associated with carrying out a request. In fact,
    any class may serve as a Receiver.
    """

    def do_something(self, a: str) -> None:
        print(f"\nReceiver: Working on ({a}.)", end="")

    def do_something_else(self, b: str) -> None:
        print(f"\nReceiver: Also working on ({b}.)", end="")


class Invoker:
    """
    The Invoker is associated with one or several commands. It sends a request
    to the command.
    """

    _on_start = None
    _on_finish = None

    """
    Initialize commands.
    """

    def set_on_start(self, command: Command):
        self._on_start = command

    def set_on_finish(self, command: Command):
        self._on_finish = command

    def do_something_important(self) -> None:
        """
        The Invoker does not depend on concrete command or receiver classes.
        The Invoker passes a request to a receiver indirectly,
        by executing a command.
        """

        print("Invoker: Does anybody want something done before I begin?")
        if isinstance(self._on_start, Command):
            self._on_start.execute()

        print("Invoker: ...doing something really important...")

        print("Invoker: Does anybody want something done after I finish?")
        if isinstance(self._on_finish, Command):
            self._on_finish.execute()


if __name__ == "__main__":
    """
    The client code can parameterize an invoker with any commands.
    """

    invoker = Invoker()
    invoker.set_on_start(SimpleCommand("Say Hi!"))
    receiver = Receiver()

    invoker.set_on_finish(
        ComplexCommand(receiver, "Send email", "Save report")
    )

    invoker.do_something_important()
