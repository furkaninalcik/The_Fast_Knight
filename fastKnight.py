n = input()

startPositionX = input()
startPositionY = input()


class Position:
  def __init__(self, x, y):
    self.x = x
    self.y = y

start = Position(startPositionX, startPositionY)

targetPositionX = input()
targetPositionY = input()

target = Position(targetPositionX, targetPositionX)

rru = (2,1)
rrd = (2,-1)
ruu = (1,2)
rdd = (1,-2)

llu = (-2,1)
lld = (-2,-1)
luu = (-1,2)
ldd = (-1,-2)


def findDistance(start,target):
    if(start.x)