from enum import Enum

class TransitionNames(Enum):
	start="start",
	hold="hold",
	unhold="unhold",
	suspend="suspend",
	unsuspend="unsuspend",
	reset="reset",
	stop="stop",
	abort="abort",
	clear="clear"