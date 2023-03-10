
from states.State import State
from states.impl.ClearingState import ClearingState
from statemachine.Isa88StateMachine import Isa88StateMachine

class AbortedState(State):
	"""
	The AbortedState denotes a state in which the machine has been brought to a sudden halt. A
	clear-command is necessary to transition to StoppedState.
	"""

	def start(self, stateMachine: Isa88StateMachine):
		pass # Start cannot be fired from Aborted -> Do nothing except maybe giving a warning


	def hold(self, stateMachine: Isa88StateMachine):
		pass # Hold cannot be fired from Aborted -> Do nothing except maybe giving a warning


	def unhold(self, stateMachine: Isa88StateMachine):
		pass # Unhold cannot be fired from Aborted -> Do nothing except maybe giving a warning


	def suspend(self, stateMachine: Isa88StateMachine):
		pass # Suspend cannot be fired from Aborted -> Do nothing except maybe giving a warning


	def unsuspend(self, stateMachine: Isa88StateMachine):
		pass # Unsuspend cannot be fired from Aborted -> Do nothing except maybe giving a warning


	def reset(self, stateMachine: Isa88StateMachine):
		pass # Reset cannot be fired from Aborted -> Do nothing except maybe giving a warning


	def stop(self, stateMachine: Isa88StateMachine):
		pass # Stop cannot be fired from Aborted -> Do nothing except maybe giving a warning


	def abort(self, stateMachine: Isa88StateMachine):
		pass # Abort cannot be fired from Aborted -> Do nothing except maybe giving a warning


	def clear(self, stateMachine: Isa88StateMachine):
		coro = stateMachine.setStateAndRunAction(ClearingState())
