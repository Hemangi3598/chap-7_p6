# wamdpp (write a menu driven pp ) for data structure: queue / FIFO

queue = []

while True:
	op = int(input("1 insert, 2 remove, 3 display and 4 exit"))
	if op == 1:
		ele = int(input("enter element "))
		queue.append(ele)
		print(ele, "is inserted in the queue")
	elif op == 2:
		if len(queue) == 0:
			print(" queue is empty ")
		else:
			ele = queue.pop(0)
			print("removed element = ", ele)
	elif op == 3:
		print(queue)
	elif op == 4:
		break
	else:
		print(" invalid option")
