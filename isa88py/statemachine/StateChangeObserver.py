from abc import ABC, abstractmethod

class StateChangeObserver(ABC) :
	from isa88py.states.IState import IState

	@abstractmethod
	def onStateChanged(self, newState: IState):
		"""
		Gets called every time the state of a state machine changes
		@param newState The new state that the state machine is in.
		"""
		pass