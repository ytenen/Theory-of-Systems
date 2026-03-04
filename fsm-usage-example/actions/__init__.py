"""Actions module for FSM state transitions"""

from .cancellation import notify_cancellation, finalize_cancellation
from .failure import (
    notify_failure,
    handle_authorization_failed,
    handle_online_signing_failed,
    handle_courier_signing_failed,
    handle_money_transfer_failed,
)
from .signing import start_online_signing, start_courier_signing, complete_signing
from .transfer import prepare_money_transfer, complete_money_transfer
from .authorization import authorize_application
from .finalization import finalize_failure, finalize_completion

__all__ = [
    "notify_cancellation",
    "finalize_cancellation",
    "notify_failure",
    "handle_authorization_failed",
    "handle_online_signing_failed",
    "handle_courier_signing_failed",
    "handle_money_transfer_failed",
    "start_online_signing",
    "start_courier_signing",
    "complete_signing",
    "prepare_money_transfer",
    "complete_money_transfer",
    "authorize_application",
    "finalize_failure",
    "finalize_completion",
]
