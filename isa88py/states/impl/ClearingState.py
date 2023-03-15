from isa88py.statemachine.Isa88StateMachine import Isa88StateMachine
from isa88py.states.AbortableState import AbortableState
from isa88py.states.ActiveStateName import ActiveStateName
from isa88py.states.impl.StoppedState import StoppedState

class ClearingState(AbortableState):
	"""
	The ClearingState denotes a transitive state that can be used to clear a machine from damaged products after it was aborted. After the
	clearing action has been executed, the state machine will change to the StoppedState.
	"""

	def start(self, stateMachine: Isa88StateMachine):
		pass # Start cannot be fired from Clearing -> Do nothing except maybe giving a warning

	def hold(self, stateMachine: Isa88StateMachine):
		pass # Hold cannot be fired from Clearing -> Do nothing except maybe giving a warning

	def unhold(self, stateMachine: Isa88StateMachine):
		pass # Unhold cannot be fired from Clearing -> Do nothing except maybe giving a warning

	def suspend(self, stateMachine: Isa88StateMachine):
		pass # Suspend cannot be fired from Clearing -> Do nothing except maybe giving a warning

	def unsuspend(self, stateMachine: Isa88StateMachine):
		pass # Unsuspend cannot be fired from Clearing -> Do nothing except maybe giving a warning

	def reset(self, stateMachine: Isa88StateMachine):
		pass # Reset cannot be fired from Clearing -> Do nothing except maybe giving a warning

	def stop(self, stateMachine: Isa88StateMachine):
		pass # Stop cannot be fired from Clearing -> Do nothing except maybe giving a warning

	def clear(self, stateMachine: Isa88StateMachine):
		pass # Clear cannot be fired from Clearing -> Do nothing except maybe giving a warning

	async def executeActionAndComplete(self, stateMachine: Isa88StateMachine):
		actionToRun = stateMachine.getStateActionManager().getAction(ActiveStateName.Clearing)
		self.executeAction(actionToRun)

		# Make sure the current state is still Clearing before going to Stopped (could have been changed in the mean time).
		if (isinstance(stateMachine.getState(), ClearingState)):
			coro = stateMachine.setStateAndRunAction(StoppedState())
