# analyze every *.py and list the status
import os
import shutil

file_list = os.listdir('..')
solved_list = []
unsolved_list = []
for i in file_list:
    if i[0] == '[':
        file_name = '../' + i
        print(file_name)
        f = open(file_name, 'r', encoding='utf-8')
        if len(f.readlines()) > 4:
            f.close()
            solved_list.append(i)
            shutil.move('../'+i, '../solved/' + i)
        else:
            unsolved_list.append(i)
            f.close()


print('number of unsolved: ', len(unsolved_list))
print('number of solved: ', len(solved_list))


