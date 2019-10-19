def file_finder(dirs, file_name):
    if dirs == file_name:
        return file_name
    for a in dirs[1:]:
        path = file_finder(a, file_name)
        if path != None:
            return dirs[0]+"/"+path