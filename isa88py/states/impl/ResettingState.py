from isa88py.states.ActiveStateName import ActiveStateName
from isa88py.states.StoppableState import StoppableState
from typing import TYPE_CHECKING

if TYPE_CHECKING:
	from isa88py.statemachine.Isa88StateMachine import Isa88StateMachine

class ResettingState (StoppableState):
	"""
	The ResettingState denotes a transitive state that brings a machine back to its IdleState after it had previously been stopped or
	aborted.
	"""

	def start(self, stateMachine: 'Isa88StateMachine'):
		pass # Start cannot be fired from Starting -> Do nothing except maybe giving a warning

	def hold(self, stateMachine: 'Isa88StateMachine'):
		pass # Hold cannot be fired from Starting -> Do nothing except maybe giving a warning

	def unhold(self, stateMachine: 'Isa88StateMachine'):
		pass # Unhold cannot be fired from Starting -> Do nothing except maybe giving a warning

	def suspend(self, stateMachine: 'Isa88StateMachine'):
		pass # Start cannot be fired from Starting -> Do nothing except maybe giving a warning

	def unsuspend(self, stateMachine: 'Isa88StateMachine'):
		pass # Unsuspend cannot be fired from Starting -> Do nothing except maybe giving a warning

	def reset(self, stateMachine: 'Isa88StateMachine'):
		pass # Reset cannot be fired from Starting -> Do nothing except maybe giving a warning

	def clear(self, stateMachine: 'Isa88StateMachine'):
		pass # Clear cannot be fired from Starting -> Do nothing except maybe giving a warning

	async def executeActionAndComplete(self, stateMachine: 'Isa88StateMachine'):
		actionToRun = stateMachine.getStateActionManager().getAction(ActiveStateName.Resetting)
		self.executeAction(actionToRun)

		# Make sure the current state is still Resetting before going to Idle (could have been changed in the mean time).
		if (isinstance(stateMachine.getState(), ResettingState)):
			from isa88py.states.impl.IdleState import IdleState
			coro = stateMachine.setStateAndRunAction(IdleState())

