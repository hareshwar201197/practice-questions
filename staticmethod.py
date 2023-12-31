class Test:
    count = 0

    def __init__(self):
        Test.count = Test.count + 1

    @classmethod
    def getnoofobjects(cls):
        print('The Number of objects created ', cls.count)

t1 = Test()
t2 = Test()
Test.getnoofobjects()