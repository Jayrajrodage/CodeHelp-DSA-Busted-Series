def say(n):
    arr= ["zero", "one", "two", "three",
                         "four", "five", "six"
                        , "seven", "eight", "nine"]
    if n==0:
        return ""
    dig=int(n%10)
    n=int(n/10)
    say(n)
    print(arr[dig],end=" ")
    return ""
print(say(314948))
