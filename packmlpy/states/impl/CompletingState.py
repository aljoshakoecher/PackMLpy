from packmlpy.states.ActiveStateName import ActiveStateName
from packmlpy.states.StoppableState import StoppableState
from packmlpy.states.impl.CompleteState import CompleteState
from typing import TYPE_CHECKING
import asyncio

if TYPE_CHECKING:
	from packmlpy.statemachine.PackMlStateMachine import PackMlStateMachine

class CompletingState (StoppableState):
	"""
	The CompletingState denotes a transitive state that can be used to bring production to an end (e.g. when the specified number of products
	have been produced). After the completing action has been executed, the state machine will change to the ExecuteState.
	"""

	def start(self, stateMachine: 'PackMlStateMachine'):
		pass # Start cannot be fired from Completing -> Do nothing except maybe giving a warning

	def hold(self, stateMachine: 'PackMlStateMachine'):
		pass # Hold cannot be fired from Completing -> Do nothing except maybe giving a warning

	def unhold(self, stateMachine: 'PackMlStateMachine'):
		pass # Unhold cannot be fired from Completing -> Do nothing except maybe giving a warning

	def suspend(self, stateMachine: 'PackMlStateMachine'):
		pass # Start cannot be fired from Completing -> Do nothing except maybe giving a warning

	def unsuspend(self, stateMachine: 'PackMlStateMachine'):
		pass # Unsuspend cannot be fired from Completing -> Do nothing except maybe giving a warning

	def reset(self, stateMachine: 'PackMlStateMachine'):
		pass # Reset cannot be fired from Completing -> Do nothing except maybe giving a warning

	def clear(self, stateMachine: 'PackMlStateMachine'):
		pass # Clear cannot be fired from Completing -> Do nothing except maybe giving a warning

	async def executeActionAndComplete(self, stateMachine: 'PackMlStateMachine'):
		actionToRun = stateMachine.getStateActionManager().getAction(ActiveStateName.Completing)
		await self.executeAction(actionToRun)
		
		# Make sure the current state is still Completing before going to Complete (could have been changed in the mean time).
		if (isinstance(stateMachine.getState(), CompletingState)):
			stateMachine.setStateAndRunAction(CompleteState())

