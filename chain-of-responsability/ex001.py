"""
Applicability
 Use the Chain of Responsibility pattern when your program is expected to
 process different kinds of requests in various ways, but the exact types
 of requests and their sequences are unknown beforehand.

 The pattern lets you link several handlers into one chain and, upon
 receiving a request, “ask” each handler whether it can process it.
 This way all handlers get a chance to process the request.

 Use the pattern when it's essential to execute several handlers in a
 particular order.

 Since you can link the handlers in the chain in any order, all requests
 will get through the chain exactly as you planned.

 Use the CoR pattern when the set of handlers and their order are supposed
 to change at runtime.

 If you provide setters for a reference field inside the handler classes,
 you'll be able to insert, remove or reorder handlers dynamically.

 How to Implement
Declare the handler interface and describe the signature of a method for
handling requests.

Decide how the client will pass the request data into the method. The most
flexible way is to convert the request into an object and pass it to the
handling method as an argument.

To eliminate duplicate boilerplate code in concrete handlers, it might be
worth creating an abstract base handler class, derived from the handler
interface.

This class should have a field for storing a reference to the next handler
in the chain. Consider making the class immutable. However, if you plan to
modify chains at runtime, you need to define a setter for altering the value
of the reference field.

You can also implement the convenient default behavior for the handling
method, which is to forward the request to the next object unless
there's none left. Concrete handlers will be able to use this behavior
by calling the parent method.

One by one create concrete handler subclasses and implement their handling
methods. Each handler should make two decisions when receiving a request:

Whether it'll process the request.
Whether it'll pass the request along the chain.
The client may either assemble chains on its own or receive pre-built chains
from other objects. In the latter case, you must implement some factory
classes to build chains according to the configuration or environment settings.

The client may trigger any handler in the chain, not just the first one.
The request will be passed along the chain until some handler refuses to
pass it further or until it reaches the end of the chain.

Due to the dynamic nature of the chain, the client should be ready to
handle the following scenarios:

The chain may consist of a single link.
Some requests may not reach the end of the chain.
Others may reach the end of the chain unhandled.

 Pros and Cons

 Pros:
 You can control the order of request handling.
 Single Responsibility Principle. You can decouple classes that invoke
 operations from classes that perform operations.
 Open/Closed Principle. You can introduce new handlers into the app without
 breaking the existing client code.

 Cons:
 Some requests may end up unhandled.
 Relations with Other Patterns
Chain of Responsibility, Command, Mediator and Observer address various
ways of connecting senders and receivers of requests:

Chain of Responsibility passes a request sequentially along a dynamic
chain of potential receivers until one of them handles it.
Command establishes unidirectional connections between senders and receivers.
Mediator eliminates direct connections between senders and receivers,
forcing them to communicate indirectly via a mediator object.
Observer lets receivers dynamically subscribe to and unsubscribe from
receiving requests.
Chain of Responsibility is often used in conjunction with Composite.
In this case, when a leaf component gets a request, it may pass it through
the chain of all of the parent components down to the root of the object tree.

Handlers in Chain of Responsibility can be implemented as Commands.
In this case, you can execute a lot of different operations over the same
context object, represented by a request.

However, there's another approach, where the request itself is a Command
object. In this case, you can execute the same operation in a series of
different contexts linked into a chain.

Chain of Responsibility and Decorator have very similar class structures.
Both patterns rely on recursive composition to pass the execution through
a series of objects. However, there are several crucial differences.

The CoR handlers can execute arbitrary operations independently of
each other. They can also stop passing the request further at any
point. On the other hand, various Decorators can extend the object's
behavior while keeping it consistent with the base interface.
In addition, decorators aren't allowed to break the flow of the request.

"""


from __future__ import annotations
from abc import ABC, abstractmethod
from typing import Any, Optional


class Handler(ABC):
    """
    The Handler interface declares a method for building the chain of handlers.
    It also declares a method for executing a request.
    """

    @abstractmethod
    def set_next(self, handler: Handler) -> Handler:
        pass

    @abstractmethod
    def handle(self, request) -> Optional[str]:
        pass


class AbstractHandler(Handler):
    """
    The default chaining behavior can be implemented inside a base handler
    class.
    """

    _next_handler: Optional[Handler] = None

    def set_next(self, handler: Handler) -> Handler:
        self._next_handler = handler
        # Returning a handler from here will let us link handlers in a
        # convenient way like this:
        # monkey.set_next(squirrel).set_next(dog)
        return handler

    @abstractmethod
    def handle(self, request: Any) -> Optional[str]:
        if self._next_handler:
            return self._next_handler.handle(request)

        return None


"""
All Concrete Handlers either handle a request or pass it to the next handler in
the chain.
"""


class MonkeyHandler(AbstractHandler):
    def handle(self, request: Any) -> Optional[str]:
        if request == "Banana":
            return f"Monkey: I'll eat the {request}"
        else:
            return super().handle(request)


class SquirrelHandler(AbstractHandler):
    def handle(self, request: Any) -> Optional[str]:
        if request == "Nut":
            return f"Squirrel: I'll eat the {request}"
        else:
            return super().handle(request)


class DogHandler(AbstractHandler):
    def handle(self, request: Any) -> Optional[str]:
        if request == "MeatBall":
            return f"Dog: I'll eat the {request}"
        else:
            return super().handle(request)


def client_code(handler: Handler) -> None:
    """
    The client code is usually suited to work with a single handler. In most
    cases, it is not even aware that the handler is part of a chain.
    """

    for food in ["Nut", "Banana", "Cup of coffee"]:
        print(f"\nClient: Who wants a {food}?")
        result = handler.handle(food)
        if result:
            print(f"  {result}", end="")
        else:
            print(f"  {food} was left untouched.", end="")


if __name__ == "__main__":
    monkey = MonkeyHandler()
    squirrel = SquirrelHandler()
    dog = DogHandler()

    (
        monkey
        .set_next(squirrel)
        .set_next(dog)
    )

    # The client should be able to send a request to any handler, not just the
    # first one in the chain.
    print("Chain: Monkey > Squirrel > Dog")
    client_code(monkey)
    print("\n")

    print("Subchain: Squirrel > Dog")
    client_code(squirrel)
