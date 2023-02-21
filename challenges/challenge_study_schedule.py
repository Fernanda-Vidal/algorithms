def study_schedule(permanence_period, target_time):
    """Faça o código aqui."""
    student_quantity = 0
    if target_time is None:
        return None

    for student in permanence_period:
        if student[0] is None or student[1] is None:
            return None

        if target_time >= student[0] and target_time <= student[1]:
            student_quantity += 1

    return student_quantity
