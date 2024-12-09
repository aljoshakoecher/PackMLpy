from packmlpy.states.ActiveStateName import ActiveStateName
from packmlpy.states.StoppableState import StoppableState
from packmlpy.states.impl.HoldingState import HoldingState
from packmlpy.states.impl.SuspendingState import SuspendingState
from packmlpy.states.impl.CompletingState import CompletingState
from typing import TYPE_CHECKING
import asyncio

if TYPE_CHECKING:
	from packmlpy.statemachine.PackMlStateMachine import PackMlStateMachine


class ExecuteState (StoppableState):
	"""
	The ExecuteState denotes a transitive state that contains the main execution actions that are responsible for actual production. After
	completing execution, the state machine will change to the CompletingState.
	"""

	def start(self, stateMachine: 'PackMlStateMachine'):
		pass # Start cannot be fired from Execute -> Do nothing except maybe giving a warning

	def hold(self, stateMachine: 'PackMlStateMachine'):
		stateMachine.setStateAndRunAction(HoldingState())

	def unhold(self, stateMachine: 'PackMlStateMachine'):
		pass # Unhold cannot be fired from Execute -> Do nothing except maybe giving a warning

	def suspend(self, stateMachine: 'PackMlStateMachine'):
		stateMachine.setStateAndRunAction(SuspendingState())

	def unsuspend(self, stateMachine: 'PackMlStateMachine'):
		pass # Unsuspend cannot be fired from Execute -> Do nothing except maybe giving a warning

	def reset(self, stateMachine: 'PackMlStateMachine'):
		pass # Reset cannot be fired from Execute -> Do nothing except maybe giving a warning

	def clear(self, stateMachine: 'PackMlStateMachine'):
		pass # Clear cannot be fired from Execute -> Do nothing except maybe giving a warning

	async def executeActionAndComplete(self, stateMachine: 'PackMlStateMachine'):
		actionToRun = stateMachine.getStateActionManager().getAction(ActiveStateName.Execute)
		await self.executeAction(actionToRun)
	
		# Make sure the current state is still Execute before going to Completing (could have been changed in the mean time).
		if (isinstance(stateMachine.getState(), ExecuteState)):
			stateMachine.setStateAndRunAction(CompletingState())
