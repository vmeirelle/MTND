class Language:
    def __init__(self, states=None, symbols=None, stack_symbols=None, 
                 start_symbol=None, end_symbol=None, num_transitions=0, initial_state=None, final_states=None, test_words=None):
        self.states = states or []
        self.symbols = symbols or []
        self.stack_symbols = stack_symbols or []
        self.transitions = {}
        self.test_words = test_words or []
        self.final_states = final_states or []
        self.start_symbol = start_symbol or ''
        self.end_symbol = end_symbol or ''
        self.initial_state = initial_state or ''
        self.num_transitions = num_transitions

    def read_transitions(self):
        for _ in range(self.num_transitions):
            trans = input().split()
            self.create_transition(trans)

    def create_transition(self, trans):
        key = trans[0] + trans[1]
        if key in self.transitions:
            self.transitions[key].append((trans[2], trans[3], trans[4]))
        else:
            self.transitions[key] = [(trans[2], trans[3], trans[4])]

    def write(self, tape, symbol, register):
        new_tape = tape.copy()
        new_tape[register] = symbol
        return new_tape

    def move(self, tape, register, direction):
        if direction == 'I':
            return register
        elif direction == 'E':
            return max(0, register - 1)
        elif direction == 'D':
            return min(len(tape), register + 1)

    def validate_transition(self, current_state, tape, register, transition_stack):
        try:
            character = tape[register]
        except:
            return True
        key = current_state + character
        if key in self.transitions:
            for transition in self.transitions[key]:
                new_register = self.move(tape, register, transition[2])
                transition_stack.append([transition[0], self.write(tape, transition[1], register), new_register])
            return False
        else:
            return True

    def is_accepted(self, state, stopped):
        return stopped and state in self.final_states

    def process_word(self, word, initial_state):
        tape = [self.start_symbol] + list(word) + [self.end_symbol]
        transition_stack = [[initial_state, tape, 1]]
        accepted = False
        while transition_stack:
            new_stack = []
            for trans in transition_stack:
                stopped = self.validate_transition(trans[0], trans[1], trans[2], new_stack)
                if self.is_accepted(trans[0], stopped):
                    accepted = True
                    break
            if accepted:
                break
            transition_stack = new_stack
        return 'S' if accepted else 'N'


language = Language()
language.states = input()
language.symbols = input()
language.stack_symbols = input()
language.start_symbol = input()
language.end_symbol = input()
language.num_transitions = int(input())
language.read_transitions()
language.initial_state = input()
language.final_states = input().split()
language.test_words = input().split()

for word in language.test_words:
    print(language.process_word(word, language.initial_state))
