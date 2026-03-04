from entities.State import State as StateClass
from entities.enum.State import State as StateEnum
from entities.enum.Event import Event
from actions import *


#FSM CREATION

def create_fsm():
    states = {}
    for state_enum in StateEnum:
        is_terminal = state_enum in [
            StateEnum.CANCELLED,
            StateEnum.FAILED,
            StateEnum.COMPLETED
        ]
        states[state_enum] = StateClass(state_enum.value, is_terminal)


    #NEW
    states[StateEnum.NEW].add_transition(Event.CANCEL, states[StateEnum.NOTIFY_CANCELLED], notify_cancellation)
    states[StateEnum.NEW].add_transition(Event.AUTHORIZATION_FAILED, states[StateEnum.NOTIFY_FAILED], handle_authorization_failed)
    states[StateEnum.NEW].add_transition(Event.AUTHORIZED, states[StateEnum.AUTHORIZED_APPLICATION], authorize_application)

    #AUTHORIZED_APPLICATION
    states[StateEnum.AUTHORIZED_APPLICATION].add_transition(Event.CANCEL, states[StateEnum.NOTIFY_CANCELLED], notify_cancellation)
    states[StateEnum.AUTHORIZED_APPLICATION].add_transition(Event.ONLINE_DOCUMENTS_SIGNING, states[StateEnum.ONLINE_SIGNING], start_online_signing)
    states[StateEnum.AUTHORIZED_APPLICATION].add_transition(Event.COURIER_DOCUMENTS_SIGNING, states[StateEnum.COURIER_SIGNING], start_courier_signing)

    #NOTIFY_CANCELLED
    states[StateEnum.NOTIFY_CANCELLED].add_transition(Event.NOTIFICATION_SENT, states[StateEnum.CANCELLED], finalize_cancellation)

    #ONLINE_SIGNING
    states[StateEnum.ONLINE_SIGNING].add_transition(Event.CANCEL, states[StateEnum.NOTIFY_CANCELLED], notify_cancellation)
    states[StateEnum.ONLINE_SIGNING].add_transition(Event.ONLINE_SIGNING_FAILED, states[StateEnum.NOTIFY_FAILED], handle_online_signing_failed)
    states[StateEnum.ONLINE_SIGNING].add_transition(Event.ONLINE_SIGNING_COMPLETED, states[StateEnum.SIGNED_APPLICATION], complete_signing)

    #COURIER_SIGNING
    states[StateEnum.COURIER_SIGNING].add_transition(Event.CANCEL, states[StateEnum.NOTIFY_CANCELLED], notify_cancellation)
    states[StateEnum.COURIER_SIGNING].add_transition(Event.COURIER_SIGNING_FAILED, states[StateEnum.NOTIFY_FAILED], handle_courier_signing_failed)
    states[StateEnum.COURIER_SIGNING].add_transition(Event.COURIER_SIGNING_COMPLETED, states[StateEnum.SIGNED_APPLICATION], complete_signing)

    #SIGNED_APPLICATION
    states[StateEnum.SIGNED_APPLICATION].add_transition(Event.CANCEL, states[StateEnum.NOTIFY_CANCELLED], notify_cancellation)
    states[StateEnum.SIGNED_APPLICATION].add_transition(Event.MONEY_TRANSFER_IS_READY, states[StateEnum.MONEY_TRANSFERRING], prepare_money_transfer)

    #MONEY_TRANSFERRING
    states[StateEnum.MONEY_TRANSFERRING].add_transition(Event.MONEY_TRANSFER_COMPLETED, states[StateEnum.COMPLETED], complete_money_transfer)
    states[StateEnum.MONEY_TRANSFERRING].add_transition(Event.MONEY_TRANSFER_FAILED, states[StateEnum.NOTIFY_FAILED], handle_money_transfer_failed)

    #NOTIFY_FAILED
    states[StateEnum.NOTIFY_FAILED].add_transition(Event.NOTIFICATION_SENT, states[StateEnum.FAILED], finalize_failure)

    return states[StateEnum.NEW]
