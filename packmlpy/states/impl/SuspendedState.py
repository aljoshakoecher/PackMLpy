from packmlpy.states.StoppableState import StoppableState
from packmlpy.states.impl.UnsuspendingState import UnsuspendingState
from typing import TYPE_CHECKING
import asyncio

if TYPE_CHECKING:
	from packmlpy.statemachine.PackMlStateMachine import PackMlStateMachine

class SuspendedState (StoppableState):
	"""
	The SuspendedState denotes a waiting state that is typically entered when external conditions prevent a machine from continuing execution. An
	unsuspend command has to be issued in order to bring the state machine back to the ExecuteState.
	"""

	def start(self, stateMachine: 'PackMlStateMachine'):
		pass # Start cannot be fired from Suspended -> Do nothing except maybe giving a warning
	def hold(self, stateMachine: 'PackMlStateMachine'):
		pass # Hold cannot be fired from Suspended -> Do nothing except maybe giving a warning
	def unhold(self, stateMachine: 'PackMlStateMachine'):
		pass # Unhold cannot be fired from Suspended -> Do nothing except maybe giving a warning
	def suspend(self, stateMachine: 'PackMlStateMachine'):
		pass # Suspend cannot be fired from Suspended -> Do nothing except maybe giving a warning
	def unsuspend(self, stateMachine: 'PackMlStateMachine'):
		stateMachine.setStateAndRunAction(UnsuspendingState())
	def reset(self, stateMachine: 'PackMlStateMachine'):
		pass # Reset cannot be fired from Suspended -> Do nothing except maybe giving a warning
	def clear(self, stateMachine: 'PackMlStateMachine'):
		pass # Clear cannot be fired from Suspended -> Do nothing except maybe giving a warning

