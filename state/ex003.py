# Define an abstract base class called TicketState
class TicketState:
    def assign(self, t):
        pass

    def resolve(self, t):
        pass

    def close(self, t):
        pass


# Implement concrete state classes for each of the ticket states
class NewState(TicketState):
    def assign(self, ticket):
        print("Ticket is now assigned.")
        return AssignedState()


class AssignedState(TicketState):
    def resolve(self, ticket):
        print("Ticket is now resolved.")
        return ResolvedState()


class ResolvedState(TicketState):
    def close(self, ticket):
        print("Ticket is now closed.")
        return ClosedState()


class ClosedState(TicketState):
    def assign(self, ticket: 'Ticket'):
        pass

    def resolve(self, ticket: 'Ticket'):
        pass

    def close(self, ticket: 'Ticket'):
        pass


# Implement a Ticket class to manage state transitions
class Ticket:
    def __init__(self) -> None:
        self.state: TicketState = NewState()

    def assign(self):
        self.state.assign(self)

    def resolve(self):
        self.state.resolve(self)

    def close(self):
        self.state.close(self)


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


if __name__ == "__main__":
    main()
