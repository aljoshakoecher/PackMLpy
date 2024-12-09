from packmlpy.states.StateAction import StateAction

class NullStateAction(StateAction):

	async def execute(self):
		"""
		Execute of a NullStateAction} simply does nothing
		"""