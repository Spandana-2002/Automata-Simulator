import os, sys
dir = os.getcwd()
sys.path.insert(1, dir + '/src')


from Automata import Automata
from Machine import Machine

if __name__ == "__main__":

    AutoEx_1 = Automata(StateCount=3, Alphabet=set('01'), OutAlphabets= None, InitialState='a', FinalStaeCount=1)

    # Adding States
    AutoEx_1.AddState(ID='a', Type= False)
    AutoEx_1.AddState(ID='b', Type= True)
    AutoEx_1.AddState(ID='c', Type= True)

    # Adding Transitions
    AutoEx_1.AddStateTransition(InState='a', InString = '1', OutString = '0', OutState= 'b')
    AutoEx_1.AddStateTransition(InState='b', InString = '0', OutString = '1', OutState= 'c')
    AutoEx_1.AddStateTransition(InState='a', InString = '1', OutString = '1', OutState= 'c')
    AutoEx_1.AddStateTransition(InState='a', InString = '0', OutString = '1', OutState= 'c')

    O = Machine(Automata=AutoEx_1, InputString= sys.argv[1])
    O.Machine_Automata_Output()
    