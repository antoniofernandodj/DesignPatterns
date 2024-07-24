from __future__ import annotations
from abc import ABC, abstractmethod
from random import randrange
from typing import Any, List, Optional


"""
Applicability
 Use the Observer pattern when changes to the state of one object may require
 changing other objects, and the actual set of objects is unknown beforehand
 or changes dynamically.

 You can often experience this problem when working with classes of the
 graphical user interface. For example, you created custom button classes, and
 you want to let the clients hook some custom code to your buttons so that
 it fires whenever a user presses a button.

The Observer pattern lets any object that implements the subscriber interface
subscribe for event notifications in publisher objects. You can add the
subscription mechanism to your buttons, letting the clients hook up their
custom code via custom subscriber classes.

 Use the pattern when some objects in your app must observe others, but only
 for a limited time or in specific cases.

 The subscription list is dynamic, so subscribers can join or leave the list
 whenever they need to.

 How to Implement
Look over your business logic and try to break it down into two parts: the
core functionality, independent from other code, will act as the publisher;
the rest will turn into a set of subscriber classes.

Declare the subscriber interface. At a bare minimum, it should declare a
single update method.

Declare the publisher interface and describe a pair of methods for adding a
subscriber object to and removing it from the list. Remember that publishers
must work with subscribers only via the subscriber interface.

Decide where to put the actual subscription list and the implementation of
subscription methods. Usually, this code looks the same for all types of
publishers, so the obvious place to put it is in an abstract class derived
directly from the publisher interface. Concrete publishers extend that class,
inheriting the subscription behavior.

However, if you're applying the pattern to an existing class hierarchy,
consider an approach based on composition: put the subscription logic into a
separate object, and make all real publishers use it.

Create concrete publisher classes. Each time something important happens
inside a publisher, it must notify all its subscribers.

Implement the update notification methods in concrete subscriber classes. Most
subscribers would need some context data about the event. It can be passed as
an argument of the notification method.

But there's another option. Upon receiving a notification, the subscriber can
fetch any data directly from the notification. In this case, the publisher
must pass itself via the update method. The less flexible option is to link a
publisher to the subscriber permanently via the constructor.

The client must create all necessary subscribers and register them with proper
publishers.


 Pros and Cons

 Pros:
 Open/Closed Principle. You can introduce new subscriber classes without
 having to change the publisher's code (and vice versa if there's a publisher
 interface).
 You can establish relations between objects at runtime.

Cons:
 Subscribers are notified in random order.



 Relations with Other Patterns
Chain of Responsibility, Command, Mediator and Observer address various ways
of connecting senders and receivers of requests:

Chain of Responsibility passes a request sequentially along a dynamic chain of
potential receivers until one of them handles it.
Command establishes unidirectional connections between senders and receivers.
Mediator eliminates direct connections between senders and receivers, forcing
them to communicate indirectly via a mediator object.
Observer lets receivers dynamically subscribe to and unsubscribe from
receiving requests.
The difference between Mediator and Observer is often elusive. In most cases,
you can implement either of these patterns; but sometimes you can apply both
simultaneously. Let's see how we can do that.

The primary goal of Mediator is to eliminate mutual dependencies among a set
of system components. Instead, these components become dependent on a single
mediator object. The goal of Observer is to establish dynamic one-way
connections between objects, where some objects act as subordinates of others.

There's a popular implementation of the Mediator pattern that relies on
Observer. The mediator object plays the role of publisher, and the components
act as subscribers which subscribe to and unsubscribe from the mediator's
events. When Mediator is implemented this way, it may look very similar to
Observer.

When you're confused, remember that you can implement the Mediator pattern in
other ways. For example, you can permanently link all the components to the
same mediator object. This implementation won't resemble Observer but will
still be an instance of the Mediator pattern.

Now imagine a program where all components have become publishers, allowing
dynamic connections between each other. There won't be a centralized mediator
object, only a distributed set of observers.

"""


class Subject(ABC):
    _state: Any
    """
    The Subject interface declares a set of methods for managing subscribers.
    """

    @abstractmethod
    def attach(self, observer: Observer) -> None:
        """
        Attach an observer to the subject.
        """
        pass

    @abstractmethod
    def detach(self, observer: Observer) -> None:
        """
        Detach an observer from the subject.
        """
        pass

    @abstractmethod
    def notify(self) -> None:
        """
        Notify all observers about an event.
        """
        pass


class ConcreteSubject(Subject):
    """
    The Subject owns some important state and notifies observers when the state
    changes.
    """

    _state: Optional[int] = None
    """
    For the sake of simplicity, the Subject's state, essential to all
    subscribers, is stored in this variable.
    """

    _observers: List[Observer] = []
    """
    List of subscribers. In real life, the list of subscribers can be stored
    more comprehensively (categorized by event type, etc.).
    """

    def attach(self, observer: Observer) -> None:
        print("Subject: Attached an observer.")
        self._observers.append(observer)

    def detach(self, observer: Observer) -> None:
        self._observers.remove(observer)

    """
    The subscription management methods.
    """

    def notify(self) -> None:
        """
        Trigger an update in each subscriber.
        """

        print("Subject: Notifying observers...")
        for observer in self._observers:
            observer.update(self)

    def some_business_logic(self) -> None:
        """
        Usually, the subscription logic is only a fraction of what a
        Subject can really do. Subjects commonly hold some important
        business logic, that triggers a notification method
        whenever something important is about to
        happen (or after it).
        """

        print("\nSubject: I'm doing something important.")
        self._state = randrange(0, 10)

        print(f"Subject: My state has just changed to: {self._state}")
        self.notify()


class Observer(ABC):
    """
    The Observer interface declares the update method, used by subjects.
    """

    @abstractmethod
    def update(self, subject: Subject) -> None:
        """
        Receive update from subject.
        """
        pass


"""
Concrete Observers react to the updates issued by the Subject they had been
attached to.
"""


class ConcreteObserverA(Observer):
    def update(self, subject: Subject) -> None:
        if subject._state < 3:
            print("ConcreteObserverA: Reacted to the event")


class ConcreteObserverB(Observer):
    def update(self, subject: Subject) -> None:
        if subject._state == 0 or subject._state >= 2:
            print("ConcreteObserverB: Reacted to the event")


if __name__ == "__main__":
    # The client code.

    subject = ConcreteSubject()

    observer_a = ConcreteObserverA()
    subject.attach(observer_a)

    observer_b = ConcreteObserverB()
    subject.attach(observer_b)

    subject.some_business_logic()
    subject.some_business_logic()

    subject.detach(observer_a)

    subject.some_business_logic()
