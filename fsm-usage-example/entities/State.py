class State:
    def __init__(self, name, is_terminal=False):
        self.name = name
        self.is_terminal = is_terminal
        self.transitions = {}

    def add_transition(self, event, state, action=None):
        self.transitions[event] = (state, action)

    def make_terminal(self):
        self.is_terminal = True