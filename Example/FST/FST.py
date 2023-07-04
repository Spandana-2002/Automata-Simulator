import os, sys
dir = os.getcwd()
sys.path.insert(1, dir + '/src')

# Refer the Morphological Generator.pdf for understanding the design of the automata
from Automata import Automata
from Machine import Machine

if __name__ == "__main__":

    A = Automata(StateCount=12, Alphabet=set('abcdefghijklmnopqrstuvwxyz'), OutAlphabets= None, InitialState='q0', FinalStaeCount=1)

    #Adding States
    A.AddState(ID='q0',Type=False)
    A.AddState(ID='q1',Type=False)
    A.AddState(ID='q_ing',Type=False)
    A.AddState(ID='q_drop_E',Type=False)
    A.AddState(ID='q_EE',Type=False)
    A.AddState(ID='q_IE',Type=False)
    A.AddState(ID='q_VOWS',Type=False)
    A.AddState(ID='q_VOWS2',Type=False)
    A.AddState(ID='q_CONS',Type=False)
    A.AddState(ID='q_CONS+E',Type=False)
    A.AddState(ID='q_CONS_VOWS-E',Type=False)
    A.AddState(ID='q_EOW',Type=True)

    A2Z=set('abcdefghijklmnopqrstuvwxyz')
    VOWS=set('aieou')
    CONS=A2Z-VOWS
    U=set('u')
    E=set('e')
    I=set('i')
    PT=set('pt')
    NR=set('nr')

    #Adding Transitions
    #AddsetTransition(self, InState, set ,OutState)
    A.AddsetTransition('q0', VOWS , 'q_VOWS')
    A.AddsetTransition('q_VOWS', VOWS, 'q_VOWS2')
    A.AddsetTransition('q_VOWS2',CONS,'q_ing')
    #AddEpilsonStringTransition(self, InState, OutString, OutState)
    A.AddEpilsonStringTransition('q_ing','ing','q_EOW')

    ##check
    #AddsetTransition(self, InState, set ,OutState)
    A.AddsetTransition('q0', A2Z ,'q1')
    A.AddsetTransition('q1', A2Z ,'q1')
    A.AddsetTransition('q1', CONS.union(U) ,'q_drop_E')
    #AddsetEpilsonTransition(self, InState, set ,OutState)
    A.AddsetEpilsonTransition('q_drop_E',E,'q_ing')
    A.AddsetTransition('q1', E ,'q_EE')
    A.AddsetTransition('q_EE', E ,'q_ing') ##########################
    A.AddsetEpilsonTransition('q1',I,'q_IE')
    #AddStateTransition(self, InState, InString, OutString, OutState)
    A.AddStateTransition('q_IE', 'e','y','q_ing')
    A.AddsetTransition('q1',CONS,'q_CONS')
    A.AddsetTransition('q1',VOWS,'q_VOWS')

    #AddsetTransition(self, InState, set ,OutState)
    A.AddsetTransition('q0', CONS ,'q_CONS')
    A.AddsetTransition('q_CONS', E ,'q_CONS+E')
    A.AddsetTransition('q_CONS+E',A2Z-PT-VOWS,'q_ing')
    #AddStateTransition(self, InState, InString, OutString, OutState
    A.AddStateTransition('q_cons+E','p','pp','q_ing')
    A.AddStateTransition('q_cons+E','t','tt','q_ing')
    A.AddsetTransition('q_CONS', VOWS-E ,'q_CONS_VOWS-E')
    A.AddsetTransition('q_CONS_VOWS-E',A2Z-NR-PT-VOWS,'q_ing')
    A.AddStateTransition('q_CONS_VOWS-E','p','pp','q_ing')
    A.AddStateTransition('q_CONS_VOWS-E','n','nn','q_ing')
    A.AddStateTransition('q_CONS_VOWS-E','r','rr','q_ing')
    A.AddStateTransition('q_CONS_VOWS-E','t','tt','q_ing')

    O = Machine(Automata=A, InputString= sys.argv[1])
    O.Machine_Automata_Output()
    