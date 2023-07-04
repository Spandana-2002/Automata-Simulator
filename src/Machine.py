class Machine:

    def __init__(self, Automata, InputString):
        self.Automata = Automata
        self.IntialState = Automata.InitialState
        self.InputString = InputString

    def Run(self,CurrentState, I = None, String = None):

        if I is None:
            Terminal_Transition_outputs = self.Automata.States[CurrentState].CheckTransition(InputAlphabet = '')
            if len(Terminal_Transition_outputs) > 0 and Terminal_Transition_outputs[0] != -1:
                Terminal_Transition_outputs = self.Automata.States[CurrentState].CheckTransition(InputAlphabet = '')

                Output = []
                for Transit in Terminal_Transition_outputs:
                    if Transit == -1:
                        continue
                    Sub_Output = self.Run(Transit[1])
                    #print(Sub_Output)
                    for S in Sub_Output:

                        S.insert(0,Transit[0])
                        Output.append(S)
                return Output

            
            elif self.Automata.States[CurrentState].StateType == True:
                return [[True]]
            else:
                return [[False]]
            
        else:
            Output = []
            Transition_Outputs = self.Automata.States[CurrentState].CheckTransition(InputAlphabet = I)

            if Transition_Outputs[0] == -1:
                return [[False]]

            else:

                for Transit_Output in Transition_Outputs:
                    
                    if Transit_Output == -1:
                        continue

                    elif len(String) == 0:
                        Sub_Transition_Output = self.Run(Transit_Output[1], I = None, String= None)
                    else:
                        Sub_Transition_Output = self.Run(Transit_Output[1], I = String[0], String= String[1:])
                    
                    for S in Sub_Transition_Output:
                        S.insert(0,Transit_Output[0])
                        Output.append(S) 
                return Output
    
    def Machine_Automata_Output(self):

        print("Initiating machine")
        OutputList = self.Run(self.IntialState, I= self.InputString[0], String=self.InputString[1:])
        print("Completing the Generation...")
        for Output in OutputList:
            if True in Output:
                Output.remove(True)
                Generated_String = "".join(Output)
                print("Input String: " + self.InputString)
                print("Generated Output String -->" + Generated_String)
                break

