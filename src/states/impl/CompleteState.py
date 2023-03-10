from statemachine.Isa88StateMachine import Isa88StateMachine
from states.StoppableState import StoppableState
from states.impl.ResettingState import ResettingState

class CompleteState (StoppableState):
	"""
	The CompleteState denotes a state in which the machine has completed production. In order to start the next order, a reset command is
	necessary to transition to IdleState.
	"""

	def start(self, stateMachine: Isa88StateMachine):
		pass # Start cannot be fired from Complete -> Do nothing except maybe giving a warning

	def hold(self, stateMachine: Isa88StateMachine):
		pass # Hold cannot be fired from Complete -> Do nothing except maybe giving a warning

	def unhold(self, stateMachine: Isa88StateMachine):
		pass # Unhold cannot be fired from Complete -> Do nothing except maybe giving a warning

	def suspend(self, stateMachine: Isa88StateMachine):
		pass # Suspend cannot be fired from Complete -> Do nothing except maybe giving a warning

	def unsuspend(self, stateMachine: Isa88StateMachine):
		pass # Unsuspend cannot be fired from Complete -> Do nothing except maybe giving a warning

	def reset(self, stateMachine: Isa88StateMachine):
		stateMachine.setStateAndRunAction(ResettingState())

	def clear(self, stateMachine: Isa88StateMachine):
		pass # Clear cannot be fired from Clearing -> Do nothing except maybe giving a warning
