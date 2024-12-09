from packmlpy.states.ActiveStateName import ActiveStateName
from packmlpy.states.StoppableState import StoppableState
from packmlpy.states.impl.HeldState import HeldState
from typing import TYPE_CHECKING
import asyncio

if TYPE_CHECKING:
	from packmlpy.statemachine.PackMlStateMachine import PackMlStateMachine

class HoldingState (StoppableState):
	"""
	The HoldingState denotes a transitive state that brings a machine to a stop when internal conditions prevent further production. After
	having completed holding procedure, the state machine will change to the HeldState.
	"""	

	def start(self, stateMachine: 'PackMlStateMachine'):
		pass # Start cannot be fired from Holding -> Do nothing except maybe giving a warning

	def hold(self, stateMachine: 'PackMlStateMachine'):
		pass # Hold cannot be fired from Holding -> Do nothing except maybe giving a warning

	def unhold(self, stateMachine: 'PackMlStateMachine'):
		pass # Unhold cannot be fired from Holding -> Do nothing except maybe giving a warning

	def suspend(self, stateMachine: 'PackMlStateMachine'):
		pass # Start cannot be fired from Holding -> Do nothing except maybe giving a warning

	def unsuspend(self, stateMachine: 'PackMlStateMachine'):
		pass # Unsuspend cannot be fired from Holding -> Do nothing except maybe giving a warning

	def reset(self, stateMachine: 'PackMlStateMachine'):
		pass # Reset cannot be fired from Holding -> Do nothing except maybe giving a warning

	def clear(self, stateMachine: 'PackMlStateMachine'):
		pass # Clear cannot be fired from Holding -> Do nothing except maybe giving a warning

	async def executeActionAndComplete(self, stateMachine: 'PackMlStateMachine'):
		actionToRun = stateMachine.getStateActionManager().getAction(ActiveStateName.Holding)
		await self.executeAction(actionToRun)
		
		# Make sure the current state is still Holding before going to Held (could have been changed in the mean time).
		if (isinstance(stateMachine.getState(), HoldingState)):
			stateMachine.setStateAndRunAction(HeldState())

