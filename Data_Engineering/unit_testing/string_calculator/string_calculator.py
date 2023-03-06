import re


def string_calculator(string):
    if not string:
        return '0'
    elif len(string) == 1:
        return string
    else:
        if string[0:2] == '//':
            separator = re.search('//(.*)\n', string)
            string = string.replace(f'//{separator.group(1)}\n', '')
            nums = re.split(separator.group(1), string)
            print(nums)
        else:
            nums = re.split(',|\n', string)
        total = 0
        try:
            # Sum and map can replace this for loop
            for n in nums:
                total += int(n)
        except ValueError as e:
            return e
        return str(total)

