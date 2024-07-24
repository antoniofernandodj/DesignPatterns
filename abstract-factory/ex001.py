"""
Applicability
 Use the Abstract Factory when your code needs to work with various families
 of related products, but you don't want it to depend on the concrete classes
 of those products—they might be unknown beforehand or you simply want to
 allow for future extensibility.

 The Abstract Factory provides you with an interface for creating objects from
 each class of the product family. As long as your code creates objects
 via this interface, you don't have to worry about creating the wrong variant
 of a product which doesn't match the products already created by your app.

 Consider implementing the Abstract Factory when you have a class with a set
 of Factory Methods that blur its primary responsibility.

 In a well-designed program each class is responsible only for one thing.
 When a class deals with multiple product types, it may be worth extracting
 its factory methods into a stand-alone factory class or a full-blown
 Abstract Factory implementation.

 How to Implement
Map out a matrix of distinct product types versus variants of these products.

Declare abstract product interfaces for all product types. Then make all
concrete product classes implement these interfaces.

Declare the abstract factory interface with a set of creation methods for all
abstract products.

Implement a set of concrete factory classes, one for each product variant.

Create factory initialization code somewhere in the app. It should instantiate
one of the concrete factory classes, depending on the application
configuration or the current environment. Pass this factory object to all
classes that construct products.

Scan through the code and find all direct calls to product constructors.
Replace them with calls to the appropriate creation method on the factory
object.

 Pros and Cons
 You can be sure that the products you're getting from a factory are
 compatible with each other.
 You avoid tight coupling between concrete products and client code.
 Single Responsibility Principle. You can extract the product creation
 code into one place, making the code easier to support.
 Open/Closed Principle. You can introduce new variants of products
 without breaking existing client code.
 The code may become more complicated than it should be, since a lot of
 new interfaces and classes are introduced along with the pattern.
 Relations with Other Patterns
Many designs start by using Factory Method (less complicated and more
customizable via subclasses) and evolve toward Abstract Factory,
Prototype, or Builder (more flexible, but more complicated).

Builder focuses on constructing complex objects step by step.
Abstract Factory specializes in creating families of related objects.
Abstract Factory returns the product immediately, whereas Builder
lets you run some additional construction steps before fetching the product.

Abstract Factory classes are often based on a set of Factory Methods,
but you can also use Prototype to compose the methods on these classes.

Abstract Factory can serve as an alternative to Facade when you only want to
hide the way the subsystem objects are created from the client code.

You can use Abstract Factory along with Bridge. This pairing is useful when
some abstractions defined by Bridge can only work with specific
implementations. In this case, Abstract Factory can encapsulate
these relations and hide the complexity from the client code.

Abstract Factories, Builders and Prototypes can all be implemented as
Singletons.

"""

from interface import GUIFactory
from win import WinFactory
from mac import MacFactory


def client_code(factory: GUIFactory):
    button = factory.create_button()
    checkbox = factory.create_checkbox()
    print(button.paint())
    print(checkbox.paint())


client_code(WinFactory())
client_code(MacFactory())
