from poll.main.app import PollMain, manage_addPollMain, addPollMain

def initialize(registrar):
    registrar.registerClass(
        PollMain,
        constructors=(manage_addPollMain, addPollMain)
    )