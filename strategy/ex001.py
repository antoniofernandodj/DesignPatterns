"""
 Applicability
 Use the Strategy pattern when you want to use different variants of an
 algorithm within an object and be able to switch from one algorithm to
 another during runtime.

 The Strategy pattern lets you indirectly alter the object's behavior at
 runtime by associating it with different sub-objects which can perform
 specific sub-tasks in different ways.

 Use the Strategy when you have a lot of similar classes that only differ in
 the way they execute some behavior.

 The Strategy pattern lets you extract the varying behavior into a separate
 class hierarchy and combine the original classes into one, thereby reducing
 duplicate code.

 Use the pattern to isolate the business logic of a class from the
 implementation details of algorithms that may not be as important in the
 context of that logic.

 The Strategy pattern lets you isolate the code, internal data,
 and dependencies of various algorithms from the rest of the code.
 Various clients get a simple interface to execute the algorithms and
 switch them at runtime.

 Use the pattern when your class has a massive conditional statement that
 switches between different variants of the same algorithm.

 The Strategy pattern lets you do away with such a conditional by extracting
 all algorithms into separate classes, all of which implement the same
 interface. The original object delegates execution to one of these objects,
 instead of implementing all variants of the algorithm.

 How to Implement
In the context class, identify an algorithm that's prone to frequent changes.
It may also be a massive conditional that selects and executes a variant of
the same algorithm at runtime.

Declare the strategy interface common to all variants of the algorithm.

One by one, extract all algorithms into their own classes. They should all
implement the strategy interface.

In the context class, add a field for storing a reference to a strategy object.
Provide a setter for replacing values of that field. The context should work
with the strategy object only via the strategy interface. The context may
define an interface which lets the strategy access its data.

Clients of the context must associate it with a suitable strategy that matches
the way they expect the context to perform its primary job.

 Pros and Cons

Pros:
 You can swap algorithms used inside an object at runtime.
 You can isolate the implementation details of an algorithm from the code that
 uses it.
 You can replace inheritance with composition.
 Open/Closed Principle. You can introduce new strategies without having to
 change the context.

Cons:
 If you only have a couple of algorithms and they rarely change, there's no
 real reason to overcomplicate the program with new classes and interfaces
 that come along with the pattern.
 Clients must be aware of the differences between strategies to be able to
 select a proper one.
 A lot of modern programming languages have functional type support that
 lets you implement different versions of an algorithm inside a set of
 anonymous functions. Then you could use these functions exactly as you'd
 have used the strategy objects, but without bloating your code with extra
 classes and interfaces.
 Relations with Other Patterns
Bridge, State, Strategy (and to some degree Adapter) have very similar
structures. Indeed, all of these patterns are based on composition,
which is delegating work to other objects. However, they all solve
different problems. A pattern isn't just a recipe for structuring your
code in a specific way. It can also communicate to other developers
the problem the pattern solves.

Command and Strategy may look similar because you can use both to parameterize
an object with some action. However, they have very different intents.

You can use Command to convert any operation into an object. The operation's
parameters become fields of that object. The conversion lets you defer
execution of the operation, queue it, store the history of commands,
send commands to remote services, etc.

On the other hand, Strategy usually describes different ways of doing the same
thing, letting you swap these algorithms within a single context class.

Decorator lets you change the skin of an object, while Strategy lets you
change the guts.

Template Method is based on inheritance: it lets you alter parts of an
algorithm by extending those parts in subclasses. Strategy is based on
composition: you can alter parts of the object's behavior by supplying
it with different strategies that correspond to that behavior.
Template Method works at the class level, so it's static. Strategy
works on the object level, letting you switch behaviors at runtime.

State can be considered as an extension of Strategy. Both patterns are
based on composition: they change the behavior of the context by
delegating some work to helper objects. Strategy makes these objects
completely independent and unaware of each other. However, State doesn't
restrict dependencies between concrete states, letting them alter the
state of the context at will.
"""


from abc import ABC, abstractmethod


# Step 1: Create the DiscountStrategy interface
class DiscountStrategy(ABC):

    @abstractmethod
    def apply_discount(self, total: float) -> float:
        pass


# Step 2: Implement the discount strategies
class NoDiscount(DiscountStrategy):
    def __init__(self):
        pass

    def apply_discount(self, total: float) -> float:
        return total


class PercentageDiscount(DiscountStrategy):
    def __init__(self, value):
        self.value = value

    def apply_discount(self, total: float) -> float:
        r = total - self.value/100 * total
        return r


class FixedAmountDiscount(DiscountStrategy):
    def __init__(self, value):
        self.value = value

    def apply_discount(self, total: float) -> float:
        r = total - self.value
        return r


# TODO: Implement NoDiscount, PercentageDiscount,
# and FixedAmountDiscount classes

# Step 3: Implement the ShoppingCart class
class ShoppingCart:

    def __init__(self, discount_strategy):
        # TODO: Initialize the shopping cart with the given discount_strategy
        # and an empty items dictionary
        self.discount_strategy = discount_strategy
        self.items = {}

    def add_item(self, item: str, price: float):
        # TODO: Add the item with its price to the items dictionary
        self.items[item] = price

    def remove_item(self, item: str):
        # TODO: Remove the item from the items dictionary if it exists
        self.items.pop(item, None)

    def get_total(self) -> float:
        return sum(list(self.items.values()))

    def get_total_after_discount(self) -> float:
        return self.discount_strategy.apply_discount(self.get_total())


# Step 4: Test your implementation
if __name__ == "__main__":
    # TODO: Create a shopping cart with a discount strategy
    cart = ShoppingCart(FixedAmountDiscount(10))

    # TODO: Add a few items
    cart.add_item("Item 1", 10.0)
    cart.add_item("Item 2", 20.0)
    cart.add_item("Item 3", 30.0)

    # TODO: Calculate and print the total price before discount
    print("Total before discount:", cart.get_total())

    # TODO: Calculate and print the total price after applying the discount
    print("Total after discount:", cart.get_total_after_discount())
