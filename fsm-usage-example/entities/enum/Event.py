import enum

class Event(enum.Enum):
    CANCEL = ("CANCEL", "Заявка отменена пользователем")

    AUTHORIZATION_FAILED = ("AUTHORIZATION_FAILED", "Ошибка авторизации клиента")
    AUTHORIZED = ("AUTHORIZED", None)

    NOTIFICATION_SENT = ("NOTIFICATION_SENT", None)

    ONLINE_DOCUMENTS_SIGNING = ("ONLINE_DOCUMENTS_SIGNING", None)
    COURIER_DOCUMENTS_SIGNING = ("COURIER_DOCUMENTS_SIGNING", None)

    ONLINE_SIGNING_FAILED = ("ONLINE_SIGNING_FAILED", "Ошибка онлайн-подписания")
    COURIER_SIGNING_FAILED = ("COURIER_SIGNING_FAILED", "Ошибка подписания курьером")

    ONLINE_SIGNING_COMPLETED = ("ONLINE_SIGNING_COMPLETED", None)
    COURIER_SIGNING_COMPLETED = ("COURIER_SIGNING_COMPLETED", None)

    MONEY_TRANSFER_IS_READY = ("MONEY_TRANSFER_IS_READY", None)

    MONEY_TRANSFER_COMPLETED = ("MONEY_TRANSFER_COMPLETED", None)
    MONEY_TRANSFER_FAILED = ("MONEY_TRANSFER_FAILED", "Ошибка перевода средств")

    def __init__(self, event_name, error_message):
        self.event_name = event_name
        self.error_message = error_message
