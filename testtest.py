from concurrent.futures import ProcessPoolExecutor
import asyncio
import time

from typing import Callable
start_time = time.time()
executor = ProcessPoolExecutor(2)
loop = asyncio.new_event_loop()
tasks = dict[str, asyncio.Future]()

class StateMachine:
	
	async def doAction1(self):
		print("started action 1", time.time() - start_time)
		try:
			time.sleep(15)
			# await asyncio.sleep(15)
			print("finished action 1", time.time() - start_time)
		except:
			print("cancelled 1", time.time() - start_time)

	async def doAction2(self):
		print("started action 2", time.time() - start_time)
		try:
			time.sleep(3)
			# await asyncio.sleep(3)
			# tasks["doAction1"].cancel()
			print("finished action 2", time.time() - start_time)
		except:
			print("cancelled 2", time.time() - start_time)

	def runAction(self, action: Callable):
		print("in state machine", time.time() - start_time)
		if len(tasks) > 0:
			print("cancelled in stateMachine")
			# for key, value in tasks.values():
				# print("cancelling: ", key)
			print("cancelling at ", time.time() - start_time)
			tasks['doAction1'].cancel()
		
		tasks[action.__name__] = asyncio.create_task(action())
		print("after call, doing something concurrently")

async def main():
	stateMachine = StateMachine()
	print("Time 1:" , time.time() - start_time)
	# tasks.append(loop.run_in_executor(executor, stateMachine.doAction1))
	stateMachine.runAction(stateMachine.doAction1)
	print("Time 2:" , time.time() - start_time)
	print("waiting 10")
	# time.sleep(10)
	await asyncio.sleep(10)
	print("ended waiting")
	# asyncio.run(asyncio.sleep(1))
	print("Time 3:" , time.time() - start_time)
	# tasks.append(loop.run_in_executor(executor, stateMachine.doAction2))
	stateMachine.runAction(stateMachine.doAction2)
	
	print("Time 4:" , time.time() - start_time)
	# asyncio.run(asyncio.sleep(5))
	# print("Time 5:" , time.time() - start_time)
	# self.task.cancel()
	print("ended main")
	# loop.run_forever()
	# loop.run_until_complete(stateMachine.tasks[0])
	

if __name__ == '__main__':	
	print("Time 0:" , 0)
	sm = StateMachine()
	asyncio.run(main())
	# a = loop.run_in_executor(executor, sm.doAction1)
	# b = loop.run_in_executor(executor, sm.doAction2)
	# main()
	

