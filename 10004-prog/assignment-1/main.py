import base


class Wizard(base.Entity):
    def __init__(self) -> None:
        super().__init__(20, 20, 40, 20, [], [], [])


class Artificer(base.Entity):
    def __init__(self) -> None:
        super().__init__(10, 30, 30, 20, [], [], [])


class Monster(base.Entity):
    def __init__(self) -> None:
        super().__init__(30, 30, 10, 30, [], [], [])
