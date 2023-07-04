from Transition import Transition

class State:
    """ This is a class to define the properties of an individual State in a automata"""

    def __init__(self, name, FinalState):
        """ Initailize the State with Arguement:
            ID           -  Unique Identifier for the State (String or Integer)
            StateType    -  Defines the if the State is Terminal State or vice versa (Boolean)
            Transition   -  COntains all transitions from the State (Dictionary)
            """

        self.ID = name
        self.StateType = FinalState
        self.Transition = dict()

    def addTransition(self, InString, OutString, OutState):
        """ Appends a Transition into the class variable 'Transition'
            Arguement of the method:
            Instring    -  Transistion string input 
            Outstring   -  Output string of the transition
            Outstate    -  Next state of the transition
            
            Return:
            None
            """

        if InString in self.Transition.keys():
            #print("Transition with same Instring available")
            self.Transition[InString].append(Transition(self, InString,OutString= OutString, OutState = OutState))
        else:
            #print("New input string Transition")
            self.Transition[InString] = []
            self.Transition[InString].append(Transition(self, InString, OutString = OutString, OutState = OutState))

    def CheckTransition(self, InputAlphabet):

        if InputAlphabet not in self.Transition.keys():
            #print("No Transition as such")
            return [-1]
        elif InputAlphabet in self.Transition.keys():

            Transition_Output_List = []
            for Transit in self.Transition[InputAlphabet]:
                Transition_Output_List.append(Transit.Output())
            
            if '' in self.Transition.keys() and '' != InputAlphabet:
                for epilsonTransit in self.Transition['']:
                    Transition_Output_List.append(epilsonTransit.Output())

            return Transition_Output_List
