from IState import IState
from statemachine.Isa88StateMachine import Isa88StateMachine
from StateAction import StateAction

class State(IState):

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