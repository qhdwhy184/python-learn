class MonitorNotifier():
    def __init__(self, boy):
        self._boy = boy

    def work(self):
        self._boy.notify("MonitorNotifier.notify1")
        self._boy.notify = self.notify
        self._boy.notify("MonitorNotifier.notify2")

    def notify(self, msg):
        print("MonitorNotifier notify :{}".format(msg))