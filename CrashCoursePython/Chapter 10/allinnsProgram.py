## Doing Allinn's UCSD beginner program exercise:

n = input()
n = int(n)

star = "+-+-+"
bar = "  | |"
space = "  "
end = "+-+"

print("+-+\n| |")
for i in range(n - 1):
    print(star)
    print(bar)
    star = space + star
    bar = space + bar
    end = space + end

print(end)


## Allinn's solution was similar, but involved multiplying spaces:

print()

for i in range(int(input())):
    print("+-+")
    print("  " * i + "| |")
    print("  " * i + "+-", end = '')
print("+")

