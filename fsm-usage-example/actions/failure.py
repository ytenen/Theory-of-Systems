"""Failure handling and notifications"""

def notify_failure(app):
    if app.failure_reason:
        print(f"[ACTION] Отправка уведомления: Ошибка по заявке - {app.failure_reason}")
    else:
        print("[ACTION] Отправка уведомления: Ошибка по заявке - Неизвестная ошибка")

def handle_authorization_failed(app):
    app.failure_reason = app.current_event.error_message
    notify_failure(app)

def handle_online_signing_failed(app):
    app.failure_reason = app.current_event.error_message
    notify_failure(app)

def handle_courier_signing_failed(app):
    app.failure_reason = app.current_event.error_message
    notify_failure(app)

def handle_money_transfer_failed(app):
    app.failure_reason = app.current_event.error_message
    notify_failure(app)
