def add_submission(submissions_dict, lang):
    if lang not in submissions_dict:
        submissions_dict[lang] = 1
    else:
        submissions_dict[lang] += 1


def add_results(results_dict, user, pts):
    if user not in results_dict:
        results_dict[user] = pts
    else:
        if results_dict[user] <= pts:
            results_dict[user] = pts


def ban(results_dict, user):
    if user in results_dict:
        results_dict.pop(user)


submissions = {}
results = {}
command = input()

while not command == "exam finished":
    cmd = command.split("-")
    username = cmd[0]
    if "banned" not in cmd:
        language, points = cmd[1], int(cmd[2])
        add_submission(submissions, language)
        add_results(results, username, points)
    else:
        ban(results, username)
    command = input()

print("Results:")
for username, points in sorted(results.items(), key=lambda kvp: (-kvp[1], kvp[0])):
    print(f"{username} | {points}")

print("Submissions:")
for language, occurrences in sorted(submissions.items(), key=lambda kvp: kvp[0]):
    print(f"{language} - {occurrences}")
