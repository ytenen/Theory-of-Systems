from entities.State import State as StateClass
from entities.enum.State import State as StateEnum
from entities.enum.Event import Event


# === ACTION FUNCTIONS ===

def notify_cancellation(**kwargs):
    """Уведомление пользователя об отмене заявки"""
    print("[ACTION] Отправка уведомления: Заявка отменена")


def notify_failure(**kwargs):
    """Уведомление пользователя об ошибке"""
    reason = kwargs.get('reason', 'Неизвестная ошибка')
    print(f"[ACTION] Отправка уведомления: Ошибка по заявке - {reason}")


def authorize_application(**kwargs):
    """Авторизация заявки в системе"""
    print("[ACTION] Авторизация заявки в кредитной системе")


def send_notification(**kwargs):
    """Отправка уведомления пользователю"""
    print("[ACTION] Отправка push/SMS уведомления пользователю")


def start_online_signing(**kwargs):
    """Начало онлайн-подписания документов"""
    print("[ACTION] Инициализация онлайн-подписания документов")


def start_courier_signing(**kwargs):
    """Вызов курьера для подписания"""
    print("[ACTION] Создание задания для курьера")


def handle_online_signing_failed(**kwargs):
    """Обработка ошибки онлайн-подписания"""
    print("[ACTION] Логирование ошибки онлайн-подписания")


def handle_courier_signing_failed(**kwargs):
    """Обработка ошибки подписания курьером"""
    print("[ACTION] Логирование ошибки подписания курьером")


def complete_signing(**kwargs):
    """Завершение подписания документов"""
    print("[ACTION] Документы подписаны, архивирование")


def prepare_money_transfer(**kwargs):
    """Подготовка перевода денег"""
    print("[ACTION] Резервирование средств для перевода")


def complete_money_transfer(**kwargs):
    """Успешный перевод денег"""
    print("[ACTION] Деньги переведены на счет клиента")


def handle_money_transfer_failed(**kwargs):
    """Обработка ошибки перевода"""
    print("[ACTION] Логирование ошибки перевода, разблокировка средств")


def finalize_cancellation(**kwargs):
    """Финализация отмены"""
    print("[ACTION] Заявка закрыта (отмена)")


def finalize_failure(**kwargs):
    """Финализация ошибки"""
    print("[ACTION] Заявка закрыта (ошибка)")


def finalize_completion(**kwargs):
    """Финализация успешного завершения"""
    print("[ACTION] Заявка закрыта (успешно)")


# === FSM CREATION ===

def create_fsm():
    states = {}
    for state_enum in StateEnum:
        is_terminal = state_enum in [
            StateEnum.CANCELLED,
            StateEnum.FAILED,
            StateEnum.COMPLETED
        ]
        states[state_enum] = StateClass(state_enum.value, is_terminal)

    # Настраиваем переходы

    # NEW -> Уведомление об отмене/ошибке или авторизация
    states[StateEnum.NEW].add_transition(Event.CANCEL, states[StateEnum.NOTIFY_CANCELLED], notify_cancellation)
    states[StateEnum.NEW].add_transition(Event.AUTHORIZATION_FAILED, states[StateEnum.NOTIFY_FAILED], notify_failure)
    states[StateEnum.NEW].add_transition(Event.AUTHORIZED, states[StateEnum.AUTHORIZED_APPLICATION], authorize_application)

    # AUTHORIZED_APPLICATION -> Уведомление или выбор способа подписания
    states[StateEnum.AUTHORIZED_APPLICATION].add_transition(Event.CANCEL, states[StateEnum.NOTIFY_CANCELLED], notify_cancellation)
    states[StateEnum.AUTHORIZED_APPLICATION].add_transition(Event.ONLINE_DOCUMENTS_SIGNING, states[StateEnum.ONLINE_SIGNING], start_online_signing)
    states[StateEnum.AUTHORIZED_APPLICATION].add_transition(Event.COURIER_DOCUMENTS_SIGNING, states[StateEnum.COURIER_SIGNING], start_courier_signing)

    # NOTIFY_CANCELLED -> CANCELLED (терминальное)
    states[StateEnum.NOTIFY_CANCELLED].add_transition(Event.NOTIFICATION_SENT, states[StateEnum.CANCELLED], finalize_cancellation)

    # ONLINE_SIGNING -> Отмена, ошибка или завершение
    states[StateEnum.ONLINE_SIGNING].add_transition(Event.CANCEL, states[StateEnum.NOTIFY_CANCELLED], notify_cancellation)
    states[StateEnum.ONLINE_SIGNING].add_transition(Event.ONLINE_SIGNING_FAILED, states[StateEnum.NOTIFY_FAILED], handle_online_signing_failed)
    states[StateEnum.ONLINE_SIGNING].add_transition(Event.ONLINE_SIGNING_COMPLETED, states[StateEnum.SIGNED_APPLICATION], complete_signing)

    # COURIER_SIGNING -> Отмена, ошибка или завершение
    states[StateEnum.COURIER_SIGNING].add_transition(Event.CANCEL, states[StateEnum.NOTIFY_CANCELLED], notify_cancellation)
    states[StateEnum.COURIER_SIGNING].add_transition(Event.COURIER_SIGNING_FAILED, states[StateEnum.NOTIFY_FAILED], handle_courier_signing_failed)
    states[StateEnum.COURIER_SIGNING].add_transition(Event.COURIER_SIGNING_COMPLETED, states[StateEnum.SIGNED_APPLICATION], complete_signing)

    # SIGNED_APPLICATION -> Перевод денег
    states[StateEnum.SIGNED_APPLICATION].add_transition(Event.MONEY_TRANSFER_IS_READY, states[StateEnum.MONEY_TRANSFERRING], prepare_money_transfer)

    # MONEY_TRANSFERRING -> Завершение или ошибка (сначала уведомление)
    states[StateEnum.MONEY_TRANSFERRING].add_transition(Event.MONEY_TRANSFER_COMPLETED, states[StateEnum.COMPLETED], complete_money_transfer)
    states[StateEnum.MONEY_TRANSFERRING].add_transition(Event.MONEY_TRANSFER_FAILED, states[StateEnum.NOTIFY_FAILED], handle_money_transfer_failed)

    # NOTIFY_FAILED -> FAILED (терминальное)
    states[StateEnum.NOTIFY_FAILED].add_transition(Event.NOTIFICATION_SENT, states[StateEnum.FAILED], finalize_failure)

    return states[StateEnum.NEW]

