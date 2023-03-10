from abc import ABC, abstractmethod
from states.IState import IState

class StateChangeObserver(ABC) :

	@abstractmethod
	def onStateChanged(self, newState: IState):
		"""
		Gets called every time the state of a state machine changes
		@param newState The new state that the state machine is in.
		"""
		pass