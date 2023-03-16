from isa88py.states.StoppableState import StoppableState
from typing import TYPE_CHECKING

if TYPE_CHECKING:
	from isa88py.statemachine.Isa88StateMachine import Isa88StateMachine

class IdleState (StoppableState):
	"""
	The IdleState denotes a waiting state that can be seen as the initial state of a machine that is ready to start production. A start command
	has to be issued in order to start production and bring the state machine to the StartingState.
	"""
	
	from isa88py.states.impl.StartingState import StartingState

	def start(self, stateMachine: 'Isa88StateMachine'):
		coro = stateMachine.setStateAndRunAction(self.StartingState())

	def hold(self, stateMachine: 'Isa88StateMachine'):
		pass # Hold cannot be fired from Idle -> Do nothing except maybe giving a warning

	def unhold(self, stateMachine: 'Isa88StateMachine'):
		pass # Unhold cannot be fired from Idle -> Do nothing except maybe giving a warning

	def suspend(self, stateMachine: 'Isa88StateMachine'):
		pass # Suspend cannot be fired from Idle -> Do nothing except maybe giving a warning

	def unsuspend(self, stateMachine: 'Isa88StateMachine'):
		pass # Unsuspend cannot be fired from Idle -> Do nothing except maybe giving a warning

	def reset(self, stateMachine: 'Isa88StateMachine'):
		pass # Reset cannot be fired from Idle -> Do nothing except maybe giving a warning

	def clear(self, stateMachine: 'Isa88StateMachine'):
		pass # Clear cannot be fired from Idle -> Do nothing except maybe giving a warning

