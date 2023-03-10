from statemachine.Isa88StateMachine import Isa88StateMachine
from states.ActiveStateName import ActiveStateName
from states.StoppableState import StoppableState
from states.impl import IdleState

class ResettingState (StoppableState):
	"""
	The ResettingState denotes a transitive state that brings a machine back to its IdleState after it had previously been stopped or
	aborted.
	"""

	def start(self, stateMachine: Isa88StateMachine):
		pass # Start cannot be fired from Starting -> Do nothing except maybe giving a warning

	def hold(self, stateMachine: Isa88StateMachine):
		pass # Hold cannot be fired from Starting -> Do nothing except maybe giving a warning

	def unhold(self, stateMachine: Isa88StateMachine):
		pass # Unhold cannot be fired from Starting -> Do nothing except maybe giving a warning

	def suspend(self, stateMachine: Isa88StateMachine):
		pass # Start cannot be fired from Starting -> Do nothing except maybe giving a warning

	def unsuspend(self, stateMachine: Isa88StateMachine):
		pass # Unsuspend cannot be fired from Starting -> Do nothing except maybe giving a warning

	def reset(self, stateMachine: Isa88StateMachine):
		pass # Reset cannot be fired from Starting -> Do nothing except maybe giving a warning

	def clear(self, stateMachine: Isa88StateMachine):
		pass # Clear cannot be fired from Starting -> Do nothing except maybe giving a warning

	def executeActionAndComplete(self, stateMachine: Isa88StateMachine):
		actionToRun = stateMachine.getStateActionManager().getAction(ActiveStateName.Resetting)
		super.executeAction(actionToRun)

		# Make sure the current state is still Resetting before going to Idle (could have been changed in the mean time).
		if (isinstance(stateMachine.getState(), ResettingState)):
			stateMachine.setStateAndRunAction(IdleState())
