from isa88py.states.StoppableState import StoppableState
from isa88py.states.impl.UnholdingState import UnholdingState
from typing import TYPE_CHECKING

if TYPE_CHECKING:
	from isa88py.statemachine.Isa88StateMachine import Isa88StateMachine

class HeldState (StoppableState):
	"""
	The HeldState denotes a waiting state that is typically entered when internal conditions prevent a machine from continuing execution. An
	unhold command has to be issued in order to bring the state machine to the UnholdingState.
	"""

	def start(self, stateMachine: 'Isa88StateMachine'):
		pass # Start cannot be fired from Held -> Do nothing except maybe giving a warning

	def hold(self, stateMachine: 'Isa88StateMachine'):
		pass # Hold cannot be fired from Held -> Do nothing except maybe giving a warning

	def unhold(self, stateMachine: 'Isa88StateMachine'):
		coro = stateMachine.setStateAndRunAction(UnholdingState())

	def suspend(self, stateMachine: 'Isa88StateMachine'):
		pass # Suspend cannot be fired from Held -> Do nothing except maybe giving a warning

	def unsuspend(self, stateMachine: 'Isa88StateMachine'):
		pass # Unsuspend cannot be fired from Held -> Do nothing except maybe giving a warning

	def reset(self, stateMachine: 'Isa88StateMachine'):
		pass # Reset cannot be fired from Held -> Do nothing except maybe giving a warning

	def clear(self, stateMachine: 'Isa88StateMachine'):
		pass # Clear cannot be fired from Held -> Do nothing except maybe giving a warning

