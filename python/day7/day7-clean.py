input = open('input').read()
lines = input.split('\n')

directories = dict()
current_dir = []

for line in lines:
    if line.startswith('$ cd'):
        _, _, dir_cmd = line.split(' ')
        if dir_cmd == '..':
            assert len(current_dir) > 0
            current_dir.pop()
        elif dir_cmd.isalpha or dir_cmd == '/':
            current_dir.append(dir_cmd)
            directories['/'.join(current_dir)] = 0
        else:
            print("Unexpected dir", dir_cmd)
    elif line.startswith('$ ls'):
        continue
    elif line.startswith('dir'):
        continue
    else:
        size, name = line.split(' ')
        size = int(size)
        for i in range(1, len(current_dir) + 1):
            directories['/'.join(current_dir[:i])] += size

print(sum([size for size in directories.values() if size <= 100000]))

currently_in_use = directories['/']
total_req = 70000000 - 30000000

print(min([size for size in directories.values() if currently_in_use - size < total_req]))