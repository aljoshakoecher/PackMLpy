from isa88py.statemachine.Isa88StateMachine import Isa88StateMachine
from isa88py.states.impl.StoppingState import StoppingState
from AbortableState import AbortableState

class StoppableState(AbortableState):
	""" 
	Abstract super class for all states that can be stopped and aborted
	"""
	
	def stop(self, stateMachine: Isa88StateMachine):
		""" 
		Execute the stop-method that the developer implemented (has that to be executed in another thread?)
		Inside of the thread: Update the state in the ontology to now be "Stopping"
		When the thread is done: Update the state in the ontology to now be "Stopped" (might have to be done in the other thread as well)
		"""
		coro = stateMachine.setStateAndRunAction(StoppingState())