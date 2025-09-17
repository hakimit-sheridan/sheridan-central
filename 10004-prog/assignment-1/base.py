"""
Defines the Attributes class
"""


class ActionItem:
    pass

    def use(self) -> int:
        return 0


# NOTE: maybe do the following:
# def = Attack Power
# dex = Attack Chance
# int = Item Power
# The player and enemy make a primary action [fight | run | useItem]. Each of these
# choices provides a set of further choices that determine the nature of the action.
# Attack matchup (takes precedence over dex) is based off the sub-action made.
# Both the player and the enemy make a sub-action, and the result is based off
# a rock-paper-scissors of the actions, each sub-action has a matchup.
# for example, if a warrior and a tinkerer were in a confrontation, the following could happen:
# warrior uses run: sprint(use 30 energy) to the left
# tinkerer uses item: net(use 40 energy) to the left
# warrior fails run, warrior caught: next move is skipped

# defence should affect ap like so:
# factor = def

# dex should affect chance like so:
# factor = 50 + dex

# should probably simplify the above


class Entity:
    """
    The attributes for a given entity
    """

    def __init__(
        self,
        defence: int,
        dexterity: int,
        intelligence: int,
        health: int,
        fightOpts: list[ActionItem],
        runOpts: list[ActionItem],
        itemOpts: list[ActionItem],
    ) -> None:
        """
        Setup attributes with the given values
        """

        self.defence: int = defence
        self.dexterity: int = dexterity
        self.intelligence: int = intelligence
        self.health: int = health
        self.energy: int = 100

        self.fightOpts: list[ActionItem] = fightOpts
        self.runOpts: list[ActionItem] = runOpts
        self.itemOpts: list[ActionItem] = itemOpts

    def fight(self, index: int) -> int:
        used = self.fightOpts[index].use()
        self.energy -= used
        return used

    def run(self, index: int) -> int:
        used = self.runOpts[index].use()
        self.energy -= used
        return used

    def item(self, index: int) -> int:
        used = self.itemOpts[index].use()
        self.energy -= used
        return used
