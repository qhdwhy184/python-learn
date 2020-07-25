from Inheritate.parent import Parent


class Boy(Parent):
    def __init__(self, internal_boy):
        self.notify("test1")
        self._internal_boy = internal_boy
        self._internal_boy.notify = self.notify
    #     self._internal_boy.notify = self._notify
    #
    # def _notify(self, msg):
    #     print("Boy _notify")
    #     self.notify(msg)

    def work(self):
        self._internal_boy.notify = self.notify