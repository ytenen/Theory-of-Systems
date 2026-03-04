class Application:
    def __init__(self, start_state):
        self.current_state = start_state

    def perform_action(self, event):
        if event in self.current_state.transitions:
            self.current_state = self.current_state.transitions[event]
            print(f"Переход в состояние: {self.current_state.name}")
        else:
            print(f"Действие '{event}' невозможно в состоянии '{self.current_state.name}'.")

    