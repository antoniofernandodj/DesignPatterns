import copy


"""
Prototype
Also known as: Clone
 Intent
Prototype is a creational design pattern that lets you copy existing objects
without making your code dependent on their classes.

Prototype Design Pattern
 Problem
Say you have an object, and you want to create an exact copy of it. How would
you do it? First, you have to create a new object of the same class. Then you
have to go through all the fields of the original object and copy their values
over to the new object.

Nice! But there's a catch. Not all objects can be copied that way because some
of the object's fields may be private and not visible from outside of the
object itself.

What can go wrong when copying things “from the outside"?” width=
Copying an object “from the outside” isn't always possible.

There's one more problem with the direct approach. Since you have to know the
object's class to create a duplicate, your code becomes dependent on that
class. If the extra dependency doesn't scare you, there's another catch.
Sometimes you only know the interface that the object follows,
but not its concrete class, when, for example, a parameter in a method accepts
any objects that follow some interface.

 Solution
The Prototype pattern delegates the cloning process to the actual objects that
are being cloned. The pattern declares a common interface for all objects that
support cloning. This interface lets you clone an object without coupling your
code to the class of that object. Usually, such an interface contains just a
single clone method.

The implementation of the clone method is very similar in all classes.
The method creates an object of the current class and carries over all of the
field values of the old object into the new one. You can even copy private
fields because most programming languages let objects access private fields of
other objects that belong to the same class.

An object that supports cloning is called a prototype. When your objects
have dozens of fields and hundreds of possible configurations, cloning them
might serve as an alternative to subclassing.

Pre-built prototypes
Pre-built prototypes can be an alternative to subclassing.

Here's how it works: you create a set of objects, configured in various ways.
When you need an object like the one you've configured, you just clone a
prototype instead of constructing a new object from scratch.

 Real-World Analogy
In real life, prototypes are used for performing various tests before starting
mass production of a product. However, in this case, prototypes don't
participate in any actual production, playing a passive role instead.

The cell division
The division of a cell.

Since industrial prototypes don't really copy themselves, a much closer
analogy to the pattern is the process of mitotic cell division (biology,
remember?). After mitotic division, a pair of identical cells is formed.
The original cell acts as a prototype and takes an active role in creating the
copy.

 Structure
Basic implementation
The structure of the Prototype design pattern
The Prototype interface declares the cloning methods. In most cases, it's a
single clone method.

The Concrete Prototype class implements the cloning method. In addition to
copying the original object's data to the clone, this method may also handle
some edge cases of the cloning process related to cloning linked objects,
untangling recursive dependencies, etc.

The Client can produce a copy of any object that follows the prototype
interface.

Prototype registry implementation
The prototype registry
The Prototype Registry provides an easy way to access frequently-used
prototypes. It stores a set of pre-built objects that are ready to be copied.
The simplest prototype registry is a name → prototype hash map. However,
if you need better search criteria than a simple name, you can build a much
more robust version of the registry.

 Pseudocode
In this example, the Prototype pattern lets you produce exact copies of
geometric objects, without coupling the code to their classes.

The structure of the Prototype pattern example
Cloning a set of objects that belong to a class hierarchy.

All shape classes follow the same interface, which provides a cloning method.
A subclass may call the parent's cloning method before copying its own field
values to the resulting object.

Applicability
 Use the Prototype pattern when your code shouldn't depend on the concrete
 classes of objects that you need to copy.

 This happens a lot when your code works with objects passed to you from
 3rd-party code via some interface. The concrete classes of these objects are
 unknown, and you couldn't depend on them even if you wanted to.

The Prototype pattern provides the client code with a general interface for
working with all objects that support cloning. This interface makes the client
code independent from the concrete classes of objects that it clones.

 Use the pattern when you want to reduce the number of subclasses that only
 differ in the way they initialize their respective objects.

 Suppose you have a complex class that requires a laborious configuration
 before it can be used. There are several common ways to configure this class,
 and this code is scattered through your app. To reduce the duplication, you
 create several subclasses and put every common configuration code into their
 constructors. You solved the duplication problem, but now you have lots of
 dummy subclasses.

The Prototype pattern lets you use a set of pre-built objects configured in
various ways as prototypes. Instead of instantiating a subclass that matches
some configuration, the client can simply look for an appropriate prototype
and clone it.

 How to Implement
Create the prototype interface and declare the clone method in it. Or just add
the method to all classes of an existing class hierarchy, if you have one.

A prototype class must define the alternative constructor that accepts an
object of that class as an argument. The constructor must copy the values of
all fields defined in the class from the passed object into the newly created
instance. If you're changing a subclass, you must call the parent constructor
to let the superclass handle the cloning of its private fields.

If your programming language doesn't support method overloading, you won't be
able to create a separate “prototype” constructor. Thus, copying the object's
data into the newly created clone will have to be performed within the clone
method. Still, having this code in a regular constructor is safer because the
resulting object is returned fully configured right after you call the new
operator.

The cloning method usually consists of just one line: running a new operator
with the prototypical version of the constructor. Note, that every class must
explicitly override the cloning method and use its own class name along with
the new operator. Otherwise, the cloning method may produce an object of a
parent class.

Optionally, create a centralized prototype registry to store a catalog of
frequently used prototypes.

You can implement the registry as a new factory class or put it in the base
prototype class with a static method for fetching the prototype. This method
should search for a prototype based on search criteria that the client code
passes to the method. The criteria might either be a simple string tag or a
complex set of search parameters. After the appropriate prototype is found,
the registry should clone it and return the copy to the client.

Finally, replace the direct calls to the subclasses' constructors with calls
to the factory method of the prototype registry.

Pros and Cons

Pros
 You can clone objects without coupling to their concrete classes.
 You can get rid of repeated initialization code in favor of cloning pre-built
    prototypes.
 You can produce complex objects more conveniently.
 You get an alternative to inheritance when dealing with configuration presets
    or complex objects.

Cons
  Cloning complex objects that have circular references might be very tricky.

Relations with Other Patterns
Many designs start by using Factory Method (less complicated and more
customizable via subclasses) and evolve toward Abstract Factory,
Prototype, or Builder (more flexible, but more complicated).

Abstract Factory classes are often based on a set of Factory Methods,
but you can also use Prototype to compose the methods on these classes.

Prototype can help when you need to save copies of Commands into history.

Designs that make heavy use of Composite and Decorator can often benefit
from using Prototype. Applying the pattern lets you clone complex structures
instead of re-constructing them from scratch.

Prototype isn't based on inheritance, so it doesn't have its drawbacks.
On the other hand, Prototype requires a complicated initialization of the
cloned object. Factory Method is based on inheritance but doesn't require an
initialization step.

Sometimes Prototype can be a simpler alternative to Memento. This works
if the object, the state of which you want to store in the history, is fairly
straightforward and doesn't have links to external resources, or the links
are easy to re-establish.

Abstract Factories, Builders and Prototypes can all be implemented as
Singletons.
"""


class SelfReferencingEntity:
    def __init__(self):
        self.parent = None

    def set_parent(self, parent):
        self.parent = parent


class SomeComponent:
    """
    Python provides its own interface of Prototype via `copy.copy` and
    `copy.deepcopy` functions. And any class that wants to implement custom
    implementations have to override `__copy__` and `__deepcopy__` member
    functions.
    """

    def __init__(self, some_int, some_list_of_objects, some_circular_ref):
        self.some_int = some_int
        self.some_list_of_objects = some_list_of_objects
        self.some_circular_ref = some_circular_ref

    def __copy__(self):
        """
        Create a shallow copy. This method will be called whenever someone
        calls `copy.copy` with this object and the returned value is returned
        as the new shallow copy.
        """

        # First, let's create copies of the nested objects.
        some_list_of_objects = copy.copy(self.some_list_of_objects)
        some_circular_ref = copy.copy(self.some_circular_ref)

        # Then, let's clone the object itself, using the prepared clones of the
        # nested objects.
        new = self.__class__(
            self.some_int, some_list_of_objects, some_circular_ref
        )
        new.__dict__.update(self.__dict__)

        return new

    def __deepcopy__(self, memo=None):
        """
        Create a deep copy. This method will be called whenever someone calls
        `copy.deepcopy` with this object and the returned value is returned as
        the new deep copy.

        What is the use of the argument `memo`? Memo is the dictionary that is
        used by the `deepcopy` library to prevent infinite recursive copies in
        instances of circular references. Pass it to all the `deepcopy` calls
        you make in the `__deepcopy__` implementation to prevent infinite
        recursions.
        """
        if memo is None:
            memo = {}

        # First, let's create copies of the nested objects.
        some_list_of_objects = copy.deepcopy(self.some_list_of_objects, memo)
        some_circular_ref = copy.deepcopy(self.some_circular_ref, memo)

        # Then, let's clone the object itself, using the prepared clones of the
        # nested objects.
        new = self.__class__(
            self.some_int, some_list_of_objects, some_circular_ref
        )
        new.__dict__ = copy.deepcopy(self.__dict__, memo)

        return new


if __name__ == "__main__":

    list_of_objects = [1, {1, 2, 3}, [1, 2, 3]]
    circular_ref = SelfReferencingEntity()
    component = SomeComponent(23, list_of_objects, circular_ref)
    circular_ref.set_parent(component)

    shallow_copied_component = copy.copy(component)

    # Let's change the list in shallow_copied_component and see
    # if it changes in component.
    shallow_copied_component.some_list_of_objects.append("another object")
    if component.some_list_of_objects[-1] == "another object":
        print(
            "Adding elements to `shallow_copied_component`'s "
            "some_list_of_objects adds it to `component`'s "
            "some_list_of_objects."
        )
    else:
        print(
            "Adding elements to `shallow_copied_component`'s "
            "some_list_of_objects doesn't add it to `component`'s "
            "some_list_of_objects."
        )

    # Let's change the set in the list of objects.
    component.some_list_of_objects[1].add(4)
    if 4 in shallow_copied_component.some_list_of_objects[1]:
        print(
            "Changing objects in the `component`'s some_list_of_objects "
            "changes that object in `shallow_copied_component`'s "
            "some_list_of_objects."
        )
    else:
        print(
            "Changing objects in the `component`'s some_list_of_objects "
            "doesn't change that object in `shallow_copied_component`'s "
            "some_list_of_objects."
        )

    deep_copied_component = copy.deepcopy(component)

    # Let's change the list in deep_copied_component and see if it changes in
    # component.
    deep_copied_component.some_list_of_objects.append("one more object")
    if component.some_list_of_objects[-1] == "one more object":
        print(
            "Adding elements to `deep_copied_component`'s "
            "some_list_of_objects adds it to `component`'s "
            "some_list_of_objects."
        )
    else:
        print(
            "Adding elements to `deep_copied_component`'s "
            "some_list_of_objects doesn't add it to `component`'s "
            "some_list_of_objects."
        )

    # Let's change the set in the list of objects.
    component.some_list_of_objects[1].add(10)
    if 10 in deep_copied_component.some_list_of_objects[1]:
        print(
            "Changing objects in the `component`'s some_list_of_objects "
            "changes that object in `deep_copied_component`'s "
            "some_list_of_objects."
        )
    else:
        print(
            "Changing objects in the `component`'s some_list_of_objects "
            "doesn't change that object in `deep_copied_component`'s "
            "some_list_of_objects."
        )

    print(
        f"id(deep_copied_component.some_circular_ref.parent): "
        f"{id(deep_copied_component.some_circular_ref.parent)}"
    )

    if deep_copied_component.some_circular_ref.parent:
        print(
            f"id(deep_copied_component.some_circular_ref.parent.some_circular_ref.parent): "  # noqa
            f"{id(deep_copied_component.some_circular_ref
                  .parent.some_circular_ref
                  .parent
                  )
               }"
        )
    print(
        "^^ This shows that deepcopied objects contain same reference, they "
        "are not cloned repeatedly."
    )
