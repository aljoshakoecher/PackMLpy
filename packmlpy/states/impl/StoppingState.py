from packmlpy.states.ActiveStateName import ActiveStateName
from packmlpy.states.AbortableState import AbortableState
from packmlpy.states.impl.StoppedState import StoppedState
import asyncio

from typing import TYPE_CHECKING
import asyncio

if TYPE_CHECKING:
	from packmlpy.statemachine.PackMlStateMachine import PackMlStateMachine

class StoppingState (AbortableState):
	"""
	The StoppingState denotes a transitive state that should bring a machine to a sudden halt. Contrary to actions in AbortingState,
	actions in StoppingState should not lead to product damages. After having executed the action in stopping, the state machine will
	transition to the StoppedState.
	"""

	def start(self, stateMachine: 'PackMlStateMachine'):
		pass # Start cannot be fired from Stopping -> Do nothing except maybe giving a warning

	def hold(self, stateMachine: 'PackMlStateMachine'):
		pass # Hold cannot be fired from Stopping -> Do nothing except maybe giving a warning

	def unhold(self, stateMachine: 'PackMlStateMachine'):
		pass # Unhold cannot be fired from Stopping -> Do nothing except maybe giving a warning

	def suspend(self, stateMachine: 'PackMlStateMachine'):
		pass # Start cannot be fired from Stopping -> Do nothing except maybe giving a warning

	def unsuspend(self, stateMachine: 'PackMlStateMachine'):
		pass # Unsuspend cannot be fired from Stopping -> Do nothing except maybe giving a warning

	def reset(self, stateMachine: 'PackMlStateMachine'):
		pass # Reset cannot be fired from Stopping -> Do nothing except maybe giving a warning

	def clear(self, stateMachine: 'PackMlStateMachine'):
		pass # Clear cannot be fired from Stopping -> Do nothing except maybe giving a warning

	async def executeActionAndComplete(self, stateMachine: 'PackMlStateMachine'):
		actionToRun = stateMachine.getStateActionManager().getAction(ActiveStateName.Stopping)
		await self.executeAction(actionToRun)

		# Make sure the current state is still Stopping before going to Stopped (could have been changed in the mean time).
		if (isinstance(stateMachine.getState(), StoppingState)):
			stateMachine.setStateAndRunAction(StoppedState())

