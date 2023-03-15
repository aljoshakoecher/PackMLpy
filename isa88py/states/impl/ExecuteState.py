from isa88py.statemachine.Isa88StateMachine import Isa88StateMachine
from isa88py.states.ActiveStateName import ActiveStateName
from isa88py.states.StoppableState import StoppableState
from isa88py.states.impl.HoldingState import HoldingState
from isa88py.states.impl.SuspendingState import SuspendingState
from isa88py.states.impl.CompletingState import CompletingState

class ExecuteState (StoppableState):
	"""
	The ExecuteState denotes a transitive state that contains the main execution actions that are responsible for actual production. After
	completing execution, the state machine will change to the CompletingState.
	"""

	def start(self, stateMachine: Isa88StateMachine):
		pass # Start cannot be fired from Execute -> Do nothing except maybe giving a warning

	def hold(self, stateMachine: Isa88StateMachine):
		coro = stateMachine.setStateAndRunAction(HoldingState())

	def unhold(self, stateMachine: Isa88StateMachine):
		pass # Unhold cannot be fired from Execute -> Do nothing except maybe giving a warning

	def suspend(self, stateMachine: Isa88StateMachine):
		coro = stateMachine.setStateAndRunAction(SuspendingState())

	def unsuspend(self, stateMachine: Isa88StateMachine):
		pass # Unsuspend cannot be fired from Execute -> Do nothing except maybe giving a warning

	def reset(self, stateMachine: Isa88StateMachine):
		pass # Reset cannot be fired from Execute -> Do nothing except maybe giving a warning

	def clear(self, stateMachine: Isa88StateMachine):
		pass # Clear cannot be fired from Execute -> Do nothing except maybe giving a warning

	async def executeActionAndComplete(self, stateMachine: Isa88StateMachine):
		actionToRun = stateMachine.getStateActionManager().getAction(ActiveStateName.Execute)
		self.executeAction(actionToRun)
		
		# Make sure the current state is still Execute before going to Completing (could have been changed in the mean time).
		if (isinstance(stateMachine.getState(), ExecuteState)):
			coro = stateMachine.setStateAndRunAction(CompletingState())
