from statemachine.Isa88StateMachine import Isa88StateMachine
from states.AbortableState import AbortableState
from states.impl.ResettingState import ResettingState

class StoppedState (AbortableState):
	"""
	The StoppedState denotes a state in which the machine is powered and stationary. Communications with other systems are functioning. A
	reset-command will cause a transition from StoppedState to ResettingState.
	"""

	def start(self, stateMachine: Isa88StateMachine):
		pass # Start cannot be fired from Stopped -> Do nothing except maybe giving a warning

	def hold(self, stateMachine: Isa88StateMachine):
		pass # Hold cannot be fired from Stopped -> Do nothing except maybe giving a warning

	def unhold(self, stateMachine: Isa88StateMachine):
		pass # Unhold cannot be fired from Stopped -> Do nothing except maybe giving a warning

	def suspend(self, stateMachine: Isa88StateMachine):
		pass # Suspend cannot be fired from Stopped -> Do nothing except maybe giving a warning

	def unsuspend(self, stateMachine: Isa88StateMachine):
		pass # Unsuspend cannot be fired from Stopped -> Do nothing except maybe giving a warning

	def reset(self, stateMachine: Isa88StateMachine):
		coro = stateMachine.setStateAndRunAction(ResettingState())

	def clear(self, stateMachine: Isa88StateMachine):
		pass # Clear cannot be fired from Stopped -> Do nothing except maybe giving a warning

