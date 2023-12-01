def study_schedule(permanence_period, target_time):
    try:
        count = 0
        for entry, out in permanence_period:
            if entry <= target_time <= out:
                count += 1
        return count
    except TypeError:
        return None
