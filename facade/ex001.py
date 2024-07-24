from __future__ import annotations


"""
Applicability
 Use the Facade pattern when you need to have a limited but straightforward
 interface to a complex subsystem.

 Often, subsystems get more complex over time. Even applying design patterns
 typically leads to creating more classes. A subsystem may become more
 flexible and easier to reuse in various contexts, but the amount of
 configuration and boilerplate code it demands from a client grows ever
 larger. The Facade attempts to fix this problem by providing a shortcut
 to the most-used features of the subsystem which fit most client requirements.

 Use the Facade when you want to structure a subsystem into layers.

 Create facades to define entry points to each level of a subsystem.
 You can reduce coupling between multiple subsystems by requiring them
 to communicate only through facades.

For example, let's return to our video conversion framework. It can be
broken down into two layers: video- and audio-related. For each layer,
you can create a facade and then make the classes of each layer communicate
with each other via those facades. This approach looks very similar to the
Mediator pattern.

 How to Implement
Check whether it's possible to provide a simpler interface than what an
existing subsystem already provides. You're on the right track if this
interface makes the client code independent from many of the subsystem's
classes.

Declare and implement this interface in a new facade class. The facade should
redirect the calls from the client code to appropriate objects of the
subsystem. The facade should be responsible for initializing the subsystem
and managing its further life cycle unless the client code already does this.

To get the full benefit from the pattern, make all the client code communicate
with the subsystem only via the facade. Now the client code is protected from
any changes in the subsystem code. For example, when a subsystem gets upgraded
to a new version, you will only need to modify the code in the facade.

If the facade becomes too big, consider extracting part of its behavior to a
new, refined facade class.

 Pros and Cons

Pros:
 You can isolate your code from the complexity of a subsystem.

Cons:
 A facade can become a god object coupled to all classes of an app.


 Relations with Other Patterns
Facade defines a new interface for existing objects, whereas Adapter tries
to make the existing interface usable. Adapter usually wraps just one object,
while Facade works with an entire subsystem of objects.

Abstract Factory can serve as an alternative to Facade when you only want
to hide the way the subsystem objects are created from the client code.

Flyweight shows how to make lots of little objects, whereas Facade shows
how to make a single object that represents an entire subsystem.

Facade and Mediator have similar jobs: they try to organize collaboration
between lots of tightly coupled classes.

Facade defines a simplified interface to a subsystem of objects, but it
doesn't introduce any new functionality. The subsystem itself is unaware of
the facade. Objects within the subsystem can communicate directly.
Mediator centralizes communication between components of the system.
The components only know about the mediator object and don't communicate
directly.
A Facade class can often be transformed into a Singleton since a single
facade object is sufficient in most cases.

Facade is similar to Proxy in that both buffer a complex entity and initialize
it on its own. Unlike Facade, Proxy has the same interface as its service
object, which makes them interchangeable.
"""


class Facade:
    """
    The Facade class provides a simple interface to the complex logic of one or
    several subsystems. The Facade delegates the client requests to the
    appropriate objects within the subsystem. The Facade is also responsible
    for managing their lifecycle. All of this shields the client from
    the undesired complexity of the subsystem.
    """

    def __init__(self, subsystem1: Subsystem1, subsystem2: Subsystem2) -> None:
        """
        Depending on your application's needs, you can provide the Facade with
        existing subsystem objects or force the Facade to create them on its
        own.
        """

        self._subsystem1 = subsystem1 or Subsystem1()
        self._subsystem2 = subsystem2 or Subsystem2()

    def operation(self) -> str:
        """
        The Facade's methods are convenient shortcuts to the sophisticated
        functionality of the subsystems. However, clients get only
        to a fraction of a subsystem's capabilities.
        """

        results = []
        results.append("Facade initializes subsystems:")
        results.append(self._subsystem1.operation1())
        results.append(self._subsystem2.operation1())
        results.append("Facade orders subsystems to perform the action:")
        results.append(self._subsystem1.operation_n())
        results.append(self._subsystem2.operation_z())
        return "\n".join(results)


class Subsystem1:
    """
    The Subsystem can accept requests either from the facade or
    client directly. In any case, to the Subsystem, the Facade is
    yet another client, and it's not a part of the Subsystem.
    """

    def operation1(self) -> str:
        return "Subsystem1: Ready!"

    # ...

    def operation_n(self) -> str:
        return "Subsystem1: Go!"


class Subsystem2:
    """
    Some facades can work with multiple subsystems at the same time.
    """

    def operation1(self) -> str:
        return "Subsystem2: Get ready!"

    # ...

    def operation_z(self) -> str:
        return "Subsystem2: Fire!"


def client_code(facade: Facade) -> None:
    """
    The client code works with complex subsystems through a simple interface
    provided by the Facade. When a facade manages the lifecycle of the
    subsystem, the client might not even know about the existence of the
    subsystem. This approach lets you keep the complexity under control.
    """

    print(facade.operation(), end="")


if __name__ == "__main__":
    # The client code may have some of the subsystem's objects already created.
    # In this case, it might be worthwhile to initialize the Facade with these
    # objects instead of letting the Facade create new instances.
    subsystem1 = Subsystem1()
    subsystem2 = Subsystem2()
    facade = Facade(subsystem1, subsystem2)
    client_code(facade)
