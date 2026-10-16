"""Module to calculate the total number of students receiving a message."""


def count_recipients(start_student, forward_targets):
    """Count unique recipients following forwarding rules until stopped.

    Stops when reaching 0 (no forward) or an already visited student.
    """
    visited_students = set()
    current_student = start_student

    while current_student and current_student not in visited_students:
        visited_students.add(current_student)
        current_student = forward_targets[current_student]

    return len(visited_students)


def main():
    """Read student forwarding network and output total recipient count."""
    first_line = input().split()
    total_students = int(first_line[0])
    start_student = int(first_line[1])

    forward_targets = [0] * (total_students + 1)
    for student_id in range(1, total_students + 1):
        target_id = int(input().strip())
        forward_targets[student_id] = target_id

    total_recipients = count_recipients(start_student, forward_targets)
    print(total_recipients)


main()
