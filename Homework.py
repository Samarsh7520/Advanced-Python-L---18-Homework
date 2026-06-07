def fun(input_str):
    n = len(input_str)
    total_combinations = 2 ** n
    sub = []

    for mask in range(1, total_combinations):
        current_sub = ""
        for i in range(n):
            if (mask & (1 << i)):
                current_sub += input_str[i]
        sub.append(current_sub)

    return sub

text = "abc"
print("All subsets using bitwise logic:")
print(fun(text))