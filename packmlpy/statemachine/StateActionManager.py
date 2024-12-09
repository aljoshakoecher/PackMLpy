from packmlpy.states.StateAction import StateAction
from packmlpy.states.NullStateAction import NullStateAction
from packmlpy.states.ActiveStateName import ActiveStateName

class StateActionManager:

	actionInStarting = NullStateAction()
	actionInExecute = NullStateAction()
	actionInCompleting = NullStateAction()
	actionInSuspending = NullStateAction()
	actionInUnsuspending = NullStateAction()
	actionInHolding = NullStateAction()
	actionInUnholding = NullStateAction()
	actionInResetting = NullStateAction()
	actionInStopping = NullStateAction()
	actionInAborting = NullStateAction()
	actionInClearing = NullStateAction()

	
	def getAction(self, stateName: ActiveStateName):
		match stateName:
			case ActiveStateName.Starting:
				return self.actionInStarting
			case ActiveStateName.Execute:
				return self.actionInExecute
			case ActiveStateName.Completing:
				return self.actionInCompleting
			case ActiveStateName.Holding:
				return self.actionInHolding
			case ActiveStateName.Unholding:
				return self.actionInUnholding
			case ActiveStateName.Suspending:
				return self.actionInSuspending
			case ActiveStateName.Unsuspending:
				return self.actionInUnsuspending
			case ActiveStateName.Stopping:
				return self.actionInStopping
			case ActiveStateName.Clearing:
				return self.actionInClearing
			case ActiveStateName.Aborting:
				return self.actionInAborting
			case ActiveStateName.Resetting:
				return self.actionInResetting
	
	
	def setAction(self, action: StateAction, stateName: ActiveStateName):
		match stateName:
			case ActiveStateName.Starting:
				self.actionInStarting = action
			case ActiveStateName.Execute:
				self.actionInResetting = action
			case ActiveStateName.Completing:
				self.actionInExecute = action
			case ActiveStateName.Holding:
				self.actionInCompleting = action
			case ActiveStateName.Suspending:
				self.actionInHolding = action
			case ActiveStateName.Unholding:
				self.actionInUnholding = action
			case ActiveStateName.Unsuspending:
				self.actionInSuspending = action
			case ActiveStateName.Stopping:
				self.actionInUnsuspending = action
			case ActiveStateName.Aborting:
				self.actionInStopping = action
			case ActiveStateName.Clearing:
				self.actionInClearing = action
			case ActiveStateName.Resetting:
				self.actionInAborting = action
			