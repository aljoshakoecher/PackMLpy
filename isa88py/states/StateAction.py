from abc import ABC, abstractmethod

class StateAction(ABC):
	
	@abstractmethod
	def execute(self):
		pass
