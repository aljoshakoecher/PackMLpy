from packmlpy.states.ActiveStateName import ActiveStateName
from packmlpy.states.StoppableState import StoppableState
from packmlpy.states.impl.ExecuteState import ExecuteState
from typing import TYPE_CHECKING
import time
import asyncio

if TYPE_CHECKING:
	from packmlpy.statemachine.PackMlStateMachine import PackMlStateMachine

class StartingState (StoppableState):
	"""
	The StartingState denotes a transitive state that should make a machine ready for producing. After having completed a startup procedure,
	the state machine will change to the ExecuteState.
	"""

	def start(self, stateMachine: 'PackMlStateMachine'):
		pass # Start cannot be fired from Starting -> Do nothing except maybe giving a warning

	def hold(self, stateMachine: 'PackMlStateMachine'):
		pass # Hold cannot be fired from Starting -> Do nothing except maybe giving a warning

	def unhold(self, stateMachine: 'PackMlStateMachine'):
		pass # Unhold cannot be fired from Starting -> Do nothing except maybe giving a warning

	def suspend(self, stateMachine: 'PackMlStateMachine'):
		pass # Start cannot be fired from Starting -> Do nothing except maybe giving a warning

	def unsuspend(self, stateMachine: 'PackMlStateMachine'):
		pass # Unsuspend cannot be fired from Starting -> Do nothing except maybe giving a warning

	def reset(self, stateMachine: 'PackMlStateMachine'):
		pass # Reset cannot be fired from Starting -> Do nothing except maybe giving a warning

	def clear(self, stateMachine: 'PackMlStateMachine'):
		pass # Clear cannot be fired from Starting -> Do nothing except maybe giving a warning

	async def executeActionAndComplete(self, stateMachine: 'PackMlStateMachine'):
		actionToRun = stateMachine.getStateActionManager().getAction(ActiveStateName.Starting)
		print("before action", time.time())
		await self.executeAction(actionToRun)
		# Make sure the current state is still Starting before going to Execute (could have been changed in the mean time).
		if (isinstance(stateMachine.getState(), StartingState)):
			print("going to execute", time.time())
			stateMachine.setStateAndRunAction(ExecuteState())

