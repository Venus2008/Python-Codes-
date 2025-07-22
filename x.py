n = "588432347423122345"

# This list will collect each maximal ascending run of digits
found = []

# Start the first run with the very first character
current_run = n[0]

# Walk through the string from the second character onward
for i in range(1, len(n)):
    # If this digit is exactly one more than the previous, extend the run
    if int(n[i]) == int(n[i-1]) + 1:
        current_run += n[i]
    else:
        # Otherwise, the run has broken:
        # — if it was length ≥2, record it
        if len(current_run) >= 2:
            found.append(current_run)
        # — start a new run at this digit
        current_run = n[i]

# After the loop, we might have one more run to record
if len(current_run) >= 2:
    found.append(current_run)

# Print them comma-separated
print(", ".join(found))