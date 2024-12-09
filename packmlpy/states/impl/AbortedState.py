
from packmlpy.states.State import State
import asyncio
from typing import TYPE_CHECKING
import asyncio

if TYPE_CHECKING:
	from packmlpy.statemachine.PackMlStateMachine import PackMlStateMachine

class AbortedState(State):
	"""
	The AbortedState denotes a state in which the machine has been brought to a sudden halt. A
	clear-command is necessary to transition to StoppedState.
	"""

	def start(self, stateMachine: 'PackMlStateMachine'):
		pass # Start cannot be fired from Aborted -> Do nothing except maybe giving a warning


	def hold(self, stateMachine: 'PackMlStateMachine'):
		pass # Hold cannot be fired from Aborted -> Do nothing except maybe giving a warning


	def unhold(self, stateMachine: 'PackMlStateMachine'):
		pass # Unhold cannot be fired from Aborted -> Do nothing except maybe giving a warning


	def suspend(self, stateMachine: 'PackMlStateMachine'):
		pass # Suspend cannot be fired from Aborted -> Do nothing except maybe giving a warning


	def unsuspend(self, stateMachine: 'PackMlStateMachine'):
		pass # Unsuspend cannot be fired from Aborted -> Do nothing except maybe giving a warning


	def reset(self, stateMachine: 'PackMlStateMachine'):
		pass # Reset cannot be fired from Aborted -> Do nothing except maybe giving a warning


	def stop(self, stateMachine: 'PackMlStateMachine'):
		pass # Stop cannot be fired from Aborted -> Do nothing except maybe giving a warning


	def abort(self, stateMachine: 'PackMlStateMachine'):
		pass # Abort cannot be fired from Aborted -> Do nothing except maybe giving a warning


	def clear(self, stateMachine: 'PackMlStateMachine'):
		from packmlpy.states.impl.ClearingState import ClearingState
		stateMachine.setStateAndRunAction(ClearingState())
