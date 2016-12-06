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
        if current[1] not in range(next[0], next[1]):
            consolidated.append(current)
            idx += 1
        else:
            consolidated.append((current[0], next[1]))
            idx += 2

    if fully_consolidated(consolidated):
        return consolidated
    else:
        return merge_ranges(consolidated)

def fully_consolidated(consolidated):
    earliest = consolidated[0][0]
    latest = consolidated[0][1]

    for meeting in consolidated:
        if (meeting[0] > earliest) and (meeting[1] < latest):
            return False

    return True

# Interview Cake's Solution
def merge_ranges(meetings):
    # sort by start times
    sorted_meetings = sorted(meetings)

    # initialize merged_meetings with the earliest meeting
    merged_meetings = [sorted_meetings[0]]

    for current_meeting_start, current_meeting_end in sorted_meetings[1:]:

        last_merged_meeting_start, last_merged_meeting_end = merged_meetings[-1]

        # if the current and last meetings overlap, use the latest end time
        if (current_meeting_start <= last_merged_meeting_end):
            merged_meetings[-1] = (last_merged_meeting_start, max(last_merged_meeting_end, current_meeting_end))

        # add the current meeting since it doesn't overlap
        else:
            merged_meetings.append((current_meeting_start, current_meeting_end))

    return merged_meetings