from server import result
from threading import Thread

def test(s):
	print(s)
	return 150


th = Thread(target=test, args=['s', result])
th.start()

print(result)