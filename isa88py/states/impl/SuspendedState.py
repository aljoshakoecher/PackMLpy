from isa88py.states.StoppableState import StoppableState
from isa88py.states.impl.UnsuspendingState import UnsuspendingState
from typing import TYPE_CHECKING

if TYPE_CHECKING:
	from isa88py.statemachine.Isa88StateMachine import Isa88StateMachine

class SuspendedState (StoppableState):
	"""
	The SuspendedState denotes a waiting state that is typically entered when external conditions prevent a machine from continuing execution. An
	unsuspend command has to be issued in order to bring the state machine back to the ExecuteState.
	"""

	def start(self, stateMachine: 'Isa88StateMachine'):
		pass # Start cannot be fired from Suspended -> Do nothing except maybe giving a warning
	def hold(self, stateMachine: 'Isa88StateMachine'):
		pass # Hold cannot be fired from Suspended -> Do nothing except maybe giving a warning
	def unhold(self, stateMachine: 'Isa88StateMachine'):
		pass # Unhold cannot be fired from Suspended -> Do nothing except maybe giving a warning
	def suspend(self, stateMachine: 'Isa88StateMachine'):
		pass # Suspend cannot be fired from Suspended -> Do nothing except maybe giving a warning
	def unsuspend(self, stateMachine: 'Isa88StateMachine'):
		coro = stateMachine.setStateAndRunAction(UnsuspendingState())
	def reset(self, stateMachine: 'Isa88StateMachine'):
		pass # Reset cannot be fired from Suspended -> Do nothing except maybe giving a warning
	def clear(self, stateMachine: 'Isa88StateMachine'):
		pass # Clear cannot be fired from Suspended -> Do nothing except maybe giving a warning

