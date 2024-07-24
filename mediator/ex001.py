from __future__ import annotations
from abc import ABC
from typing import Optional


"""

Applicability
 Use the Mediator pattern when it's hard to change some of the classes because
 they are tightly coupled to a bunch of other classes.

 The pattern lets you extract all the relationships between classes into a
 separate class, isolating any changes to a specific component from the rest
 of the components.

 Use the pattern when you can't reuse a component in a different program
 because it's too dependent on other components.

 After you apply the Mediator, individual components become unaware of the
 other components. They could still communicate with each other, albeit
 indirectly, through a mediator object. To reuse a component in a different
 app, you need to provide it with a new mediator class.

 Use the Mediator when you find yourself creating tons of component subclasses
 just to reuse some basic behavior in various contexts.

 Since all relations between components are contained within the mediator,
 it's easy to define entirely new ways for these components to collaborate by
 introducing new mediator classes, without having to change the components
 themselves.

 How to Implement
Identify a group of tightly coupled classes which would benefit from being
more independent (e.g., for easier maintenance or simpler reuse of these
classes).

Declare the mediator interface and describe the desired communication protocol
between mediators and various components. In most cases, a single method for
receiving notifications from components is sufficient.

This interface is crucial when you want to reuse component classes in
different contexts. As long as the component works with its mediator via the
generic interface, you can link the component with a different implementation
of the mediator.

Implement the concrete mediator class. Consider storing references to all
components inside the mediator. This way, you could call any component from
the mediator's methods.

You can go even further and make the mediator responsible for the creation and
destruction of component objects. After this, the mediator may resemble a
factory or a facade.

Components should store a reference to the mediator object. The connection is
usually established in the component's constructor, where a mediator object is
passed as an argument.

Change the components' code so that they call the mediator's notification
method instead of methods on other components. Extract the code that involves
calling other components into the mediator class. Execute this code whenever
the mediator receives notifications from that component.

 Pros and Cons

 Pros:
 Single Responsibility Principle. You can extract the communications between
 various components into a single place, making it easier to comprehend and
 maintain.
 Open/Closed Principle. You can introduce new mediators without having to
 change the actual components.
 You can reduce coupling between various components of a program.
 You can reuse individual components more easily.

 Cons:
 Over time a mediator can evolve into a God Object.
 Relations with Other Patterns
Chain of Responsibility, Command, Mediator and Observer address various ways
of connecting senders and receivers of requests:

Chain of Responsibility passes a request sequentially along a dynamic chain of
potential receivers until one of them handles it.
Command establishes unidirectional connections between senders and receivers.
Mediator eliminates direct connections between senders and receivers,
forcing them to communicate indirectly via a mediator object.
Observer lets receivers dynamically subscribe to and unsubscribe from
receiving requests.
Facade and Mediator have similar jobs: they try to organize collaboration
between lots of tightly coupled classes.

Facade defines a simplified interface to a subsystem of objects, but it
doesn't introduce any new functionality. The subsystem itself is unaware of
the facade. Objects within the subsystem can communicate directly.
Mediator centralizes communication between components of the system.
The components only know about the mediator object and don't communicate
directly.
The difference between Mediator and Observer is often elusive. In most cases,
you can implement either of these patterns; but sometimes you can apply both
simultaneously. Let's see how we can do that.

The primary goal of Mediator is to eliminate mutual dependencies among a
set of system components. Instead, these components become dependent on a
single mediator object. The goal of Observer is to establish dynamic one-way
connections between objects, where some objects act as subordinates of others.

There's a popular implementation of the Mediator pattern that relies on
Observer. The mediator object plays the role of publisher, and the components
act as subscribers which subscribe to and unsubscribe from the mediator's
events. When Mediator is implemented this way, it may look very similar to
Observer.

When you're confused, remember that you can implement the Mediator
pattern in other ways. For example, you can permanently link all the
components to the same mediator object. This implementation won't
resemble Observer but will still be an instance of the Mediator pattern.

Now imagine a program where all components have become publishers,
allowing dynamic connections between each other. There won't be a
centralized mediator object, only a distributed set of observers.

"""


class Mediator(ABC):
    """
    The Mediator interface declares a method used by components to notify the
    mediator about various events. The Mediator may react to these events and
    pass the execution to other components.
    """

    def notify(self, sender: object, event: str) -> None:
        pass


class ConcreteMediator(Mediator):
    def __init__(self, component1: Component1, component2: Component2) -> None:
        self._component1 = component1
        self._component1.mediator = self
        self._component2 = component2
        self._component2.mediator = self

    def notify(self, sender: object, event: str) -> None:
        if event == "A":
            print("Mediator reacts on A and triggers following operations:")
            self._component2.send_request("C")
        elif event == "D":
            print("Mediator reacts on D and triggers following operations:")
            self._component1.send_request("B")
            self._component2.send_request("C")


class BaseComponent:
    """
    The Base Component provides the basic functionality of storing a mediator's
    instance inside component objects.
    """

    def __init__(self, mediator: Optional[Mediator] = None) -> None:
        self._mediator = mediator

    @property
    def mediator(self) -> Optional[Mediator]:
        return self._mediator

    @mediator.setter
    def mediator(self, mediator: Mediator) -> None:
        self._mediator = mediator


"""
Concrete Components implement various functionality. They don't depend on other
components. They also don't depend on any concrete mediator classes.
"""


class Component1(BaseComponent):
    def send_request(self, request) -> None:
        print(f"Component 1 does {request}.")
        if self.mediator is None:
            raise TypeError

        self.mediator.notify(self, request)


class Component2(BaseComponent):
    def send_request(self, request) -> None:
        print(f"Component 2 does {request}.")
        if self.mediator is None:
            raise TypeError

        self.mediator.notify(self, request)


if __name__ == "__main__":
    # The client code.
    c1 = Component1()
    c2 = Component2()
    mediator = ConcreteMediator(c1, c2)

    print("Client triggers operation A.")
    c1.send_request("A")

    print("\n", end="")

    print("Client triggers operation D.")
    c2.send_request("D")
