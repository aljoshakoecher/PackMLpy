from statemachine.Isa88StateMachine import Isa88StateMachine
from states.ActiveStateName import ActiveStateName
from states.StoppableState import StoppableState
from states.impl.HeldState import HeldState

class HoldingState (StoppableState):
	"""
	The HoldingState denotes a transitive state that brings a machine to a stop when internal conditions prevent further production. After
	having completed holding procedure, the state machine will change to the HeldState.
	"""	

	def start(self, stateMachine: Isa88StateMachine):
		pass # Start cannot be fired from Holding -> Do nothing except maybe giving a warning

	def hold(self, stateMachine: Isa88StateMachine):
		pass # Hold cannot be fired from Holding -> Do nothing except maybe giving a warning

	def unhold(self, stateMachine: Isa88StateMachine):
		pass # Unhold cannot be fired from Holding -> Do nothing except maybe giving a warning

	def suspend(self, stateMachine: Isa88StateMachine):
		pass # Start cannot be fired from Holding -> Do nothing except maybe giving a warning

	def unsuspend(self, stateMachine: Isa88StateMachine):
		pass # Unsuspend cannot be fired from Holding -> Do nothing except maybe giving a warning

	def reset(self, stateMachine: Isa88StateMachine):
		pass # Reset cannot be fired from Holding -> Do nothing except maybe giving a warning

	def clear(self, stateMachine: Isa88StateMachine):
		pass # Clear cannot be fired from Holding -> Do nothing except maybe giving a warning

	async def executeActionAndComplete(self, stateMachine: Isa88StateMachine):
		actionToRun = stateMachine.getStateActionManager().getAction(ActiveStateName.Holding)
		self.executeAction(actionToRun)
		
		# Make sure the current state is still Holding before going to Held (could have been changed in the mean time).
		if (isinstance(stateMachine.getState(), HoldingState)):
			coro = stateMachine.setStateAndRunAction(HeldState())

