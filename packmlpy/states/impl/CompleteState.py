from packmlpy.states.StoppableState import StoppableState
from packmlpy.states.impl.ResettingState import ResettingState
from typing import TYPE_CHECKING
import asyncio

if TYPE_CHECKING:
	from packmlpy.statemachine.PackMlStateMachine import PackMlStateMachine

class CompleteState (StoppableState):
	"""
	The CompleteState denotes a state in which the machine has completed production. In order to start the next order, a reset command is
	necessary to transition to IdleState.
	"""

	def start(self, stateMachine: 'PackMlStateMachine'):
		pass # Start cannot be fired from Complete -> Do nothing except maybe giving a warning

	def hold(self, stateMachine: 'PackMlStateMachine'):
		pass # Hold cannot be fired from Complete -> Do nothing except maybe giving a warning

	def unhold(self, stateMachine: 'PackMlStateMachine'):
		pass # Unhold cannot be fired from Complete -> Do nothing except maybe giving a warning

	def suspend(self, stateMachine: 'PackMlStateMachine'):
		pass # Suspend cannot be fired from Complete -> Do nothing except maybe giving a warning

	def unsuspend(self, stateMachine: 'PackMlStateMachine'):
		pass # Unsuspend cannot be fired from Complete -> Do nothing except maybe giving a warning

	def reset(self, stateMachine: 'PackMlStateMachine'):
		stateMachine.setStateAndRunAction(ResettingState())

	def clear(self, stateMachine: 'PackMlStateMachine'):
		pass # Clear cannot be fired from Clearing -> Do nothing except maybe giving a warning
