# Task 08. Loading Bar

def loading_bar(progress):
    if progress == 100:
        return f"100% Complete!\n[{''.join('%' for _ in range(10))}]"
    loaded = ['%' for _ in range(progress//10)]
    bar = ["." for _ in range(10-progress//10)]
    total_bar = loaded + bar
    return f"{progress}% [{''.join(total_bar)}]\nStill loading..."


progress = int(input())
print(loading_bar(progress))
