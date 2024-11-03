def find_common_participants (first,second,razd=','):
    first = first.split(razd)
    second = second.split(razd)
    inter = []
    for i in first:
        if i in second:
            inter.append(i)
        inter = sorted(inter)
    return inter


participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

participants = find_common_participants(participants_first_group,participants_second_group,'|')
print(participants)
