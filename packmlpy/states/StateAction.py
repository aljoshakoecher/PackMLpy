from abc import ABC, abstractmethod

class StateAction(ABC):
	
	@abstractmethod
	async def execute(self):
		pass
