from Inheritate.notifier import MonitorNotifier
from Inheritate.boy import Boy
from Inheritate.internal_boy import InternalBoy

internal_boy = InternalBoy()
boy = Boy(internal_boy)

monitor_notifier = MonitorNotifier(boy)
monitor_notifier.work()
boy.work()


internal_boy.work()


