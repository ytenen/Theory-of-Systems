from transitions import create_fsm
from entities.Application import Application
from entities.enum.Event import Event


def print_header(title):
    print(f"\n{'=' * 60}")
    print(f"  {title}")
    print(f"{'=' * 60}")


def simulate_success_online():
    print_header("СЦЕНАРИЙ 1: Успешная заявка (онлайн-подписание)")
    app = Application(create_fsm())
    print(f"Начальное состояние: {app.current_state.name}\n")
    app.perform_action(Event.AUTHORIZED)
    app.perform_action(Event.ONLINE_DOCUMENTS_SIGNING)
    app.perform_action(Event.ONLINE_SIGNING_COMPLETED)
    app.perform_action(Event.MONEY_TRANSFER_IS_READY)
    app.perform_action(Event.MONEY_TRANSFER_COMPLETED)
    print(f"\nФинальное состояние: {app.current_state.name}")


def simulate_success_courier():
    print_header("СЦЕНАРИЙ 2: Успешная заявка (курьер)")
    app = Application(create_fsm())
    print(f"Начальное состояние: {app.current_state.name}\n")
    app.perform_action(Event.AUTHORIZED)
    app.perform_action(Event.COURIER_DOCUMENTS_SIGNING)
    app.perform_action(Event.COURIER_SIGNING_COMPLETED)
    app.perform_action(Event.MONEY_TRANSFER_IS_READY)
    app.perform_action(Event.MONEY_TRANSFER_COMPLETED)
    print(f"\nФинальное состояние: {app.current_state.name}")


def simulate_auth_failure():
    print_header("СЦЕНАРИЙ 3: Ошибка авторизации")
    app = Application(create_fsm())
    print(f"Начальное состояние: {app.current_state.name}\n")
    app.perform_action(Event.AUTHORIZATION_FAILED)
    app.perform_action(Event.NOTIFICATION_SENT)
    print(f"\nФинальное состояние: {app.current_state.name}")


def simulate_online_signing_failure():
    print_header("СЦЕНАРИЙ 4: Ошибка онлайн-подписания")
    app = Application(create_fsm())
    print(f"Начальное состояние: {app.current_state.name}\n")
    app.perform_action(Event.AUTHORIZED)
    app.perform_action(Event.ONLINE_DOCUMENTS_SIGNING)
    app.perform_action(Event.ONLINE_SIGNING_FAILED)
    app.perform_action(Event.NOTIFICATION_SENT)
    print(f"\nФинальное состояние: {app.current_state.name}")


def simulate_money_transfer_failure():
    print_header("СЦЕНАРИЙ 5: Ошибка перевода средств")
    app = Application(create_fsm())
    print(f"Начальное состояние: {app.current_state.name}\n")
    app.perform_action(Event.AUTHORIZED)
    app.perform_action(Event.ONLINE_DOCUMENTS_SIGNING)
    app.perform_action(Event.ONLINE_SIGNING_COMPLETED)
    app.perform_action(Event.MONEY_TRANSFER_IS_READY)
    app.perform_action(Event.MONEY_TRANSFER_FAILED)
    app.perform_action(Event.NOTIFICATION_SENT)
    print(f"\nФинальное состояние: {app.current_state.name}")


def simulate_cancel_at_new():
    print_header("СЦЕНАРИЙ 6: Отмена заявки (сразу)")
    app = Application(create_fsm())
    print(f"Начальное состояние: {app.current_state.name}\n")
    app.perform_action(Event.CANCEL)
    app.perform_action(Event.NOTIFICATION_SENT)
    print(f"\nФинальное состояние: {app.current_state.name}")


def simulate_cancel_after_auth():
    print_header("СЦЕНАРИЙ 7: Отмена заявки (после авторизации)")
    app = Application(create_fsm())
    print(f"Начальное состояние: {app.current_state.name}\n")
    app.perform_action(Event.AUTHORIZED)
    app.perform_action(Event.CANCEL)
    app.perform_action(Event.NOTIFICATION_SENT)
    print(f"\nФинальное состояние: {app.current_state.name}")


if __name__ == "__main__":
    simulate_success_online()
    simulate_success_courier()
    simulate_auth_failure()
    simulate_online_signing_failure()
    simulate_money_transfer_failure()
    simulate_cancel_at_new()
    simulate_cancel_after_auth()
    print_header("ВСЕ СЦЕНАРИИ ЗАВЕРШЕНЫ")
