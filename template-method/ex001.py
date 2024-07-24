"""
Applicability
 Use the Template Method pattern when you want to let clients extend only
 particular steps of an algorithm, but not the whole algorithm or its
 structure.

 The Template Method lets you turn a monolithic algorithm into a series of
 individual steps which can be easily extended by subclasses while keeping
 intact the structure defined in a superclass.

 Use the pattern when you have several classes that contain almost identical
 algorithms with some minor differences. As a result, you might need to
 modify all classes when the algorithm changes.

 When you turn such an algorithm into a template method, you can also
 pull up the steps with similar implementations into a superclass,
 eliminating code duplication. Code that varies between subclasses can
 remain in subclasses.

 How to Implement
Analyze the target algorithm to see whether you can break it into steps.
Consider which steps are common to all subclasses and which ones will
always be unique.

Create the abstract base class and declare the template method and a set
of abstract methods representing the algorithm's steps. Outline the
algorithm's structure in the template method by executing corresponding steps.
Consider making the template method final to prevent subclasses from
overriding it.

It's okay if all the steps end up being abstract. However, some steps
might benefit from having a default implementation. Subclasses don't have
to implement those methods.

Think of adding hooks between the crucial steps of the algorithm.

For each variation of the algorithm, create a new concrete subclass.
It must implement all of the abstract steps, but may also override
some of the optional ones.

Pros and Cons
Pros:
 You can let clients override only certain parts of a large algorithm,
 making them less affected by changes that happen to other parts of the
 algorithm. You can pull the duplicate code into a superclass.

Cons:
 Some clients may be limited by the provided skeleton of an algorithm.
 You might violate the Liskov Substitution Principle by suppressing a
 default step implementation via a subclass.
 Template methods tend to be harder to maintain the more steps they have.
 Relations with Other Patterns
Factory Method is a specialization of Template Method. At the same time,
a Factory Method may serve as a step in a large Template Method.

Template Method is based on inheritance: it lets you alter parts of an
algorithm by extending those parts in subclasses. Strategy is based on
composition: you can alter parts of the object's behavior by supplying
it with different strategies that correspond to that behavior.
Template Method works at the class level, so it's static.
Strategy works on the object level, letting you switch behaviors at runtime.

"""


from abc import ABC, abstractmethod


class AbstractClass(ABC):
    """
    The Abstract Class defines a template method that contains a skeleton of
    some algorithm, composed of calls to (usually) abstract primitive
    operations.

    Concrete subclasses should implement these operations, but leave the
    template method itself intact.
    """

    def template_method(self) -> None:
        """
        The template method defines the skeleton of an algorithm.
        """

        self.base_operation1()
        self.required_operations1()
        self.base_operation2()
        self.hook1()
        self.required_operations2()
        self.base_operation3()
        self.hook2()

    # These operations already have implementations.

    def base_operation1(self) -> None:
        print("AbstractClass says: I am doing the bulk of the work")

    def base_operation2(self) -> None:
        print("AbstractClass says: But I let subclasses "
              "override some operations")

    def base_operation3(self) -> None:
        print("AbstractClass says: But I am doing the bulk of the work anyway")

    # These operations have to be implemented in subclasses.

    @abstractmethod
    def required_operations1(self) -> None:
        pass

    @abstractmethod
    def required_operations2(self) -> None:
        pass

    # These are "hooks." Subclasses may override them, but it's not mandatory
    # since the hooks already have default (but empty) implementation. Hooks
    # provide additional extension points in some crucial places of the
    # algorithm.

    def hook1(self) -> None:
        pass

    def hook2(self) -> None:
        pass


class ConcreteClass1(AbstractClass):
    """
    Concrete classes have to implement all abstract operations of the base
    class. They can also override some operations with a default
    implementation.
    """

    def required_operations1(self) -> None:
        print("ConcreteClass1 says: Implemented Operation1")

    def required_operations2(self) -> None:
        print("ConcreteClass1 says: Implemented Operation2")


class ConcreteClass2(AbstractClass):
    """
    Usually, concrete classes override only a fraction of base class'
    operations.
    """

    def required_operations1(self) -> None:
        print("ConcreteClass2 says: Implemented Operation1")

    def required_operations2(self) -> None:
        print("ConcreteClass2 says: Implemented Operation2")

    def hook1(self) -> None:
        print("ConcreteClass2 says: Overridden Hook1")


def client_code(abstract_class: AbstractClass) -> None:
    """
    The client code calls the template method to execute the algorithm. Client
    code does not have to know the concrete class of an object it works with,
    as long as it works with objects through the interface of their base class.
    """

    # ...
    abstract_class.template_method()
    # ...


if __name__ == "__main__":
    print("Same client code can work with different subclasses:")
    client_code(ConcreteClass1())
    print("")

    print("Same client code can work with different subclasses:")
    client_code(ConcreteClass2())
