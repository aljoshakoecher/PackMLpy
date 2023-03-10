from statemachine.Isa88StateMachine import Isa88StateMachine
from states.ActiveStateName import ActiveStateName
from states.StoppableState import StoppableState
from states.impl.SuspendedState import SuspendedState

class SuspendingState (StoppableState):
	"""
	The SuspendingState denotes a transitive state that is entered on a suspend command. This command is typically issued when external
	conditions prevent a machine from continuing execution (e.g. waiting for downstream machines). After executing the action the state machine will
	transition to the SuspendedState
	"""

	def start(self, stateMachine: Isa88StateMachine):
		pass # Start cannot be fired from Suspending -> Do nothing except maybe giving a warning

	def hold(self, stateMachine: Isa88StateMachine):
		pass # Hold cannot be fired from Suspending -> Do nothing except maybe giving a warning

	def unhold(self, stateMachine: Isa88StateMachine):
		pass # Unhold cannot be fired from Suspending -> Do nothing except maybe giving a warning

	def suspend(self, stateMachine: Isa88StateMachine):
		pass # Start cannot be fired from Suspending -> Do nothing except maybe giving a warning

	def unsuspend(self, stateMachine: Isa88StateMachine):
		pass # Unsuspend cannot be fired from Suspending -> Do nothing except maybe giving a warning

	def reset(self, stateMachine: Isa88StateMachine):
		pass # Reset cannot be fired from Suspending -> Do nothing except maybe giving a warning

	def clear(self, stateMachine: Isa88StateMachine):
		pass # Clear cannot be fired from Suspending -> Do nothing except maybe giving a warning

	def executeActionAndComplete(self, stateMachine: Isa88StateMachine):
		actionToRun = stateMachine.getStateActionManager().getAction(ActiveStateName.Suspending)
		super.executeAction(actionToRun)

		# Make sure the current state is still execute before going to Completing (could have been changed in the mean time).
		if (isinstance(stateMachine.getState(), SuspendingState)):
			stateMachine.setStateAndRunAction(SuspendedState())

