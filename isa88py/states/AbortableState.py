from isa88py.states.State import State
from typing import TYPE_CHECKING

if TYPE_CHECKING:
	from isa88py.statemachine.Isa88StateMachine import Isa88StateMachine

class AbortableState(State):
	"""
	Abstract super class of all ISA-88 states that can just be aborted but not stopped (i.e. Stopping, Clearing, Stopped).
	"""
	
	def abort(self, stateMachine: 'Isa88StateMachine'):
		from isa88py.states.impl.AbortingState import AbortingState
		coro = stateMachine.setStateAndRunAction(AbortingState())

	
	def stop(self, stateMachine: 'Isa88StateMachine'):
		pass