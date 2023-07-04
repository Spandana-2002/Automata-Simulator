from State import State

class Automata:
    """ Basic class to define the automata's structure and its transitions. Further this automata model and be deployed in acceptor or automaton for applications."""

    def __init__(self, StateCount, Alphabet, OutAlphabets, InitialState, FinalStaeCount):
        
        self.StatesCount = StateCount
        self.Alphabet = Alphabet
        self.OutAlphabets = OutAlphabets
        self.InitialState = InitialState
        self.FinalStaeCount = FinalStaeCount

        self.States = dict()
    
    # Methods for building the automata structure

    def AddState(self, ID, Type):

        if self.StatesCount >= len(self.States):
            self.States[ID] = State(ID, Type)
        else:
            print("Exceeding the number of states!!!")

    def AddStateTransition(self, InState, InString, OutString, OutState):

        if InState in self.States.keys() and OutState in self.States.keys():
            In = self.States[InState]
            In.addTransition(InString, OutString, OutState)
            return
        else:
            return -1

    # Create a new Transition object for a state

    def AddsetTransition(self, InState, set ,OutState):
        
        for a in set:
            PCode = self.AddStateTransition(InState, a, a, OutState)
            if PCode == -1:
                print(f'No state : {InState} present for the Transition |OR| No state : {OutState} present for the Transition')
                break
        
    def AddsetEpilsonTransition(self, InState, set ,OutState):

        for a in set:
            PCode = self.AddStateTransition(InState, a, '', OutState)
            if PCode == -1:
                print(f'No state : {InState} present for the Transition |OR| No state : {OutState} present for the Transition')
                break


    def AddEpilsonTransition(self, InState, OutState):

        PCode = self.AddStateTransition(InState, '', '', OutState)
        if PCode == -1:
            print(f'No state : {InState} present for the Transition |OR| No state : {OutState} present for the Transition')

    def AddEpilsonStringTransition(self, InState, OutString, OutState):

        PCode = self.AddStateTransition(InState, '', OutString, OutState)
        if PCode == -1:
            print(f'No state : {InState} present for the Transition |OR| No state : {OutState} present for the Transition')
        
