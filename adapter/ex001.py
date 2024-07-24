"""
Applicability
 Use the Adapter class when you want to use some existing class,
 but its interface isn't compatible with the rest of your code.

 The Adapter pattern lets you create a middle-layer class
 that serves as a translator between your code and a legacy class, a
 3rd-party class or any other class with a weird interface.

 Use the pattern when you want to reuse several existing subclasses
 that lack some common functionality that can't be added to the superclass.

 You could extend each subclass and put the missing functionality
 into new child classes. However, you'll need to duplicate the code
 across all of these new classes, which smells really bad.

The much more elegant solution would be to put the missing
functionality into an adapter class. Then you would wrap objects
with missing features inside the adapter, gaining needed features
dynamically. For this to work, the target classes must have a
common interface, and the adapter's field should follow that
interface. This approach looks very similar to the Decorator pattern.

 How to Implement
Make sure that you have at least two classes with incompatible interfaces:

A useful service class, which you can't change (often 3rd-party,
legacy or with lots of existing dependencies).
One or several client classes that would benefit from using the service class.
Declare the client interface and describe how clients communicate
with the service.

Create the adapter class and make it follow the client interface.
Leave all the methods empty for now.

Add a field to the adapter class to store a reference to the service
object. The common practice is to initialize this field via the constructor,
but sometimes it's more convenient to pass it to the adapter
when calling its methods.

One by one, implement all methods of the client interface in the
adapter class. The adapter should delegate most of the real work to
the service object, handling only the interface or data format conversion.

Clients should use the adapter via the client interface.
This will let you change or extend the adapters without
affecting the client code.

 Pros and Cons

 Pros:
 Single Responsibility Principle. You can separate the
    interface or data conversion code from the primary business
    logic of the program.
 Open/Closed Principle. You can introduce new types of
    adapters into the program without breaking the existing
    client code, as long as they work with the adapters through the
    client interface.

 Cons:
 The overall complexity of the code increases because you need to
 introduce a set of new interfaces and classes. Sometimes it's simpler
 just to change the service class so that it matches the rest of your code.
 Relations with Other Patterns
Bridge is usually designed up-front, letting you develop parts of an
application independently of each other. On the other hand,
Adapter is commonly used with an existing app to make some
otherwise-incompatible classes work together nicely.

Adapter provides a completely different interface for accessing an
existing object. On the other hand, with the Decorator pattern the
interface either stays the same or gets extended. In addition,
Decorator supports recursive composition, which isn't possible when
you use Adapter.

With Adapter you access an existing object via different interface.
With Proxy, the interface stays the same. With Decorator you access
the object via an enhanced interface.

Facade defines a new interface for existing objects, whereas Adapter
tries to make the existing interface usable. Adapter usually wraps
just one object, while Facade works with an entire subsystem of objects.

Bridge, State, Strategy (and to some degree Adapter) have very
similar structures. Indeed, all of these patterns are based on
composition, which is delegating work to other objects. However,
they all solve different problems. A pattern isn't just a recipe
for structuring your code in a specific way. It can also
communicate to other developers the problem the pattern solves.

"""


class Target:
    """
    The Target defines the domain-specific interface used by the client code.
    """

    def request(self) -> str:
        return "Target: The default target's behavior."


class Adaptee:
    """
    The Adaptee contains some useful behavior, but its interface
    is incompatible with the existing client code. The Adaptee
    needs some adaptation before the client code can use it.
    """

    def specific_request(self) -> str:
        return ".eetpadA eht fo roivaheb laicepS"


class Adapter(Target, Adaptee):
    """
    The Adapter makes the Adaptee's interface compatible with the Target's
    interface via multiple inheritance.
    """

    def request(self) -> str:
        return f"Adapter: (TRANSLATED) {self.specific_request()[::-1]}"


def client_code(target: "Target") -> None:
    """
    The client code supports all classes that follow the Target interface.
    """

    print(target.request(), end="\n\n")


if __name__ == "__main__":
    print("Client: I can work just fine with the Target objects:")
    target = Target()
    client_code(target)

    adaptee = Adaptee()
    print("Client: The Adaptee class has a weird interface. "
          "See, I don't understand it:")

    print(f"Adaptee: {adaptee.specific_request()}", end="\n\n")

    print("Client: But I can work with it via the Adapter:")
    adapter = Adapter()
    client_code(adapter)
