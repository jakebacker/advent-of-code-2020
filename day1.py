data = ''''''

nums = data.split("\n")

for x in range(0, len(nums)):
    for y in range(0, len(nums)):
        for z in range(0, len(nums)):
            if x != y and x != z and y != z:
                x_val = int(nums[x])
                y_val = int(nums[y])
                z_val = int(nums[z])

                if x_val + y_val + z_val == 2020:
                    print("aaaaaa")
                    print(x_val)
                    print(y_val)
                    print(z_val)
                    print(x_val * y_val * z_val)
                    print()

