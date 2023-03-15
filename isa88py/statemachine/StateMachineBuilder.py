from isa88py.statemachine.Isa88StateMachine import Isa88StateMachine
from isa88py.states.State import State
from isa88py.states.StateAction import StateAction
from isa88py.states.ActiveStateName import ActiveStateName
from isa88py.states.impl.IdleState import IdleState

class StateMachineBuilder:
	"""
	Builder class that is in charge of constructing a properly set up Isa88StateMachine
	"""

	stateMachine: Isa88StateMachine

	def __init__(self):
		self.stateMachine = Isa88StateMachine(IdleState())

	
	def withInitialState(self, initialState: State) :  
		""" 
		* Constructs a state machine with a special initial state
		* 
		* initialState The state that is to be the initial state of the state machine
		* return: This StateMachineBuilder instance to use for further construction operations
		"""
		self.stateMachine.setState(initialState)
		return self
	

	
	"""
	 * Adds an IStateAction to a certain State. The IStateAction will be executed in that given State.
	 * 
	 * @param action An instance of IStateAction that is executed in StartingState
	 * @param stateName Name of the State that the action will be executed in.
	 * @return This StateMachineBuilder instance to use for further construction operations
	"""
	def withAction(self, action: StateAction, stateName: ActiveStateName) :
		match stateName:
			case ActiveStateName.Starting:
				self.stateMachine.getStateActionManager().setAction(action, ActiveStateName.Starting)
			case ActiveStateName.Execute:
				self.stateMachine.getStateActionManager().setAction(action, ActiveStateName.Execute)
			case ActiveStateName.Completing:
				self.stateMachine.getStateActionManager().setAction(action, ActiveStateName.Completing)
			case ActiveStateName.Holding:
				self.stateMachine.getStateActionManager().setAction(action, ActiveStateName.Holding)
			case ActiveStateName.Unholding:
				self.stateMachine.getStateActionManager().setAction(action, ActiveStateName.Unholding)
			case ActiveStateName.Suspending:
				self.stateMachine.getStateActionManager().setAction(action, ActiveStateName.Suspending)
			case ActiveStateName.Unsuspending:
				self.stateMachine.getStateActionManager().setAction(action, ActiveStateName.Unsuspending)
			case ActiveStateName.Stopping:
				self.stateMachine.getStateActionManager().setAction(action, ActiveStateName.Stopping)
			case ActiveStateName.Clearing:
				self.stateMachine.getStateActionManager().setAction(action, ActiveStateName.Clearing)
			case ActiveStateName.Aborting:
				self.stateMachine.getStateActionManager().setAction(action, ActiveStateName.Aborting)
			case ActiveStateName.Resetting:
				self.stateMachine.getStateActionManager().setAction(action, ActiveStateName.Resetting)
		
		return self
	

	"""
	 * Adds an IStateAction that is to be executed in StartingState. Alias for withAction(action, ActiveStateName.Starting).
	 * 
	 * @param action An instance of IStateAction that is executed in StartingState
	 * @return This StateMachineBuilder instance to use for further construction operations
	"""
	def withActionInStarting(self, action: StateAction) :
		self.withAction(action, ActiveStateName.Starting)
		return self
	

	"""
	 * Adds an IStateAction that is to be executed in ExecuteState. Alias for withAction(action, ActiveStateName.Execute).
	 * 
	 * @param action An instance of IStateAction that is executed in ExecuteState
	 * @return This StateMachineBuilder instance to use for further construction operations
	"""
	def withActionInExecute(self, action: StateAction) :
		self.withAction(action, ActiveStateName.Execute)
		return self
	

	"""
	 * Adds an IStateAction that is to be executed in CompletingState. Alias for withAction(action, ActiveStateName.Completing).
	 * 
	 * @param action An instance of IStateAction that is executed in CompletingState
	 * @return This StateMachineBuilder instance to use for further construction operations
	"""
	def withActionInCompleting(self, action: StateAction) :
		self.withAction(action, ActiveStateName.Completing)
		return self
	

	"""
	 * Adds an IStateAction that is to be executed in SuspendingState. Alias for withAction(action, ActiveStateName.Suspending).
	 * 
	 * @param action An instance of IStateAction that is executed in SuspendingState
	 * @return This StateMachineBuilder instance to use for further construction operations
	"""
	def withActionInSuspending(self, action: StateAction) :
		self.withAction(action, ActiveStateName.Suspending)
		return self
	

	"""
	 * Adds an IStateAction that is to be executed in UnsuspendingState. Alias for withAction(action, ActiveStateName.Unsuspending).
	 * 
	 * @param action An instance of IStateAction that is executed in UnsuspendingState
	 * @return This StateMachineBuilder instance to use for further construction operations
	"""
	def withActionInUnsuspending(self, action: StateAction) :
		self.withAction(action, ActiveStateName.Unsuspending)
		return self
	

	"""
	 * Adds an IStateAction that is to be executed in HoldingState. Alias for withAction(action, ActiveStateName.Holding).
	 * 
	 * @param action An instance of IStateAction that is executed in HoldingState
	 * @return This StateMachineBuilder instance to use for further construction operations
	"""
	def withActionInHolding(self, action: StateAction) :
		self.withAction(action, ActiveStateName.Holding)
		return self
	

	"""
	 * Adds an IStateAction that is to be executed in UnholdingState. Alias for withAction(action, ActiveStateName.Unholding).
	 * 
	 * @param action An instance of IStateAction that is executed in UnholdingState
	 * @return This StateMachineBuilder instance to use for further construction operations
	"""
	def withActionInUnholding(self, action: StateAction) :
		self.withAction(action, ActiveStateName.Unholding)
		return self
	

	"""
	 * Adds an IStateAction that is to be executed in ResettingState. Alias for withAction(action, ActiveStateName.Resetting).
	 * 
	 * @param action An instance of IStateAction that is executed in ResettingState
	 * @return This StateMachineBuilder instance to use for further construction operations
	"""
	def withActionInResetting(self, action: StateAction) :
		self.withAction(action, ActiveStateName.Resetting)
		return self
	

	"""
	 * Adds an IStateAction that is to be executed in StoppingState. Alias for withAction(action, ActiveStateName.Stopping).
	 * 
	 * @param action An instance of IStateAction that is executed in StoppingState
	 * @return This StateMachineBuilder instance to use for further construction operations
	"""
	def withActionInStopping(self, action: StateAction) :
		self.withAction(action, ActiveStateName.Stopping)
		return self
	

	"""
	 * Adds an IStateAction that is to be executed in AbortingState. Alias for withAction(action, ActiveStateName.Aborting).
	 * 
	 * @param action An instance of IStateAction that is executed in AbortingState
	 * @return This StateMachineBuilder instance to use for further construction operations
	"""
	def withActionInAborting(self, action: StateAction) :
		self.withAction(action, ActiveStateName.Aborting)
		return self
	

	"""
	 * Adds an IStateAction that is to be executed in ClearingState. Alias for withAction(action, ActiveStateName.Clearing).
	 * 
	 * @param action An instance of IStateAction that is executed in ClearingState
	 * @return This StateMachineBuilder instance to use for further construction operations
	"""
	def withActionInClearing(self, action: StateAction) :
		self.withAction(action, ActiveStateName.Clearing)
		return self
	

	"""
	 * Finishes building the Isa88StateMachine and returns a fresh instance with the given attributes
	 * 
	 * @return Fresh instance of Isa88StateMachine
	"""
	def build(self) :
		return self.stateMachine
	
