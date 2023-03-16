from isa88py.states.StateAction import StateAction
from isa88py.statemachine.StateChangeObserver import StateChangeObserver
from typing import TYPE_CHECKING

if TYPE_CHECKING:
	from isa88py.statemachine.Isa88StateMachine import Isa88StateMachine
	from isa88py.states.State import State

import pytest
import time

dummyActionTime = 0.3		# Sleep time

class ExampleObserver(StateChangeObserver):
	
	def __init__(self) -> None:
		super().__init__()
		self.observedStateName = "None"

	def onStateChanged(self,newState: 'State'):
		print(newState.__class__.__name__)
		self.observedStateName = newState.__class__.__name__


class SleepAction(StateAction):
	""" Dummy action that just pauses the thread """

	
	def execute(self):
		time.sleep(dummyActionTime)


from isa88py.statemachine.StateMachineBuilder import StateMachineBuilder

class TestObserving:
	
	dummyAction = SleepAction()
	builder = StateMachineBuilder()
	stateMachine = builder.withActionInAborting(dummyAction).withActionInClearing(dummyAction).withActionInCompleting(dummyAction)\
		.withActionInExecute(dummyAction).withActionInHolding(dummyAction).withActionInResetting(dummyAction).withActionInStarting(dummyAction)\
		.withActionInStopping(dummyAction).withActionInSuspending(dummyAction).withActionInUnholding(dummyAction).withActionInUnsuspending(dummyAction)\
		.build()
	firstObserver = ExampleObserver()
	secondObserver = ExampleObserver()

	# @pytest.fixture(scope="module",autouse=True)
	# def setUp(self):
	# 	self.firstObserver = ExampleObserver()
	# 	self.secondObserver = ExampleObserver()
		
	# 	builder = StateMachineBuilder()
	# 	self.stateMachine = builder.withActionInAborting(self.dummyAction).withActionInClearing(self.dummyAction).withActionInCompleting(self.dummyAction)\
	# 	.withActionInExecute(self.dummyAction).withActionInHolding(self.dummyAction).withActionInResetting(self.dummyAction).withActionInStarting(self.dummyAction)\
	# 	.withActionInStopping(self.dummyAction).withActionInSuspending(self.dummyAction).withActionInUnholding(self.dummyAction).withActionInUnsuspending(self.dummyAction)\
	# 	.build()
	
	@pytest.mark.order(1)
	def test_addFirstObserverAndStart(self):
		self.stateMachine.addStateChangeObserver(self.firstObserver)
		self.stateMachine.start()
		assert self.firstObserver.observedStateName == "StartingState","Observer should be notified that the state machine is now in Starting" 
	
	@pytest.mark.order(2)
	def test_ResetWithFirstObserver(self):
		time.sleep(dummyActionTime*4)		# Wait for execution of starting, execute, completing + safetyTime 
		self.stateMachine.reset()
		time.sleep(dummyActionTime*2)		# Wait for execution of resetting + safetyTime
		assert self.firstObserver.observedStateName == "IdleState", "Observer should be notified that the state machine is now in Idle"
	
	@pytest.mark.order(3)
	def test_addSecondObserverAndStart(self):
		self.stateMachine.addStateChangeObserver(self.secondObserver)
		self.stateMachine.start()
		assert self.secondObserver.observedStateName == "StartingState", "Second observer should be notified that the state machine is now in Starting" 
	
	@pytest.mark.order(4)
	def test_makeSureFirstObserverStillWorking(self):
		time.sleep(dummyActionTime*4)		# Wait for execution of starting, execute, completing + safetyTime
		assert self.firstObserver.observedStateName == "CompleteState","First observer should have tracked changes and should now be in CompleteState" 
	
	@pytest.mark.order(5)
	def test_removeSecondObserverAndMakeSureFirstObserverStillWorking(self):
		self.stateMachine.removeStateChangeObserver(self.secondObserver)
		self.stateMachine.reset()
		time.sleep(dummyActionTime*2)		# Wait for execution of resetting + safetyTime
		assert self.firstObserver.observedStateName == "IdleState", "First observer should now be in IdleState"

	@pytest.mark.order(6)
	def test_SecondOberserverNoLongerNotified(self):
		assert self.secondObserver.observedStateName == "CompleteStaet", "Second observer should not have been notified after removal and should still be in CompleteState" 