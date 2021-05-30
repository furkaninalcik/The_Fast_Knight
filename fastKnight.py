import math
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

def formula(dx,dy):
	#print(dx)
	#print(dy)
	a = int(round(max(dx/2,dy/2,(dx+dy)/3)))
	return a + ((a+dx+dy)%2)
	
	
def findDistance(start,target):

	if((target-start).x + (target-start).y < 5):#wrong!
		return 2
	if(start.x < target.x and start.y < target.y and (target-start).x < (target-start).y ):#region1
		#print("region1")
		start = moveStart(start,ruu)
		return 1 + findDistance(start,target)
	if(start.x < target.x and start.y < target.y and (target-start).x > (target-start).y ):#region2
		#print("region2")
		start = moveStart(start,rru)
		return 1 + findDistance(start,target)
	if(start.x < target.x and start.y > target.y and (target-start).x > (target-start).y ):#region3
		#print("region3")
		start = moveStart(start,rrd)
		return 1 + findDistance(start,target)
	if(start.x < target.x and start.y > target.y and (target-start).x < (target-start).y ):#region4
		print("region4")
		start = moveStart(start,rdd)
		return 1 + findDistance(start,target)
	else:
		if(start.x >= target.x):
			#print("warning")
			start = moveStart(start,luu)
			return 1 + findDistance(start,target)
		#print("start")
		#print(start.x , start.y)
		#print("target")
		#print(target.x , target.y)
		start = moveStart(start,rru)
		return 1 + findDistance(start,target)
		
start = Position(0,0)
start2 = Position(0,0)
target = Position(241,1210)
target2 = Position(241,1210)
print("Result:")
print(findDistance(start,target))
print("Result by Formula:")
vector = target2-start2
#print("TEST")
#print(vector.x,vector.y)
print(formula(vector.x,vector.y))


