class Application:
    def __init__(self, start_state):
        self.current_state = start_state

    def perform_action(self, event, **kwargs):
        if event in self.current_state.transitions:
            next_state, action = self.current_state.transitions[event]
            self.current_state = next_state
            if action:
                action(**kwargs)
            print(f"Переход в состояние: {self.current_state.name}")
        else:
            print(f"Действие '{event}' невозможно в состоянии '{self.current_state.name}'.")

    