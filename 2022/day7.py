class Directory():

    def __init__(self, name, parent):
        self.name = name
        self.parent = parent
        self.files = []
        self.dirs = []
        self.size = 0

    def add_file(self, file):
        self.files.append(file)
    
    def add_dir(self, dir):
        self.dirs.append(dir)

    def list_directories(self):
        names = []
        for dir in self.dirs:
            names.append(dir.name)
        return names

    def get_directory(self, name):
        for dir in self.dirs:
            if name == dir.name:
                return dir

    def calculate_size(self):
        size_sum = sum(self.files)
        for d in self.dirs:
            dir_size = d.calculate_size()
            size_sum += dir_size
        self.size = size_sum
        return size_sum

current_dir = Directory('', '')
main_dir = ''
listing_files = False
with open('input_7.txt') as f:
    for line in f.readlines():
        line = line.strip('\n')
        if line.startswith('$ cd'):
            listing_files = False
            _, _, dir = line.split(' ')

            if dir == '..':
                current_dir = current_dir.parent
            else:
                # check if we already created an object for this dir
                if dir in current_dir.list_directories():
                    d = current_dir.get_directory(dir)
                else:
                    d = Directory(dir, current_dir)
                current_dir = d

                if dir == '/':
                    main_dir = d

        elif line.startswith('$ ls'):
            listing_files = True
            continue
    
        if listing_files:
            if line.startswith('dir'):
                name = line.split(' ')[1]
                d = Directory(name, current_dir)
                current_dir.add_dir(d)
            else:
                file_size = line.split(' ')[0]
                current_dir.add_file(int(file_size))
            
main_dir.calculate_size()

def check_dirs(dir, total_sum):
    if dir.size <= 100000:
        total_sum += dir.size
    for d in dir.dirs:
        total_sum = check_dirs(d, total_sum)
    return total_sum
    
total_sum = check_dirs(main_dir, 0)
print(total_sum)

used_space = main_dir.size
free_space = 70000000 - main_dir.size
delete_space = 30000000 - free_space
print('used space ', used_space) 
print('free space ', free_space)
print('we need to free up ', delete_space)

def find_dir_to_delete(dir, delete_space, current_dir_size_to_delete):
    size = dir.size
    if size >= delete_space and size < current_dir_size_to_delete:
        current_dir_size_to_delete = size
    for d in dir.dirs:
        current_dir_size_to_delete = find_dir_to_delete(d, delete_space, current_dir_size_to_delete)
    return current_dir_size_to_delete

dir_size_to_delete = find_dir_to_delete(main_dir, delete_space, 70000000)
print(dir_size_to_delete)
