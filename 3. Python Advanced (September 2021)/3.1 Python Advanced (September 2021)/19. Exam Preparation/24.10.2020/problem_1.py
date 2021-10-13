def read_input(is_test=False):
    if is_test:
        return ([3, 1, 10, 1, 2], 0)
    return (map(int, input().split(', ')),
            int(input()))


def min_cycles_for_job(jobs, job_index):
    sorted_jobs = sorted(
        [(v, i) for (i, v) in enumerate(jobs)]
    )
    cycles = 0
    for job, index in sorted_jobs:
        cycles += job
        if index == job_index:
            break
    return cycles


def print_result(result):
    print(result)


jobs, job_index = read_input()
result = min_cycles_for_job(jobs, job_index)
print_result(result)
