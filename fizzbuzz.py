#The classic question.
[print("%s"%x+"fizz"*(not(x%3))+'buzz'*(not(x%5)))for x in range(101)]