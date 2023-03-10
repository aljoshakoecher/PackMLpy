from statemachine.Isa88StateMachine import Isa88StateMachine
from states.State import State
from states.ActiveStateName import ActiveStateName
from states.impl.AbortedState import AbortedState

class AbortingState(State):
	"""
	* The AbortingState denotes a transitive state that should bring a machine to a sudden halt. Damages on products have to be expected. From
	* Aborting, no commands are accepted. After executing its action, the state machine will change to the AbortedState.
	"""

	def start(self, stateMachine: Isa88StateMachine):
		pass # Start cannot be fired from Aborting -> Do nothing except maybe giving a warning

	def hold(self, stateMachine: Isa88StateMachine):
		pass # Hold cannot be fired from Aborting -> Do nothing except maybe giving a warning

	def unhold(self, stateMachine: Isa88StateMachine):
		pass # Unhold cannot be fired from Aborting -> Do nothing except maybe giving a warning

	def suspend(self, stateMachine: Isa88StateMachine):
		pass # Suspend cannot be fired from Aborting -> Do nothing except maybe giving a warning

	def unsuspend(self, stateMachine: Isa88StateMachine):
		pass # Unsuspend cannot be fired from Aborting -> Do nothing except maybe giving a warning

	def reset(self, stateMachine: Isa88StateMachine):
		pass # Reset cannot be fired from Aborting -> Do nothing except maybe giving a warning

	def stop(self, stateMachine: Isa88StateMachine):
		pass # Stop cannot be fired from Aborting -> Do nothing except maybe giving a warning

	def abort(self, stateMachine: Isa88StateMachine):
		pass # Abort cannot be fired from Aborting -> Do nothing except maybe giving a warning

	def clear(self, stateMachine: Isa88StateMachine):
		pass # Clear cannot be fired from Aborting -> Do nothing except maybe giving a warning

	def executeActionAndComplete(self, stateMachine: Isa88StateMachine):
		actionToRun = stateMachine.getStateActionManager().getAction(ActiveStateName.Aborting)
		super.executeAction(actionToRun)

		# Make sure the current state is still Aborting before going to Aborted (could have been changed in the mean time).
		if (isinstance(stateMachine.getState(), AbortingState)):
			stateMachine.setStateAndRunAction(AbortedState())
