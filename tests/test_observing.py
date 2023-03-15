from isa88py.states.StateAction import StateAction
from isa88py.statemachine.StateChangeObserver import StateChangeObserver


import time

dummyActionTime = 0.3		# Sleep time

class ExampleObserver(StateChangeObserver):
	from isa88py.states.IState import IState
	observedStateName: str
	
	def onStateChanged(self,newState: IState):
		self.observedStateName = newState.__class__.__name__


class SleepAction(StateAction):
	""" Dummy action that just pauses the thread """

	
	def execute(self):
		time.sleep(dummyActionTime)


class TestObserving:
	
	from isa88py.statemachine.StateMachineBuilder import StateMachineBuilder
	from isa88py.statemachine.Isa88StateMachine import Isa88StateMachine

	dummyAction = SleepAction()
	stateMachine: Isa88StateMachine
	firstObserver: ExampleObserver 
	secondObserver: ExampleObserver 

	def setUp(self):
		firstObserver = ExampleObserver()
		secondObserver = ExampleObserver()
		
		builder = StateMachineBuilder()
		self.stateMachine = builder.withActionInAborting(self.dummyAction).withActionInClearing(self.dummyAction).withActionInCompleting(self.dummyAction)\
			.withActionInExecute(self.dummyAction).withActionInHolding(self.dummyAction).withActionInResetting(self.dummyAction).withActionInStarting(self.dummyAction)\
			.withActionInStopping(self.dummyAction).withActionInSuspending(self.dummyAction).withActionInUnholding(self.dummyAction).withActionInUnsuspending(self.dummyAction)\
			.build()
	
	# @Test
	@pytest.mark.order1
	def test_addFirstObserverAndStart(self):
		self.stateMachine.addStateChangeObserver(self.firstObserver)
		self.stateMachine.start()
		assert self.firstObserver.observedStateName == "StartingState","Observer should be notified that the state machine is now in Starting" 
		# assert self.firstObserver.observedStateName, "Starting", "Observer should be notified that the state machine is now in Starting"\)
	
	# @Test
	@pytest.mark.order2
	def test_ResetWithFirstObserver(self):
		time.sleep(dummyActionTime*4)		# Wait for execution of starting, execute, completing + safetyTime 
		self.stateMachine.reset()
		time.sleep(dummyActionTime*2)		# Wait for execution of resetting + safetyTime
		assert self.firstObserver.observedStateName == "IdleState", "Observer should be notified that the state machine is now in Idle"
	
	# @Test
	@pytest.mark.order3
	def test_addSecondObserverAndStart(self):
		self.stateMachine.addStateChangeObserver(self.secondObserver)
		self.stateMachine.start()
		assert self.secondObserver.observedStateName == "StartingState", "Second observer should be notified that the state machine is now in Starting" 
		# assertEquals(secondObserver.observedStateName, "StartingState", "Second observer should be notified that the state machine is now in Starting")
	
	# @Test
	@pytest.mark.order4
	def test_makeSureFirstObserverStillWorking(self):
		time.sleep(dummyActionTime*4)		# Wait for execution of starting, execute, completing + safetyTime
		assert self.firstObserver.observedStateName == "CompleteState","First observer should have tracked changes and should now be in CompleteState" 
		# assertEquals(firstObserver.observedStateName, "CompleteState", "First observer should have tracked changes and should now be in CompleteState")
	
	# @Test
	@pytest.mark.order5
	def test_removeSecondObserverAndMakeSureFirstObserverStillWorking(self):
		self.stateMachine.removeStateChangeObserver(self.secondObserver)
		self.stateMachine.reset()
		time.sleep(dummyActionTime*2)		# Wait for execution of resetting + safetyTime
		assert self.firstObserver.observedStateName == "IdleState", "First observer should now be in IdleState"
		# assertEquals(firstObserver.observedStateName, "IdleState", "First observer should now be in IdleState")
	
	# @Test
	@pytest.mark.order6
	def test_SecondOberserverNoLongerNotified(self):
		assert self.secondObserver.observedStateName == "CompleteStaet", "Second observer should not have been notified after removal and should still be in CompleteState" 