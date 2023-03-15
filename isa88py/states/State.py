from isa88py.states.IState import IState

class State(IState):
	from isa88py.statemachine.Isa88StateMachine import Isa88StateMachine
	from isa88py.states.StateAction import StateAction

	async def executeActionAndComplete(self, stateMachine: Isa88StateMachine):
		"""
		Execute an action, complete this state and transition to the next state 
		stateMachine: The current state machine instance
		"""
		# Default implementation: Do nothing
		# Acting states have to override this method in order to automatically complete
	
	
	def executeAction(self, action: StateAction):
		"""
		Default of a simple runAction implementation. Could be overriden if e.g. an action has to run in a separate thread
		action: {@link IStateAction} that is going to be executed
		"""
		action.execute()