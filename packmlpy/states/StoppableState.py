from packmlpy.states.AbortableState import AbortableState
import asyncio
from typing import TYPE_CHECKING

if TYPE_CHECKING:
	from packmlpy.statemachine.PackMlStateMachine import PackMlStateMachine

class StoppableState(AbortableState):
	""" 
	Abstract super class for all states that can be stopped and aborted
	"""
	from packmlpy.states.impl.StoppingState import StoppingState
	
	def stop(self, stateMachine: 'PackMlStateMachine'):
		""" 
		Execute the stop-method that the developer implemented (has that to be executed in another thread?)
		Inside of the thread: Update the state in the ontology to now be "Stopping"
		When the thread is done: Update the state in the ontology to now be "Stopped" (might have to be done in the other thread as well)
		"""
		stateMachine.setStateAndRunAction(self.StoppingState())