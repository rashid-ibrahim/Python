class FileOwners:

    @staticmethod
    def group_by_owners(files):
        groupDict = {}
        for item in files:
            if files[item] in groupDict:
                groupDict[files[item]].append(item)
            else:
                groupDict[files[item]] = []
                groupDict[files[item]].append(item)
        return groupDict

files = {
    'Input.txt': 'Randy',
    'Code.py': 'Stan',
    'Output.txt': 'Randy'
}
print(FileOwners.group_by_owners(files))
