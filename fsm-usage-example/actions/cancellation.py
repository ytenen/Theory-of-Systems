"""Cancellation actions"""

def notify_cancellation(app):
    msg = app.current_event.error_message if app.current_event.error_message else "Заявка отменена"
    print(f"[ACTION] Отправка уведомления: {msg}")

def finalize_cancellation(app):
    print("[ACTION] Заявка закрыта (отмена)")
