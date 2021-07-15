actual = [0,1]

def find_fibonacci(limit):
    for i in range(3,int(limit)+1):
        length = len(actual)
        second_last_number = length - 2
        actual.append(actual[-1] + actual[second_last_number])

def test_fibonacci():
    expected = [0,1,1,2,3,5,8,13]
    assert len(actual) == len(expected)
    assert all([a == b for a, b in zip(actual, expected)])
    
find_fibonacci(8)
test_fibonacci()
