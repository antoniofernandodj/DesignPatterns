"""
 Applicability
 Use the Builder pattern to get rid of a “telescoping constructor”.

 Say you have a constructor with ten optional parameters. Calling such a
 beast is very inconvenient; therefore, you overload the constructor and
 create several shorter versions with fewer parameters. These constructors
 still refer to the main one, passing some default values into any
 omitted parameters.

class Pizza {
    Pizza(int size) { ... }
    Pizza(int size, boolean cheese) { ... }
    Pizza(int size, boolean cheese, boolean pepperoni) { ... }
    // ...
Creating such a monster is only possible in languages that support method
overloading, such as C# or Java.

The Builder pattern lets you build objects step by step, using only
those steps that you really need. After implementing the pattern,
you don't have to cram dozens of parameters into your constructors anymore.

 Use the Builder pattern when you want your code to be able to create
 different representations of some product (for example, stone and
 wooden houses).

 The Builder pattern can be applied when construction of various
 representations of the product involves similar steps that differ
 only in the details.

The base builder interface defines all possible construction steps,
and concrete builders implement these steps to construct particular
representations of the product. Meanwhile, the director class guides
the order of construction.

 Use the Builder to construct Composite trees or other complex objects.

 The Builder pattern lets you construct products step-by-step. You could
 defer execution of some steps without breaking the final product.
 You can even call steps recursively, which comes in handy when you need
 to build an object tree.

A builder doesn't expose the unfinished product while running construction
steps. This prevents the client code from fetching an incomplete result.

 How to Implement
Make sure that you can clearly define the common construction steps for
building all available product representations. Otherwise, you won't
be able to proceed with implementing the pattern.

Declare these steps in the base builder interface.

Create a concrete builder class for each of the product representations and
implement their construction steps.

Don't forget about implementing a method for fetching the result of
the construction. The reason why this method can't be declared inside the
builder interface is that various builders may construct products
that don't have a common interface. Therefore, you don't know what
would be the return type for such a method. However, if you're
dealing with products from a single hierarchy, the fetching method
can be safely added to the base interface.

Think about creating a director class. It may encapsulate various
ways to construct a product using the same builder object.

The client code creates both the builder and the director objects.
Before construction starts, the client must pass a builder object
to the director. Usually, the client does this only once, via parameters
of the director's class constructor. The director uses the builder
object in all further construction. There's an alternative approach,
where the builder is passed to a specific product construction
method of the director.

The construction result can be obtained directly from the director
only if all products follow the same interface. Otherwise,
the client should fetch the result from the builder.

 Pros and Cons

 Pros:
 You can construct objects step-by-step, defer construction steps
 or run steps recursively.
 You can reuse the same construction code when building various
 representations of products.
 Single Responsibility Principle. You can isolate complex construction
 code from the business logic of the product.

 Cons:
 The overall complexity of the code increases since the pattern
 requires creating multiple new classes.
 Relations with Other Patterns
Many designs start by using Factory Method (less complicated and more
customizable via subclasses) and evolve toward Abstract Factory,
Prototype, or Builder (more flexible, but more complicated).

Builder focuses on constructing complex objects step by step.
Abstract Factory specializes in creating families of related objects.
Abstract Factory returns the product immediately, whereas Builder
lets you run some additional construction steps before fetching the product.

You can use Builder when creating complex Composite trees because
you can program its construction steps to work recursively.

You can combine Builder with Bridge: the director class plays
the role of the abstraction, while different builders act as implementations.

Abstract Factories, Builders and Prototypes can all be
implemented as Singletons.

"""


from abc import ABC, abstractmethod


class Computer:
    def __init__(self):
        self.processor = None
        self.memory = None
        self.storage = None
        self.graphics_card = None
        self.operating_system = None
        self.extras = None


class ComputerBuilder(ABC):
    @abstractmethod
    def add_processor(self, item):
        pass

    @abstractmethod
    def add_memory(self, item):
        pass

    @abstractmethod
    def add_storage(self, item):
        pass

    @abstractmethod
    def add_graphics_card(self, item):
        pass

    @abstractmethod
    def add_operating_system(self, item):
        pass

    @abstractmethod
    def add_extras(self, item):
        pass


class CustomComputerBuilder(ComputerBuilder):
    def __init__(self):
        self.computer = Computer()

    def add_processor(self, processor):
        self.computer.processor = processor

    def add_memory(self, memory):
        self.computer.memory = memory

    def add_storage(self, storage):
        self.computer.storage = storage

    def add_graphics_card(self, graphics_card):
        self.computer.graphics_card = graphics_card

    def add_operating_system(self, operating_system):
        self.computer.operating_system = operating_system

    def add_extras(self, extras):
        self.computer.extras = extras


class ComputerDirector:
    def __init__(self, builder: ComputerBuilder):
        self.builder = builder

    def build_computer(self, specs: dict):
        self.builder.add_processor(specs['processor'])
        self.builder.add_memory(specs['memory'])
        self.builder.add_storage(specs['storage'])
        self.builder.add_graphics_card(specs['graphics_card'])
        self.builder.add_operating_system(specs['operating_system'])
        self.builder.add_extras(specs['extras'])


# Helper function to test the computer building process
def test_computer_building(specs, expected_output):
    builder = CustomComputerBuilder()
    director = ComputerDirector(builder)
    director.build_computer(specs)
    computer = builder.computer
    assert (
        computer.__dict__ == expected_output
    ), f"Expected {expected_output}, but got {computer.__dict__}"


# Test cases
test_specs = {
    'processor': 'Intel Core i5',
    'memory': '8GB',
    'storage': '512GB SSD',
    'graphics_card': 'Integrated',
    'operating_system': 'Windows 11',
    'extras': ['Wi-Fi']
}

expected_output = {
    'processor': 'Intel Core i5',
    'memory': '8GB',
    'storage': '512GB SSD',
    'graphics_card': 'Integrated',
    'operating_system': 'Windows 11',
    'extras': ['Wi-Fi']
}

test_computer_building(test_specs, expected_output)

print("All tests passed!")
