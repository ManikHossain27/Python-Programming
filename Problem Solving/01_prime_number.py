# Find prime numbers from a list of 0-20

# numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
#
# for number in numbers:
#     if number < 2:
#         continue
#
#     is_prime = True
#     for i in range(2, number):
#         if number % i == 0:
#             is_prime = False
#             break
#
#     if is_prime:
#         print(number)

numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
list = []

for number in numbers:
    if number >= 2:
        is_prime = True
        for i in range(2, number):
            if number % i == 0:
                is_prime = False
                break

        if is_prime:
            print(number)
            list.append(number)
print('Prime numbrs', list)

