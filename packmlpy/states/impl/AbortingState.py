from packmlpy.states.State import State
from packmlpy.states.ActiveStateName import ActiveStateName

from typing import TYPE_CHECKING
import asyncio

if TYPE_CHECKING:
	from packmlpy.statemachine.PackMlStateMachine import PackMlStateMachine

class AbortingState(State):
	"""
	* The AbortingState denotes a transitive state that should bring a machine to a sudden halt. Damages on products have to be expected. From
	* Aborting, no commands are accepted. After executing its action, the state machine will change to the AbortedState.
	"""

	from packmlpy.states.impl.AbortedState import AbortedState

	def start(self, stateMachine: 'PackMlStateMachine'):
		pass # Start cannot be fired from Aborting -> Do nothing except maybe giving a warning

	def hold(self, stateMachine: 'PackMlStateMachine'):
		pass # Hold cannot be fired from Aborting -> Do nothing except maybe giving a warning

	def unhold(self, stateMachine: 'PackMlStateMachine'):
		pass # Unhold cannot be fired from Aborting -> Do nothing except maybe giving a warning

	def suspend(self, stateMachine: 'PackMlStateMachine'):
		pass # Suspend cannot be fired from Aborting -> Do nothing except maybe giving a warning

	def unsuspend(self, stateMachine: 'PackMlStateMachine'):
		pass # Unsuspend cannot be fired from Aborting -> Do nothing except maybe giving a warning

	def reset(self, stateMachine: 'PackMlStateMachine'):
		pass # Reset cannot be fired from Aborting -> Do nothing except maybe giving a warning

	def stop(self, stateMachine: 'PackMlStateMachine'):
		pass # Stop cannot be fired from Aborting -> Do nothing except maybe giving a warning

	def abort(self, stateMachine: 'PackMlStateMachine'):
		pass # Abort cannot be fired from Aborting -> Do nothing except maybe giving a warning

	def clear(self, stateMachine: 'PackMlStateMachine'):
		pass # Clear cannot be fired from Aborting -> Do nothing except maybe giving a warning

	async def executeActionAndComplete(self, stateMachine: 'PackMlStateMachine'):
		actionToRun = stateMachine.getStateActionManager().getAction(ActiveStateName.Aborting)
		await self.executeAction(actionToRun)

		# Make sure the current state is still Aborting before going to Aborted (could have been changed in the mean time).
		if (isinstance(stateMachine.getState(), AbortingState)):
			stateMachine.setStateAndRunAction(self.AbortedState())
