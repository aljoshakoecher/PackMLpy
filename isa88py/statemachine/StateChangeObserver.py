from abc import ABC, abstractmethod
from typing import TYPE_CHECKING

if TYPE_CHECKING:
	from isa88py.states.State import State

class StateChangeObserver(ABC) :

	@abstractmethod
	def onStateChanged(self, newState: 'State'):
		"""
		Gets called every time the state of a state machine changes
		@param newState The new state that the state machine is in.
		"""
		pass