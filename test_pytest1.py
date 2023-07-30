class Test_pytest():
    def test_sum(self):
        a=10
        b=20
        print(a+b)
    def test_sub(self):
        a=10
        b=20
        print(a-b)
        if a==b:
            print("it is true")
            assert True
        else:
            print("it is false")
            assert False
