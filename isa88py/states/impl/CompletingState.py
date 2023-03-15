from isa88py.statemachine.Isa88StateMachine import Isa88StateMachine
from isa88py.states.ActiveStateName import ActiveStateName
from isa88py.states.StoppableState import StoppableState
from isa88py.states.impl.CompleteState import CompleteState

class CompletingState (StoppableState):
	"""
	The CompletingState denotes a transitive state that can be used to bring production to an end (e.g. when the specified number of products
	have been produced). After the completing action has been executed, the state machine will change to the ExecuteState.
	"""

	def start(self, stateMachine: Isa88StateMachine):
		pass # Start cannot be fired from Completing -> Do nothing except maybe giving a warning

	def hold(self, stateMachine: Isa88StateMachine):
		pass # Hold cannot be fired from Completing -> Do nothing except maybe giving a warning

	def unhold(self, stateMachine: Isa88StateMachine):
		pass # Unhold cannot be fired from Completing -> Do nothing except maybe giving a warning

	def suspend(self, stateMachine: Isa88StateMachine):
		pass # Start cannot be fired from Completing -> Do nothing except maybe giving a warning

	def unsuspend(self, stateMachine: Isa88StateMachine):
		pass # Unsuspend cannot be fired from Completing -> Do nothing except maybe giving a warning

	def reset(self, stateMachine: Isa88StateMachine):
		pass # Reset cannot be fired from Completing -> Do nothing except maybe giving a warning

	def clear(self, stateMachine: Isa88StateMachine):
		pass # Clear cannot be fired from Completing -> Do nothing except maybe giving a warning

	async def executeActionAndComplete(self, stateMachine: Isa88StateMachine):
		actionToRun = stateMachine.getStateActionManager().getAction(ActiveStateName.Completing)
		self.executeAction(actionToRun)

		# Make sure the current state is still Completing before going to Complete (could have been changed in the mean time).
		if (isinstance(stateMachine.getState(), CompletingState)):
			coro = stateMachine.setStateAndRunAction(CompleteState())

