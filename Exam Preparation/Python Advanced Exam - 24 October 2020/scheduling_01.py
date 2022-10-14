from collections import deque

jobs = [int(x) for x in input().split(", ")]

task_index = int(input())
task_number = jobs[task_index]

cycles = 0

for _ in range(len(jobs)):
    lowest_num = min([x for x in jobs if x])

    cycles += lowest_num
    idx_lowest_num = jobs.index(lowest_num)

    if idx_lowest_num == task_index:
        break
    jobs[idx_lowest_num] = None

print(cycles)
