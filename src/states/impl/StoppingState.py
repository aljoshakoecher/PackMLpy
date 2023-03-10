from statemachine.Isa88StateMachine import Isa88StateMachine
from states.ActiveStateName import ActiveStateName
from states.AbortableState import AbortableState
from states.impl.StoppedState import StoppedState

class StoppingState (AbortableState):
	"""
	The StoppingState denotes a transitive state that should bring a machine to a sudden halt. Contrary to actions in AbortingState,
	actions in StoppingState should not lead to product damages. After having executed the action in stopping, the state machine will
	transition to the StoppedState.
	"""

	def start(self, stateMachine: Isa88StateMachine):
		pass # Start cannot be fired from Stopping -> Do nothing except maybe giving a warning

	def hold(self, stateMachine: Isa88StateMachine):
		pass # Hold cannot be fired from Stopping -> Do nothing except maybe giving a warning

	def unhold(self, stateMachine: Isa88StateMachine):
		pass # Unhold cannot be fired from Stopping -> Do nothing except maybe giving a warning

	def suspend(self, stateMachine: Isa88StateMachine):
		pass # Start cannot be fired from Stopping -> Do nothing except maybe giving a warning

	def unsuspend(self, stateMachine: Isa88StateMachine):
		pass # Unsuspend cannot be fired from Stopping -> Do nothing except maybe giving a warning

	def reset(self, stateMachine: Isa88StateMachine):
		pass # Reset cannot be fired from Stopping -> Do nothing except maybe giving a warning

	def clear(self, stateMachine: Isa88StateMachine):
		pass # Clear cannot be fired from Stopping -> Do nothing except maybe giving a warning

	def executeActionAndComplete(self, stateMachine: Isa88StateMachine):
		actionToRun = stateMachine.getStateActionManager().getAction(ActiveStateName.Stopping)
		super.executeAction(actionToRun)

		# Make sure the current state is still Stopping before going to Stopped (could have been changed in the mean time).
		if (isinstance(stateMachine.getState(), StoppingState)):
			stateMachine.setStateAndRunAction(StoppedState())

