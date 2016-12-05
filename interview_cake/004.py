# HiCal Calendar Tool
def merge_ranges(meetings):
    # in: list of tuples representing meeting time ranges
    # out: condensed list of tuples representing blocks of time when meetings are ocurring

    # sort meetings by start time
    meetings.sort(key=lambda tup: tup[0])
    consolidated = []

    idx = 0

    while idx < len(meetings) - 1:
        current = meetings[idx]
        next = meetings[idx + 1]
        print next
        if current[1] not in range(next[0], next[1]):
            consolidated.append(current)
            idx += 1
        else:
            consolidated.append((current[0], next[1]))
            idx += 2

    return consolidated