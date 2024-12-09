from packmlpy.states.AbortableState import AbortableState
import asyncio
from typing import TYPE_CHECKING
import asyncio

if TYPE_CHECKING:
	from packmlpy.statemachine.PackMlStateMachine import PackMlStateMachine

class StoppedState (AbortableState):
	"""
	The StoppedState denotes a state in which the machine is powered and stationary. Communications with other systems are functioning. A
	reset-command will cause a transition from StoppedState to ResettingState.
	"""

	def start(self, stateMachine: 'PackMlStateMachine'):
		pass # Start cannot be fired from Stopped -> Do nothing except maybe giving a warning

	def hold(self, stateMachine: 'PackMlStateMachine'):
		pass # Hold cannot be fired from Stopped -> Do nothing except maybe giving a warning

	def unhold(self, stateMachine: 'PackMlStateMachine'):
		pass # Unhold cannot be fired from Stopped -> Do nothing except maybe giving a warning

	def suspend(self, stateMachine: 'PackMlStateMachine'):
		pass # Suspend cannot be fired from Stopped -> Do nothing except maybe giving a warning

	def unsuspend(self, stateMachine: 'PackMlStateMachine'):
		pass # Unsuspend cannot be fired from Stopped -> Do nothing except maybe giving a warning

	def reset(self, stateMachine: 'PackMlStateMachine'):
		from packmlpy.states.impl.ResettingState import ResettingState
		stateMachine.setStateAndRunAction(ResettingState())

	def clear(self, stateMachine: 'PackMlStateMachine'):
		pass # Clear cannot be fired from Stopped -> Do nothing except maybe giving a warning

