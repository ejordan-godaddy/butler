import os


TREE_CHARS= {
    'dir': "├",
    'l_dir': "└",
    'top_level': ".",
    'branches': "──",
}

# find all the files in certain directories
class Directory():
    def __init__(self, directory_name):
        file = "test.txt"
        self.search_file(file)
        self.tree(directory_name)
        print(f"tried searching {directory_name} for {file}")


    def tree(self, top_dir):
        if '~' in top_dir:
            full_path = os.path.expanduser(top_dir)
        for (root, dirs, files) in os.walk(os.fspath(full_path)):
            pass
            #print('{} {} {}'.format(root, dirs, files))


    def search_file(self, file: str) -> bool:
        if file == True:
            return True 
        return False


    def search_filetypes():
        pass
