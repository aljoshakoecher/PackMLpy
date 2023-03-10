from statemachine.Isa88StateMachine import Isa88StateMachine
from states.IState import IState


class AbortableState(IState):
	"""
	Abstract super class of all ISA-88 states that can just be aborted but not stopped (i.e. Stopping, Clearing, Stopped).
	"""
	
	def abort(self, stateMachine: Isa88StateMachine):
		newAborting = AbortingState()
		stateMachine.setStateAndRunAction(newAborting)

	
	def stop(self, stateMachine: Isa88StateMachine):
		pass