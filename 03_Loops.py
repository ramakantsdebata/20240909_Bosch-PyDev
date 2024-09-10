# # loops in Python - For, While
# # No do-while loops in Python

# lst = [1, 2, 3, 4, 5]
# for x in lst:
#     print(x, end=' ')
# print()

# # for x in range(10):
# # for x in range(5, 25, 2):
# for _ in range(5, 25, 2):
#     print("Hi", end=', ')
# print()


# lst = [1, 2, 3, 4, 5]
# x = 3
# for val in lst:
#     if x == val:
#         print("Found it")
#         break
# else: # Executes this block if all iterations are completed without a break
#     print("Not Found")

# ## Error-prone
# # if val >= lst[len(lst) - 1]:
# #     print("Not Found")

# ## continue - Skip executio of the remaining statements in the block and move on to the next iteration, if any.



# ## while

# x = 0
# while True:
#     print(x)
#     x += 2
#     if x >= 10:
#         break


x = 0

while x < 10:
    print(x)
    if x == 50:
        break
    x += 1
else:      # Executes this block if all iterations are completed without a break
    print("No breaks occurred")

