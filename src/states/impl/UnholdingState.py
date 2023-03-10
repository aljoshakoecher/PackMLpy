from statemachine.Isa88StateMachine import Isa88StateMachine
from states.ActiveStateName import ActiveStateName
from states.StoppableState import StoppableState
from states.impl.ExecuteState import ExecuteState

class UnholdingState (StoppableState):
	"""
	The UnholdingState denotes a transitive state that is entered after the machine has been suspended and an unhold command has been issued. After executing the action the state
	machine will transition back to the ExecuteState.
	"""

	def start(self, stateMachine: Isa88StateMachine):
		pass # Start cannot be fired from Unholding -> Do nothing except maybe giving a warning

	def hold(self, stateMachine: Isa88StateMachine):
		pass # Hold cannot be fired from Unholding -> Do nothing except maybe giving a warning

	def unhold(self, stateMachine: Isa88StateMachine):
		pass # Unhold cannot be fired from Unholding -> Do nothing except maybe giving a warning

	def suspend(self, stateMachine: Isa88StateMachine):
		pass # Start cannot be fired from Unholding -> Do nothing except maybe giving a warning

	def unsuspend(self, stateMachine: Isa88StateMachine):
		pass # Unsuspend cannot be fired from Unholding -> Do nothing except maybe giving a warning

	def reset(self, stateMachine: Isa88StateMachine):
		pass # Reset cannot be fired from Unholding -> Do nothing except maybe giving a warning

	def clear(self, stateMachine: Isa88StateMachine):
		pass # Clear cannot be fired from Unholding -> Do nothing except maybe giving a warning

	def executeActionAndComplete(self, stateMachine: Isa88StateMachine):
		actionToRun = stateMachine.getStateActionManager().getAction(ActiveStateName.Unholding)
		super.executeAction(actionToRun)

		# Make sure the current state is still Unholding before going to Execute (could have been changed in the mean time).
		if (isinstance(stateMachine.getState(), UnholdingState)):
			stateMachine.setStateAndRunAction(ExecuteState())

