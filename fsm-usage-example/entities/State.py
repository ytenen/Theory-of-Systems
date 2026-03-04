class State:
    def __init__(self, name, is_terminal=False):
        self.name = name
        self.is_terminal = is_terminal
        self.transitions = {}

    def add_transition(self, action, state):
        self.transitions[action] = state

    def make_terminal(self):
        self.is_terminal = True