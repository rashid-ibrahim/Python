class Path:
    def __init__(self, path):
        self.current_path = path

    def cd(self, new_path):
        while new_path != "":
            if len(new_path) >= 3 and new_path[0:3] == "../":
                self.current_path = self.current_path[:-2]
                new_path = new_path[3:]
            else:
                if new_path[0] == "/":
                    self.current_path += new_path[:2]
                    if len(new_path) >= 2:
                        new_path = new_path[3:]
                    else:
                        new_path = ""
                else:
                    self.current_path += "/" + new_path[:1]
                    if len(new_path) >= 1:
                        new_path = new_path[2:]
                    else:
                        new_path = ""

path = Path('/a/b/c/d')
path.cd('../x')
print(path.current_path)
path.cd('/e/f/g')
print("Final:", path.current_path)
path.cd('../../')
print("Final:", path.current_path)
path.cd('/o/p/q')
print("Final:", path.current_path)
path.cd('../j/k/../')
print("Final:", path.current_path)
