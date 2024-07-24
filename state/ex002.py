from abc import ABC, abstractmethod


# Step 1: Define the abstract base class TicketState
class TicketState(ABC):
    _instance = None
    ticket: 'Ticket'

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)

        return cls._instance

    @abstractmethod
    def assign(self, ticket: 'Ticket') -> 'TicketState':
        pass

    @abstractmethod
    def resolve(self, ticket: 'Ticket') -> 'TicketState':
        pass

    @abstractmethod
    def close(self, ticket: 'Ticket') -> 'TicketState':
        pass

    def __str__(self):
        cls = type(self)
        return f'{{  {cls.__name__}  }}'


# Step 2: Implement the concrete state classes
class NewState(TicketState):
    def assign(self, ticket: 'Ticket'):
        ticket.state = AssignedState()

    def resolve(self, ticket: 'Ticket'):
        print('Não dá: ticket precisa ser atribuído')

    def close(self, ticket: 'Ticket'):
        ticket.state = ClosedState()


class AssignedState(TicketState):
    def assign(self, ticket: 'Ticket'):
        print('Já está atribuído!')

    def resolve(self, ticket: 'Ticket'):
        ticket.state = ResolvedState()

    def close(self, ticket: 'Ticket'):
        ticket.state = ClosedState()


class ResolvedState(TicketState):
    def assign(self, ticket: 'Ticket'):
        print("Não dá: Ticket já resolvido")

    def resolve(self, ticket: 'Ticket'):
        print("O ticket já está resolvido")

    def close(self, ticket: 'Ticket'):
        ticket.state = ClosedState()


class ClosedState(TicketState):
    def assign(self, ticket: 'Ticket'):
        print("Não dá: Ticket já fechado")

    def resolve(self, ticket: 'Ticket'):
        print("Não dá: Ticket já fechado")

    def close(self, ticket: 'Ticket'):
        print("Não dá: Ticket já fechado")


# Step 3: Implement the Ticket class
class Ticket:

    def __init__(self) -> None:
        self.state: TicketState = NewState()
        # print(self)

    def assign(self):
        self.state.assign(self)
        # print(self)

    def resolve(self):
        self.state.resolve(self)
        # print(self)

    def close(self):
        self.state.close(self)
        # print(self)

    def __str__(self):
        cls = type(self)
        return f'{cls.__name__}{self.state}'


# Step 4: Test the behavior of the ticket and its state transitions
def main():
    ticket = Ticket()

    # Test the initial state and transitions
    ticket.assign()
    ticket.resolve()
    ticket.close()

    # Test invalid transitions
    ticket.assign()
    ticket.resolve()
    print(ticket)


if __name__ == "__main__":
    main()
