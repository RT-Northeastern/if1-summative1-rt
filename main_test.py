# import our function rt_fizznumber from rt_fizzbuzz
from rt_fizzbuzz import rt_fizznumber

#defines our function is the fizznumber is divsiable by 2 return Fizz
def test_fizz():
    assert rt_fizznumber(4) == "Fizz"
    assert rt_fizznumber(5) != "Fizz"
    assert rt_fizznumber(2) == "Fizz"

# defines our function if the fizznumber is divsable by 3 return Buzz
def test_buzz():
    assert rt_fizznumber(9) == "Buzz"
    assert rt_fizznumber(8) != "Buzz"
    assert rt_fizznumber(3) == "Buzz"

# defines our function if the fizznumber is divsable by 6 return Fizzbuzz
def test_fizzbuzz():
    assert rt_fizznumber(12) == "Fizzbuzz"
    assert rt_fizznumber(13) != "Fizzbuzz"
    assert rt_fizznumber(6) == "Fizzbuzz"


