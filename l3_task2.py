# TODO Напишите функцию find_common_participants
def find_common_participants(participants_1, participants_2, separator=','):
    first_group = set(participants_1.split(separator))
    second_group = set(participants_2.split(separator))
    common_participants =list(first_group.intersection(second_group))
    common_participants.sort()
    return common_participants

participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"
# TODO Провеьте работу функции с разделителем отличным от запятой
common_participants = find_common_participants(participants_first_group, participants_second_group, separator='|')
print(common_participants)
