from packmlpy.states.ActiveStateName import ActiveStateName
from packmlpy.states.StoppableState import StoppableState
from typing import TYPE_CHECKING
import asyncio

if TYPE_CHECKING:
	from packmlpy.statemachine.PackMlStateMachine import PackMlStateMachine


class UnholdingState (StoppableState):
	"""
	The UnholdingState denotes a transitive state that is entered after the machine has been suspended and an unhold command has been issued. After executing the action the state
	machine will transition back to the ExecuteState.
	"""

	def start(self, stateMachine: 'PackMlStateMachine'):
		pass # Start cannot be fired from Unholding -> Do nothing except maybe giving a warning

	def hold(self, stateMachine: 'PackMlStateMachine'):
		pass # Hold cannot be fired from Unholding -> Do nothing except maybe giving a warning

	def unhold(self, stateMachine: 'PackMlStateMachine'):
		pass # Unhold cannot be fired from Unholding -> Do nothing except maybe giving a warning

	def suspend(self, stateMachine: 'PackMlStateMachine'):
		pass # Start cannot be fired from Unholding -> Do nothing except maybe giving a warning

	def unsuspend(self, stateMachine: 'PackMlStateMachine'):
		pass # Unsuspend cannot be fired from Unholding -> Do nothing except maybe giving a warning

	def reset(self, stateMachine: 'PackMlStateMachine'):
		pass # Reset cannot be fired from Unholding -> Do nothing except maybe giving a warning

	def clear(self, stateMachine: 'PackMlStateMachine'):
		pass # Clear cannot be fired from Unholding -> Do nothing except maybe giving a warning

	async def executeActionAndComplete(self, stateMachine: 'PackMlStateMachine'):
		actionToRun = stateMachine.getStateActionManager().getAction(ActiveStateName.Unholding)
		await self.executeAction(actionToRun)

		# Make sure the current state is still Unholding before going to Execute (could have been changed in the mean time).
		if (isinstance(stateMachine.getState(), UnholdingState)):
			from packmlpy.states.impl.ExecuteState import ExecuteState
			stateMachine.setStateAndRunAction(ExecuteState())

