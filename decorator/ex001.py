import time


"""
Applicability
 Use the Decorator pattern when you need to be able to assign extra behaviors
 to objects at runtime without breaking the code that uses these objects.

 The Decorator lets you structure your business logic into layers, create
 a decorator for each layer and compose objects with various combinations
 of this logic at runtime. The client code can treat all these objects in
 the same way, since they all follow a common interface.

 Use the pattern when it's awkward or not possible to extend an object's
 behavior using inheritance.

 Many programming languages have the final keyword that can be used to
 prevent further extension of a class. For a final class, the only way to
 reuse the existing behavior would be to wrap the class with your own wrapper,
 using the Decorator pattern.

 How to Implement
Make sure your business domain can be represented as a primary component
with multiple optional layers over it.

Figure out what methods are common to both the primary component and
the optional layers. Create a component interface and declare those
methods there.

Create a concrete component class and define the base behavior in it.

Create a base decorator class. It should have a field for storing a
reference to a wrapped object. The field should be declared with the component
interface type to allow linking to concrete components as well as decorators.
The base decorator must delegate all work to the wrapped object.

Make sure all classes implement the component interface.

Create concrete decorators by extending them from the base decorator.
A concrete decorator must execute its behavior before or after the call to the
parent method (which always delegates to the wrapped object).

The client code must be responsible for creating decorators and composing them
in the way the client needs.


Pros and Cons

Pros:
 You can extend an object's behavior without making a new subclass.
 You can add or remove responsibilities from an object at runtime.
 You can combine several behaviors by wrapping an object into multiple
 decorators.
 Single Responsibility Principle. You can divide a monolithic class that
 implements many possible variants of behavior into several smaller classes.

 Cons:
It's hard to remove a specific wrapper from the wrappers stack.
 It's hard to implement a decorator in such a way that its behavior
 doesn't depend on the order in the decorators stack.
 The initial configuration code of layers might look pretty ugly.


 Relations with Other Patterns
Adapter provides a completely different interface for accessing an existing
object. On the other hand, with the Decorator pattern the interface either
stays the same or gets extended. In addition, Decorator supports recursive
composition, which isn't possible when you use Adapter.

With Adapter you access an existing object via different interface.
With Proxy, the interface stays the same. With Decorator you access the object
via an enhanced interface.

Chain of Responsibility and Decorator have very similar class structures.
Both patterns rely on recursive composition to pass the execution through a
series of objects. However, there are several crucial differences.

The CoR handlers can execute arbitrary operations independently of each
other. They can also stop passing the request further at any point.
On the other hand, various Decorators can extend the object's behavior
while keeping it consistent with the base interface. In addition,
decorators aren't allowed to break the flow of the request.

Composite and Decorator have similar structure diagrams since both rely
on recursive composition to organize an open-ended number of objects.

A Decorator is like a Composite but only has one child component.
There's another significant difference: Decorator adds additional
responsibilities to the wrapped object, while Composite just “sums up”
its children's results.

However, the patterns can also cooperate: you can use Decorator
to extend the behavior of a specific object in the Composite tree.

Designs that make heavy use of Composite and Decorator can often
benefit from using Prototype. Applying the pattern lets you clone
complex structures instead of re-constructing them from scratch.

Decorator lets you change the skin of an object, while Strategy
lets you change the guts.

Decorator and Proxy have similar structures, but very different intents.
Both patterns are built on the composition principle, where one object
is supposed to delegate some of the work to another. The difference is
that a Proxy usually manages the life cycle of its service object on its
own, whereas the composition of Decorators is always controlled by the client.

"""


class Instant:
    def __init__(self) -> None:
        self.start = time.perf_counter()

    def elapsed_s(self):
        return (time.perf_counter() - self.start)

    def elapsed_micr_s(self):
        return (time.perf_counter() - self.start) * 1_000_000

    def elapsed_ms(self):
        return (time.perf_counter() - self.start) * 1_000

    @staticmethod
    def now() -> 'Instant':
        return Instant()


def d(f):
    def inner():
        start = Instant.now()
        f()
        print(f"Time: {start.elapsed_ms()} ms")
    return inner


def do_something():
    i = 1
    for j in range(1, 21):
        i *= j
    print(f"Result: {i}")


def main():
    print("Starting to count to 1M")
    decorated_do_something = d(do_something)
    decorated_do_something()


if __name__ == "__main__":
    main()
