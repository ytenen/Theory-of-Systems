import inspect


class Application:
    def __init__(self, start_state):
        self.current_state = start_state
        self.failure_reason = None
        self.current_event = None

    def perform_action(self, event):
        self.current_event = event
        if event in self.current_state.transitions:
            next_state, action = self.current_state.transitions[event]
            if action:
                action(self)
            self.current_state = next_state
            print(f"Переход в состояние: {self.current_state.name}")
        else:
            print(f"Действие '{event}' невозможно в состоянии '{self.current_state.name}'.")