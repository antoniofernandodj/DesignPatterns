from abc import ABC, abstractmethod
from typing import NamedTuple, Annotated
import time


"""
Applicability
 Use the State pattern when you have an object that behaves differently
 depending on its current state, the number of states is enormous, and the
 state-specific code changes frequently.

 The pattern suggests that you extract all state-specific code into a set of
 distinct classes. As a result, you can add new states or change existing ones
 independently of each other, reducing the maintenance cost.

 Use the pattern when you have a class polluted with massive conditionals that
 alter how the class behaves according to the current values of the class's
 fields.

 The State pattern lets you extract branches of these conditionals into
 methods of corresponding state classes. While doing so, you can also clean
 temporary fields and helper methods involved in state-specific code out of
 your main class.

 Use State when you have a lot of duplicate code across similar states and
 transitions of a condition-based state machine.

 The State pattern lets you compose hierarchies of state classes and reduce
 duplication by extracting common code into abstract base classes.

 How to Implement
Decide what class will act as the context. It could be an existing class which
already has the state-dependent code; or a new class, if the state-specific
code is distributed across multiple classes.

Declare the state interface. Although it may mirror all the methods declared
in the context, aim only for those that may contain state-specific behavior.

For every actual state, create a class that derives from the state interface.
Then go over the methods of the context and extract all code related to that
state into your newly created class.

While moving the code to the state class, you might discover that it depends
on private members of the context. There are several workarounds:

Make these fields or methods public.
Turn the behavior you're extracting into a public method in the context and
call it from the state class. This way is ugly but quick, and you can always
fix it later.
Nest the state classes into the context class, but only if your programming
language supports nesting classes.
In the context class, add a reference field of the state interface type and a
public setter that allows overriding the value of that field.

Go over the method of the context again and replace empty state conditionals
with calls to corresponding methods of the state object.

To switch the state of the context, create an instance of one of the state
classes and pass it to the context. You can do this within the context itself,
or in various states, or in the client. Wherever this is done, the class
becomes dependent on the concrete state class that it instantiates.

 Pros and Cons

Pros:
 Single Responsibility Principle. Organize the code related to particular
 states into separate classes.
 Open/Closed Principle. Introduce new states without changing existing state
 classes or the context.
 Simplify the code of the context by eliminating bulky state machine
 conditionals.

Cons:
 Applying the pattern can be overkill if a state machine has only a few states
 or rarely changes.
 Relations with Other Patterns
Bridge, State, Strategy (and to some degree Adapter) have very similar
structures. Indeed, all of these patterns are based on composition, which is
delegating work to other objects. However, they all solve different problems.
A pattern isn't just a recipe for structuring your code in a specific way.
It can also communicate to other developers the problem the pattern solves.

State can be considered as an extension of Strategy. Both patterns are based
on composition: they change the behavior of the context by delegating some
work to helper objects. Strategy makes these objects completely independent
and unaware of each other. However, State doesn't restrict dependencies
between concrete states, letting them alter the state of the context at will.
"""


class Baseclass:
    def __str__(self):
        cls = type(self)
        return f'{cls.__name__}({vars(self)})'

    def __repr__(self):
        cls = type(self)
        return f'{cls.__name__}({vars(self)})'


class Color(NamedTuple):
    r: Annotated[int, "0 to 255"]
    g: Annotated[int, "0 to 255"]
    b: Annotated[int, "0 to 255"]

    def __add__(self, color: 'Color') -> 'Color':  # type: ignore
        return Color(self.r + color.r, self.g + color.g, self.b + color.b)


red = Color(r=255, g=0, b=0)
green = Color(r=0, g=255, b=0)
blue = Color(r=0, g=0, b=255)

yellow = red + green
cian = green + blue
magenta = blue + red


class TrafficLight(Baseclass):
    def __init__(self, state: 'TrafficLightState'):
        self.state = state

    def next(self):
        self.state.next(self)

    def set_state(self, state):
        self.state = state

    def get_color(self):
        return self.state.get_color()


class TrafficLightState(ABC, Baseclass):

    @abstractmethod
    def get_color(self) -> Color:
        raise NotImplementedError

    @abstractmethod
    def next(self, light: TrafficLight) -> None:
        raise NotImplementedError


class GreenState(TrafficLightState):
    _instance = None

    @classmethod
    def get_instance(cls):
        if cls._instance is not None:
            return cls._instance
        instance = cls.__new__(cls)
        cls._instance = instance
        return instance

    def get_color(self) -> Color:
        return green

    def next(self, light: 'TrafficLight') -> None:
        light.state = YellowState.get_instance()


class YellowState(TrafficLightState):
    _instance = None

    @classmethod
    def get_instance(cls):
        if cls._instance is not None:
            return cls._instance
        instance = cls.__new__(cls)
        cls._instance = instance
        return instance

    def get_color(self) -> Color:
        return yellow

    def next(self, light: 'TrafficLight') -> None:
        light.state = RedState.get_instance()


class RedState(TrafficLightState):

    _instance = None

    @classmethod
    def get_instance(cls):
        if cls._instance is not None:
            return cls._instance
        instance = cls.__new__(cls)
        cls._instance = instance
        return instance

    def get_color(self) -> Color:
        return red

    def next(self, light: 'TrafficLight') -> None:
        light.state = GreenState.get_instance()


traffic_light = TrafficLight(GreenState())
while True:
    traffic_light.next()
    print(traffic_light)
    time.sleep(2)
