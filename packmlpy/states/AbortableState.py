from packmlpy.states.State import State
import asyncio
from typing import TYPE_CHECKING

if TYPE_CHECKING:
	from packmlpy.statemachine.PackMlStateMachine import PackMlStateMachine

class AbortableState(State):
	"""
	Abstract super class of all ISA-88 states that can just be aborted but not stopped (i.e. Stopping, Clearing, Stopped).
	"""
	
	def abort(self, stateMachine: 'PackMlStateMachine'):
		from packmlpy.states.impl.AbortingState import AbortingState
		stateMachine.setStateAndRunAction(AbortingState())

	def stop(self, stateMachine: 'PackMlStateMachine'):
		pass