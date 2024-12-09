from packmlpy.states.StoppableState import StoppableState
from typing import TYPE_CHECKING
import asyncio

if TYPE_CHECKING:
	from packmlpy.statemachine.PackMlStateMachine import PackMlStateMachine

class IdleState (StoppableState):
	"""
	The IdleState denotes a waiting state that can be seen as the initial state of a machine that is ready to start production. A start command
	has to be issued in order to start production and bring the state machine to the StartingState.
	"""
	
	from packmlpy.states.impl.StartingState import StartingState

	def start(self, stateMachine: 'PackMlStateMachine'):
		stateMachine.setStateAndRunAction(self.StartingState())

	def hold(self, stateMachine: 'PackMlStateMachine'):
		pass # Hold cannot be fired from Idle -> Do nothing except maybe giving a warning

	def unhold(self, stateMachine: 'PackMlStateMachine'):
		pass # Unhold cannot be fired from Idle -> Do nothing except maybe giving a warning

	def suspend(self, stateMachine: 'PackMlStateMachine'):
		pass # Suspend cannot be fired from Idle -> Do nothing except maybe giving a warning

	def unsuspend(self, stateMachine: 'PackMlStateMachine'):
		pass # Unsuspend cannot be fired from Idle -> Do nothing except maybe giving a warning

	def reset(self, stateMachine: 'PackMlStateMachine'):
		pass # Reset cannot be fired from Idle -> Do nothing except maybe giving a warning

	def clear(self, stateMachine: 'PackMlStateMachine'):
		pass # Clear cannot be fired from Idle -> Do nothing except maybe giving a warning

