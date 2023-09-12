import re

class Ejercicio_2a():
    
    def __init__(self, string):
        self.string = string
        self.states = ["q0", "q1", "q2", "q3", "q4", "q5", "q6", "q7", "q8"]
        self.transitions = ["x", "y", "e"]
        self.transitions_blank = ["x", "y", "e", ""]
        self.initial_state = "q0"
        self.acceptance_state = ["q2", "q8"]
        self.lambdas = {
            ("q0", "x"): ("q1", "x", "R"),
            ("q1", "e"): ("q2", "e", "R"),
            ("q1", "e"): ("q8", "e", "R"),
            ("q2", "e"): ("q3", "e", "R"),
            ("q2", "e"): ("q4", "e", "R"),
            ("q3", "x"): ("q5", "x", "R"),
            ("q3", "y"): ("q6", "y", "R"),
            ("q4", "e"): ("q5", "e", "R"),
            ("q4", "e"): ("q6", "e", "R"),
            ("q5", "e"): ("q7", "e", "R"),
            ("q6", "e"): ("q7", "e", "R"),
            ("q7", "e"): ("q2", "e", "R"),
            ("q7", "e"): ("q8", "e", "R")
        }

        self.lambdas_states =[
            ["q1", "kboom"],
            ["q2", "q3"],
            ["q2", "q3"],
            ["q2", "q3"],
        ]

    def obtener_fila(self, estado):
        rows = {"q0": 0, "q1": 1, "q2": 2, "q3": 3}
        return rows.get(estado)
    
    def obtener_col(self, char):
        columns = {"x": 0, "y": 1}
        return columns.get(char)
    
    def transactions(self):

        self.actual_state = self.initial_state
        for char in self.string:
            if char in self.transitions_blank:
                if self.actual_state != "kboom":
                    self.actual_state = self.lambdas_states[self.obtener_fila(self.actual_state)][self.obtener_col(char)]
                else:
                    break
            else:
                print(f"Invalid character: {char}")
                return False
        if self.actual_state in self.acceptance_state:
            print("Accepted")
            return True
        else:
            print("Rejected")
            return False


class Ejercicio_2b():

    def __init__(self, string):
        self.string = string
        self.states = ["q0", "q1", "q2", "q3"]
        self.transitions = ["a", "c"]
        self.transitions_blank = ["a", "c", ""]
        self.initial_state = "q0"
        self.acceptance_state = ["q2", "q3"]
        self.lambdas = {
            ("q0", "a"): ("q4", "a", "R"),
            ("q0", "b"): ("q1", "b", "R"),
            ("q1", "a"): ("q4", "a", "R"),
            ("q1", "b"): ("q2", "b", "R"),
            ("q2", "a"): ("q3", "a", "R"),
            ("q2", "b"): ("q2", "b", "R"),
            ("q3", "a"): ("q4", "a", "R"),
            ("q3", "b"): ("q2", "b", "R")
        }
        self.lambdas_states =[
            ["q1", "q2"],
            ["kboom", "q3"],
            ["q1", "q2"],
            ["q1", "q2"],
        ]

    def obtener_fil(self, estado):
        rows = {"q0": 0, "q1": 1, "q2": 2, "q3": 3}
        return rows.get(estado)

    def obtener_col(self, char):
        columns = {"a": 0, "c": 1}
        return columns.get(char)

    def transactions(self):

        self.actual_state = self.initial_state
        for char in self.string:
            if char in self.transitions_blank:
                if self.actual_state != "kboom":
                    self.actual_state = self.lambdas_states[self.obtener_fil(self.actual_state)][self.obtener_col(char)]
                else:
                    break
            else:
                print(f"Invalid character: {char}")
                return False
        if self.actual_state in self.acceptance_state:
            print("Accepted")
            return True 
        else:
            print("Rejected")
            return False

class Ejercicio_2c():

    def __init__(self, string):
        self.string = string
        self.states = ["q0", "q1", "q2", "q3", "q4"]
        self.transitions = ["a", "b"]
        self.transitions_blank = ["a", "b", ""]
        self.initial_state = "q0"
        self.acceptance_state = ["q3", "q4"]
        self.lambdas = {
            ("q0", "a"): ("q4", "a", "R"),
            ("q0", "b"): ("q1", "b", "R"),
            ("q1", "a"): ("q4", "a", "R"),
            ("q1", "b"): ("q2", "b", "R"),
            ("q2", "a"): ("q3", "a", "R"),
            ("q2", "b"): ("q2", "b", "R"),
            ("q3", "a"): ("q4", "a", "R"),
            ("q3", "b"): ("q2", "b", "R")
        }
        self.lambdas_states =[
            ["q4", "q1"],
            ["q4", "q2"],
            ["q3", "q2"],
            ["q4", "q2"],
            ["q4", "q2"],
        ]

    def obtener_fil(self, estado):
        rows = {"q0": 0, "q1": 1, "q2": 2, "q3": 3, "q4": 4}
        return rows.get(estado)

    def obtener_col(self, char):
        columns = {"a": 0, "b": 1}
        return columns.get(char)

    def transactions(self):

        self.actual_state = self.initial_state
        for char in self.string:
            if char in self.transitions_blank:
                if self.actual_state != "kboom":
                    self.actual_state = self.lambdas_states[self.obtener_fil(self.actual_state)][self.obtener_col(char)]
                else:
                    break
            else:
                print(f"Invalid character: {char}")
                return False
        if self.actual_state in self.acceptance_state:
            print("Accepted")
            return True
        else:
            print("Rejected")
            return False




if __name__ == "__main__":
    ejercicio_2c = Ejercicio_2c("bbaaa")
    ejercicio_2c.transactions()
    # ejercicio_2a = Ejercicio_2a("yx")
    # ejercicio_2a.transactions()
    # ejercicio_2b = Ejercicio_2b("aa")
    # ejercicio_2b.transactions()
    pass
