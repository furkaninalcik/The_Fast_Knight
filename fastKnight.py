class Position:
	def __init__(self, x, y):
		self.x = x
		self.y = y


	def __sub__(self, other):
		x = self.x - other.x
		y = self.y - other.y
		return Position(x, y)

'''n = input()

#target must be to the right of the start

startPositionX = input()
startPositionY = input()

start = Position(startPositionX, startPositionY)

targetPositionX = input()
targetPositionY = input()

target = Position(targetPositionX, targetPositionX)
'''
ruu = (1,2) #region1 step
rru = (2,1) #region2 step
rrd = (2,-1)#region3 step
rdd = (1,-2)#region4 step

llu = (-2,1)
lld = (-2,-1)
luu = (-1,2)
ldd = (-1,-2)

'''def setPoints(start,target): #target will be at the up-right side of the start
	if (target.x < start.x):
		temp = start
		start = target
		target = temp
	if(target.y < start.y)
'''
def moveStart(start, step):
	start.x = start.x + step[0]
	start.y = start.y + step[1]
	return start


def findDistance(start,target):

	if((target-start).x + (target-start).y < 5):
		return 0
	if(start.x < target.x and start.y < target.y and (target-start).x < (target-start).y ):#region1
		start = moveStart(start,ruu)
		return 1 + findDistance(start,target)
	if(start.x < target.x and start.y < target.y and (target-start).x > (target-start).y ):#region2
		start = moveStart(start,rru)
		return 1 + findDistance(start,target)
	if(start.x < target.x and start.y > target.y and (target-start).x > (target-start).y ):#region3
		start = moveStart(start,rrd)
		return 1 + findDistance(start,target)
	if(start.x < target.x and start.y > target.y and (target-start).x < (target-start).y ):#region4
		start = moveStart(start,rrd)
		return 1 + findDistance(start,target)
	else:
		start = moveStart(start,ruu)
		return 1 + findDistance(start,target)
		
start = Position(1,1)
target = Position(70,70)

print("Result:")
print(findDistance(start,target))
