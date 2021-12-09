class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        i=1
        list = []
        while i <= n:
            if i % 3 == 0 and i % 5 == 0:
                list.append("FizzBuzz")
                i += 1
            elif i % 3 == 0:
                list.append("Fizz")
                i += 1
            elif i%5 == 0:
                list.append("Buzz")
                i += 1
            else:
               list.append(str(i))
               i += 1
        return list
