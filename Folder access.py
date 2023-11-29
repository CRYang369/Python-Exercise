class FolderAccess:
    def __init__(self, folders, access):
        self.folders = folders
        self.access = access

    def has_access(self, folder_name):
        access_set = set(self.access)

        def is_accessible(folder_name):
            # If the folder is in the access set, return True
            if folder_name in access_set:
                return True

            # If the folder has a parent, recursively check its parent
            for folder, parent in self.folders:
                if folder == folder_name and parent is not None:
                    return is_accessible(parent)

            return False

        return is_accessible(folder_name)

# Test cases
folders_data = [
    ('A', None),
    ('B', 'A'),
    ('C', 'B'),
    ('D', 'B'),
    ('E', 'A'),
    ('F', 'E')
]

access_data = ['C', 'E']

folder_access = FolderAccess(folders_data, access_data)

print(folder_access.has_access("B"))  # Output: False
print(folder_access.has_access("C"))  # Output: True
