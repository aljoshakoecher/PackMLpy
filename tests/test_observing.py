from packmlpy.states.StateAction import StateAction
from packmlpy.statemachine.StateChangeObserver import StateChangeObserver
from typing import TYPE_CHECKING

if TYPE_CHECKING:
	from packmlpy.statemachine.PackMlStateMachine import PackMlStateMachine
	from packmlpy.states.State import State

import pytest
import asyncio
import time

dummyActionTime = 1	# Sleep time
state = "None"

class ExampleObserver(StateChangeObserver):
	
	def __init__(self) -> None:
		super().__init__()
		self.observedStateName = "None"

	def onStateChanged(self,newState: 'State'):
		print("new state")
		print(newState.__class__.__name__)
		print("setting")
		global state
		state = newState
		self.observedStateName = newState.__class__.__name__


class SleepAction(StateAction):
	""" Dummy action that just pauses the thread """

	async def execute(self):
		print("sleep")
		global state
		print("sleeping in state ", state)
		await asyncio.sleep(dummyActionTime)
		print("sleeping over")
		# await asyncio.sleep(dummyActionTime)


from packmlpy.statemachine.StateMachineBuilder import StateMachineBuilder

class TestObserving:


	@pytest.fixture(autouse=True, scope="module")
	def event_loop(self):
		loop = asyncio.new_event_loop()
		
		print("set up fixture")
		dummyAction = SleepAction()
		TestObserving.firstObserver = ExampleObserver()
		TestObserving.secondObserver = ExampleObserver()
		
		builder = StateMachineBuilder()
		TestObserving.stateMachine = builder.withActionInAborting(dummyAction).withActionInClearing(dummyAction).withActionInCompleting(dummyAction)\
		.withActionInExecute(dummyAction).withActionInHolding(dummyAction).withActionInResetting(dummyAction).withActionInStarting(dummyAction)\
		.withActionInStopping(dummyAction).withActionInSuspending(dummyAction).withActionInUnholding(dummyAction).withActionInUnsuspending(dummyAction)\
		.build()
		yield loop
		loop.close()
		
	
	@pytest.mark.asyncio
	@pytest.mark.order(1)
	async def test_addFirstObserverAndStart(self):
		print("go")
		TestObserving.stateMachine.addStateChangeObserver(TestObserving.firstObserver)
		TestObserving.stateMachine.start()
		print("state is:" , TestObserving.firstObserver.observedStateName)
		assert TestObserving.firstObserver.observedStateName == "StartingState","Observer should be notified that the state machine is now in Starting" 
	
	@pytest.mark.asyncio 
	@pytest.mark.order(2)
	async def test_ResetWithFirstObserver(self):
		print(TestObserving.stateMachine.runningTask)
		print("waiting in test 2")
		await asyncio.sleep(dummyActionTime*4)
		print("waiting in test 2 over")
		print("state is:" , TestObserving.stateMachine.currentState)
		assert TestObserving.firstObserver.observedStateName == "CompleteState", "Observer should be notified that the state machine is now in Idle"
		print("resetting")
		TestObserving.stateMachine.reset()
		print("after reset")
		print("state is:" , TestObserving.stateMachine.currentState)
		await asyncio.sleep(dummyActionTime * 2)
		print("state is:" , TestObserving.firstObserver.observedStateName)
		print(TestObserving.stateMachine.taskChecklist)
		assert TestObserving.firstObserver.observedStateName == "IdleState", "Observer should be notified that the state machine is now in Idle"
	
	@pytest.mark.asyncio 
	@pytest.mark.order(3)
	async def test_addSecondObserverAndStart(self):
		TestObserving.stateMachine.addStateChangeObserver(TestObserving.secondObserver)
		TestObserving.stateMachine.start()
		assert TestObserving.secondObserver.observedStateName == "StartingState", "Second observer should be notified that the state machine is now in Starting" 
	
	@pytest.mark.asyncio 
	@pytest.mark.order(4)
	async def test_makeSureFirstObserverStillWorking(self):
		await asyncio.sleep(dummyActionTime*4)		# Wait for execution of starting, execute, completing + safetyTime
		assert TestObserving.firstObserver.observedStateName == "CompleteState","First observer should have tracked changes and should now be in CompleteState" 
	
	@pytest.mark.asyncio 
	@pytest.mark.order(5)
	async def test_removeSecondObserverAndMakeSureFirstObserverStillWorking(self):
		TestObserving.stateMachine.removeStateChangeObserver(TestObserving.secondObserver)
		TestObserving.stateMachine.reset()
		await asyncio.sleep(dummyActionTime*2)		# Wait for execution of resetting + safetyTime
		assert TestObserving.firstObserver.observedStateName == "IdleState", "First observer should now be in IdleState"
		print(TestObserving.stateMachine.taskChecklist)

	@pytest.mark.asyncio 
	@pytest.mark.order(6)
	async def test_SecondOberserverNoLongerNotified(self):
		assert TestObserving.secondObserver.observedStateName == "CompleteState", "Second observer should not have been notified after removal and should still be in CompleteState" 