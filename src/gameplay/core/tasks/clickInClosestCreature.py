import time
import src.utils.keyboard as keyboard
import src.utils.mouse as mouse
from ...typings import Context
from .common.base import BaseTask

class ClickInClosestCreatureTask(BaseTask):
    def __init__(self):
        super().__init__()
        self.name = 'clickInClosestCreature'
        self.delayOfTimeout = 1

    def shouldIgnore(self, context: Context) -> bool:
        return context.get('ng_cave', {}).get('targetCreature') is not None or context.get('ng_cave', {}).get('isAttackingSomeCreature', False)

    def did(self, context: Context) -> bool:
        return context.get('ng_cave', {}).get('isAttackingSomeCreature', False)

    def do(self, context: Context) -> Context:
        if context.get('ng_cave', {}).get('isAttackingSomeCreature', False) == False:
            # TODO: find another way (maybe click in battle)
            # attack by mouse click when there are players on screen or ignorable creatures
            if context.get('gameWindow', {}).get('players') or context.get('ng_targeting', {}).get('hasIgnorableCreatures'):
                keyboard.keyDown('alt')
                mouse.leftClick(context['ng_cave']['closestCreature']['windowCoordinate'])
                keyboard.keyUp('alt')
                return context
            keyboard.press('space')

        return context