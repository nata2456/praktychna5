# Дано два списки.Знайти обєднання цих списків, у порядку зростання.
num_list1 = set([float(input('Enter number {0}: '.format(x + 1))) for x in range(5)])
num_list2 = set([float(input('Enter number {0}: '.format(x + 1))) for x in range(5)])
print(sorted(num_list1 | num_list2))
