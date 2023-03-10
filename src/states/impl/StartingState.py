from statemachine.Isa88StateMachine import Isa88StateMachine
from states.ActiveStateName import ActiveStateName
from states.StoppableState import StoppableState
from states.impl import ExecuteState

class StartingState (StoppableState):
	"""
	The StartingState denotes a transitive state that should make a machine ready for producing. After having completed a startup procedure,
	the state machine will change to the ExecuteState.
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
		actionToRun = stateMachine.getStateActionManager().getAction(ActiveStateName.Starting)
		super.executeAction(actionToRun)
		
		# Make sure the current state is still Starting before going to Execute (could have been changed in the mean time).
		if (isinstance(stateMachine.getState(), StartingState)):
			stateMachine.setStateAndRunAction(ExecuteState())

