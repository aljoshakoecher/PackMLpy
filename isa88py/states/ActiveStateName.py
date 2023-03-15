from enum import Enum

class ActiveStateName(Enum):
	Starting="Starting"
	Execute="Execute"
	Completing="Completing"
	Holding="Holding"
	Unholding="Unholding"
	Suspending="Suspending"
	Unsuspending="Unsuspending"
	Stopping="Stopping"
	Clearing="Clearing"
	Aborting="Aborting"
	Resetting="Resetting"