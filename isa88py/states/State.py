from abc import abstractmethod
from typing import TYPE_CHECKING

if TYPE_CHECKING:
	from isa88py.statemachine.Isa88StateMachine import Isa88StateMachine
	from isa88py.states.StateAction import StateAction

class State:

	async def executeActionAndComplete(self, stateMachine: 'Isa88StateMachine'):
		"""
		Execute an action, complete this state and transition to the next state 
		stateMachine: The current state machine instance
		"""
		# Default implementation: Do nothing
		# Acting states have to override this method in order to automatically complete
	
	
	def executeAction(self, action: 'StateAction'):
		"""
		Default of a simple runAction implementation. Could be overriden if e.g. an action has to run in a separate thread
		action: {@link IStateAction} that is going to be executed
		"""
		action.execute()

	@abstractmethod
	def start(self, stateMachine: 'Isa88StateMachine'):
		""" The start command does only have an effect in IdleState. With this command, the state machine will change to the ExecuteState
			stateMachine: A reference to the current Isa88StateMachine instance """

	
	@abstractmethod
	def hold(self, stateMachine: 'Isa88StateMachine'):
		"""
		The hold command is used when interal reasons of a machine should bring it to an halt. Such reasons could be e.g. necessary refill of material.
		With this command, the state machine will transition to a HoldingState and eventually come to a full HeldState.
		stateMachine: A reference to the current Isa88StateMachine instance 
		"""

	
	@abstractmethod
	def unhold(self, stateMachine: 'Isa88StateMachine'):
		"""
		The unhold command brings the machine into an UnholdingState that eventually leads back to the ExecuteState. The hold command
		should be used when the internal reasons that brought a machine into a HeldState have been cleared.
		stateMachine: A reference to the current Isa88StateMachine instance 
		"""

	
	@abstractmethod
	def suspend(self, stateMachine: 'Isa88StateMachine'):
		"""
		The suspend command is used when extenal reasons of a machine should bring it to an halt. Such reasons could be e.g. waiting for following
		machines to accept a workpiece. With this command, the state machine will transition to a SuspendingState and eventually come to a full
		SuspendedState.
		stateMachine: A reference to the current Isa88StateMachine instance 
		"""
		
	
	@abstractmethod
	def unsuspend(self, stateMachine: 'Isa88StateMachine'):
		"""
		The unsuspend command brings the machine into an UnsuspendingState that eventually leads back to the ExecuteState. The
		unsuspend command should be used when the external reasons that brought a machine into a SuspendedState have been cleared.
		stateMachine: A reference to the current Isa88StateMachine instance 
		"""
	
	@abstractmethod
	def reset(self, stateMachine: 'Isa88StateMachine'):
		"""
		The reset command brings the machine into a ResettingState that eventually leads back to the IdleState. The reset command can
		be used when the machine has been brought to a sudden halt (e.g. with stop or abort command)
		stateMachine: A reference to the current Isa88StateMachine instance 
		"""
		
	@abstractmethod
	def stop(self, stateMachine: 'Isa88StateMachine'):
		"""
		The stop command can be triggered by an external system such as an MES. Stop brings the state machine to a StoppingState and from there
		to a StoppedState. The currently produced product should not be destroyed and production can continue after the machine has been reset.
		stateMachine A reference to the current Isa88StateMachine instance 
		"""

	
	@abstractmethod
	def abort(self, stateMachine: 'Isa88StateMachine'):
		"""
		The abort command can be triggered by an external system such as an MES. Abort brings the state machine to a sudden stop by transitioning to
		the AbortingState and eventually to the AbortedState. The machine is switched off, the currently produced product might have to
		be destroyed and production of it can not be continued.
		stateMachine A reference to the current Isa88StateMachine instance 
		"""

	@abstractmethod
	def clear(self, stateMachine: 'Isa88StateMachine'):
		"""
		After a machine has been brought to the AbortedState, a clear command can be used to bring it to a ClearingState to e.g. remove
		destroyed products. From the ClearingState, the machine will come to the StoppedState from which it then can be reset.
		stateMachine A reference to the current Isa88StateMachine instance 
		"""