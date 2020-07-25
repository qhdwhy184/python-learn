from Inheritate.parent import Parent


class InternalBoy(Parent):

    def work(self):
        print("InternalBoy work")
        self.notify("InternalBoy: work")
