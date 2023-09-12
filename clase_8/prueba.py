class TuringMachine:
    def __init__(self, tape):
        self.tape = list(tape)
        self.current_state = 'q0'
        self.head_position = 0
        self.zero_count = 0

    def move_right(self):
        self.head_position += 1
        if self.head_position == len(self.tape):
            self.tape.append('b')

    def move_left(self):
        if self.head_position > 0:
            self.head_position -= 1

    def run(self):
        while True:
            symbol = self.tape[self.head_position]
            if self.current_state == 'q0':
                if symbol == '0':
                    self.tape[self.head_position] = 'b'
                    self.move_right()
                elif symbol == '1':
                    self.move_right()
                elif symbol == 'b':
                    self.current_state = 'q1'
            elif self.current_state == 'q1':
                if symbol == '0':
                    self.move_right()
                    self.zero_count += 1
                elif symbol == '1':
                    self.move_right()
                elif symbol == 'b':
                    break

        return self.zero_count % 2 == 0

# Ejemplo de uso:
input_string = "00010"
tm = TuringMachine(input_string)

if tm.run():
    print("El número de ceros es par.")
else:
    print("El número de ceros no es par.")
