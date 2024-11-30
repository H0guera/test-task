def make_set_of_presence(
    lesson_intervals: list[int], entity_intervals: list[int]
) -> set[int]:
    set_of_appearance = set()
    while entity_intervals:
        start = entity_intervals.pop(0)
        if start < lesson_intervals[0]:
            start = lesson_intervals[0]
        end = entity_intervals.pop(0)
        if end > lesson_intervals[1]:
            end = lesson_intervals[1]
        set_of_appearance.update([*range(start, end)])
    return set_of_appearance


def appearance(intervals: dict[str, list[int]]) -> int:
    pupil_presence: set[int] = make_set_of_presence(
        intervals["lesson"], intervals["pupil"]
    )
    tutor_presence: set[int] = make_set_of_presence(
        intervals["lesson"], intervals["tutor"]
    )
    return len(pupil_presence & tutor_presence)
