class Transition:
    """The Basic Transition implementation of a state is defined"""

    def __init__(self, InState, InString, OutState, OutString = None):
        """ Defines the basic transition properties and intialized with Argument
            Instate    -   Current state ID
            Instring   -   Transition string input
            OutString  -   Transition output sting
            OutState   -   Next state's ID of the transition
            """

        self.InState = InState
        self.InString = InString
        self.OutString = OutString
        self.OutState = OutState

    def Output(self):
        """ Returns the output if any exists
            """
        return [self.OutString, self.OutState]