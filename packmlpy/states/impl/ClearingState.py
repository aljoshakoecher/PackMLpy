
from packmlpy.states.ActiveStateName import ActiveStateName
from packmlpy.states.impl.StoppedState import StoppedState
from packmlpy.states.AbortableState import AbortableState
import asyncio
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from packmlpy.statemachine.PackMlStateMachine import PackMlStateMachine

class ClearingState(AbortableState):
	"""
	The ClearingState denotes a transitive state that can be used to clear a machine from damaged products after it was aborted. After the
	clearing action has been executed, the state machine will change to the StoppedState.
	"""

	def start(self, stateMachine: 'PackMlStateMachine'):
		pass # Start cannot be fired from Clearing -> Do nothing except maybe giving a warning

	def hold(self, stateMachine: 'PackMlStateMachine'):
		pass # Hold cannot be fired from Clearing -> Do nothing except maybe giving a warning

	def unhold(self, stateMachine: 'PackMlStateMachine'):
		pass # Unhold cannot be fired from Clearing -> Do nothing except maybe giving a warning

	def suspend(self, stateMachine: 'PackMlStateMachine'):
		pass # Suspend cannot be fired from Clearing -> Do nothing except maybe giving a warning

	def unsuspend(self, stateMachine: 'PackMlStateMachine'):
		pass # Unsuspend cannot be fired from Clearing -> Do nothing except maybe giving a warning

	def reset(self, stateMachine: 'PackMlStateMachine'):
		pass # Reset cannot be fired from Clearing -> Do nothing except maybe giving a warning

	def stop(self, stateMachine: 'PackMlStateMachine'):
		pass # Stop cannot be fired from Clearing -> Do nothing except maybe giving a warning

	def clear(self, stateMachine: 'PackMlStateMachine'):
		pass # Clear cannot be fired from Clearing -> Do nothing except maybe giving a warning

	async def executeActionAndComplete(self, stateMachine: 'PackMlStateMachine'):
		actionToRun = stateMachine.getStateActionManager().getAction(ActiveStateName.Clearing)
		await self.executeAction(actionToRun)

		# Make sure the current state is still Clearing before going to Stopped (could have been changed in the mean time).
		if (isinstance(stateMachine.getState(), ClearingState)):
			stateMachine.setStateAndRunAction(StoppedState())
