from packmlpy.states.TransitionNames import TransitionNames
from packmlpy.statemachine.StateActionManager import StateActionManager
import asyncio
import time
from concurrent.futures import ProcessPoolExecutor
from typing import TYPE_CHECKING

if TYPE_CHECKING:
	from packmlpy.states.State import State	# Import inside class to avoid circular dependency with IState -- State -- StateMachine
	from packmlpy.statemachine.StateChangeObserver import StateChangeObserver

class PackMlStateMachine:

	def __init__(self, initialState: 'State'):
		self.taskChecklist = list[asyncio.Task]()
		self.loop = asyncio.get_event_loop()
		self.runningTask: asyncio.Task
		self.currentState = initialState
		self.stateActionManager = StateActionManager()
		self.stateChangeObservers: list['StateChangeObserver'] = list()

	def setTask(self, task: asyncio.Task):
		self.taskChecklist.append(task)
		self.runningTask = task

	def invokeTransition(self, transitionName: TransitionNames):
		from packmlpy.states.State import State	# Import inside class to avoid circular dependency with IState -- State -- StateMachine
		match transitionName:
			case TransitionNames.start:
				self.start()
			case TransitionNames.hold:
				self.currentState.hold(self)
			case TransitionNames.unhold:
				self.currentState.unhold(self)
			case TransitionNames.suspend:
				self.currentState.suspend(self)
			case TransitionNames.unsuspend:
				self.currentState.unsuspend(self)
			case TransitionNames.reset:
				self.reset()
			case TransitionNames.stop:
				self.currentState.stop(self)
			case TransitionNames.abort:
				self.currentState.abort(self)
			case TransitionNames.clear:
				self.currentState.clear(self)


	def start(self):
		"""
		Execute a start command. Can be used to transition from Idle to Execute. Alias for invokeTransition(TransitionName.start).
		"""
		self.currentState.start(self)
	
	
	def hold(self):
		"""
		Execute a hold command. Can be used to transition from Execute to Held. Alias for invokeTransition(TransitionName.hold).
		"""
		self.currentState.hold(self)
	

	
	def unhold(self):
		"""
		Execute an unhold command. Can be used to transition from Held back to Execute. Alias for invokeTransition(TransitionName.unhold).
		"""
		self.currentState.unhold(self)

	def suspend(self):
		"""
		Execute a suspend command. Can be used to transition Execute to Suspend. Alias for invokeTransition(TransitionName.suspend).
		"""
		self.currentState.suspend(self)

	def unsuspend(self):
		"""
		Execute an unsuspend command. Can be used to transition from Suspended back to Execute. Alias for invokeTransition(TransitionName.unsuspend).
		"""
		self.currentState.unsuspend(self)

	
	def reset(self):
		"""
		Execute a reset command. Can be used to transition from Complete or Stopped back to Idle. Alias for invokeTransition(TransitionName.reset).
		"""
		self.currentState.reset(self)

	def stop(self):
		"""
		Execute a stop command. Can be used to transition from all 'normal' states to Stopped. Alias for invokeTransition(TransitionName.stop).
		"""
		self.currentState.stop(self)

	def abort(self):
		"""
		Execute an abort command. Can be used to transition from all 'normal' and 'stopping'-states to Aborted. Alias for
		invokeTransition(TransitionName.abort).
		"""
		self.currentState.abort(self)

	def clear(self):
		"""
		Execute a clear command. Can be used to transition from Aborted to Stopped. Alias for invokeTransition(TransitionName.clear).
		"""
		self.currentState.clear(self)
	


	def getState(self) -> 'State':
		"""
		Returns the current state of self state machine.
		return: The current state instance
		"""
		return self.currentState
	

	def setState(self, state: 'State'):
		"""
		Sets the current state of the StateMachine.
		state: The new state that will be set as the current state
		"""
		self.currentState = state
	

	
	def setStateAndRunAction(self, state: 'State'):
		"""
		Sets the current state of the StateMachine and runs self state's action.
		state: The new state that will be set as the current state
		"""
		# Stop the current action if there is one
		if hasattr(self, "runningTask") and (self.runningTask.done() is False):
			print("trying to cancel, there are tasks: ", len(self.taskChecklist))
			self.taskChecklist.pop()
			self.runningTask.cancel()

		# Set the new state and notify all observers
		self.currentState = state
		for observer in self.stateChangeObservers:
			observer.onStateChanged(self.currentState)
		
		# Execute the action of the new state
		print("new task for execute action and complete", time.time())
		self.setTask(asyncio.create_task(self.currentState.executeActionAndComplete(self)))


	def getStateActionManager(self) -> 'StateActionManager':
		"""
		Returns the StateActionManager of self state machine.
		@return This state machine's state manager instance
		"""
		return self.stateActionManager


	def addStateChangeObserver(self, observer: 'StateChangeObserver') :
		"""
		Adds a new StateChangeObserver instance to the list of observers.
		observer: The new observer to add.
		"""
		self.stateChangeObservers.append(observer)
	

	def removeStateChangeObserver(self, observer: 'StateChangeObserver'):
		"""
		Removes a given StateChangeObserver instance from the list of observers.
		observer: The observer that is going to be removed.
		"""
		self.stateChangeObservers.remove(observer)