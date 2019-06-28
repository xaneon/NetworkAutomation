s1 = "2827837"
s2 = "233434.3433"
s3 = "kdjfkdj2233"
s4 = "-42"
s5 = "-45.5"
s6 = "3^2"
s7 = "3**4"
s8 = "99/44"
alle = [s1, s2, s3, s4, s5, s6, s7, s8]

def testall(s):
    print(s)
    print("isdigit:",  s.isdigit())
    print("isnumeric:",  s.isnumeric())
    print("isdecimal:",  s.isdecimal())
    print("#" * 10)

[testall(s) for s in alle]

