import os


def find_files(suffix: str, path: str):
    """
    Find all files beneath path with file name suffix.

    Note that a path may contain further subdirectories
    and those subdirectories may also contain further subdirectories.

    There are no limit to the depth of the subdirectories can be.

    Args:
      suffix(str): suffix if the file name to be found
      path(str): path of the file system

    Returns:
       a list of paths
    """

    # base case >> if there is no more subdir
    if len(os.listdir(path)) == 0:
        return []

    # check current dir
    path_elements = os.listdir(path)
    # search target
    targets = ([os.path.join(path, file) 
                for file in path_elements 
                if file.split('.')[-1] == suffix])
                
    folders = [folder for folder in path_elements if '.' not in folder]

    # traverse child dir using recursion
    for f in folders:
        targets.extend(find_files(suffix, os.path.join(path, f)))
    
    return targets


result = find_files('c', './testdir')
print(result)