input = open('input').read()
lines = input.split('\n')

directories = dict()
dir_history = []
current_dir = None

def get_parent(dir: str):
    parts = dir.split('/')
    if len(parts) == 2:
        return None
    return '/'.join(parts[:-2]) + '/'

for line in lines:
    if line.startswith('$ cd'):
        _, _, dir_cmd = line.split(' ')
        if dir_cmd == '/':
            current_dir = '/'
            directories['/'] = 0
            dir_history.append(current_dir)
        elif dir_cmd == '..':
            assert len(dir_history) > 0
            dir_history.pop()
            current_dir = dir_history[-1]
        elif dir_cmd.isalpha:
            current_dir = current_dir + dir_cmd + '/'
            assert not current_dir in directories.keys()
            directories[current_dir] = 0
            dir_history.append(current_dir)
        else:
            print("Unexpected dir", dir_cmd)
    elif line.startswith('$ ls'):
        continue
    elif line.startswith('dir'):
        continue
    else:
        size, name = line.split(' ')
        size = int(size)
        dir = current_dir
        while dir != None:
            directories[dir] += size
            dir = get_parent(dir)

print(sum([size for size in directories.values() if size <= 100000]))

currently_in_use = directories['/']
total_req = 70000000 - 30000000

results = []
smallest = 70000000
for dir, size in directories.items():
    if size < smallest:
        if currently_in_use - size < total_req:
            smallest = size

print(smallest)