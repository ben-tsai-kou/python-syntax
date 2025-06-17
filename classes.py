class Point:
    def draw(self):
        print('draw')

    def move(self):
        print('move')


point1 = Point()
point1.x = 10
point1.y = 20
print(point1.x, point1.y)
point1.move()

