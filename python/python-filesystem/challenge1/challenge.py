import os,pathlib

ospath_log_path=""
ospath_old_log_path=""
another_join_path=""
another_join_new_path=""

def ospath_get_path(input_file,input_old_file):
    global ospath_log_path,ospath_old_log_path
    ospath_log_path=os.path.join(os.getcwd(),input_file)
    ospath_old_log_path=os.path.join(os.path.dirname(ospath_log_path),input_old_file)

def pathlib_get_path(input_file,input_old_file):
    path_lib=pathlib.Path()
    global another_join_path,another_join_new_path
    join_path=path_lib.joinpath(path_lib.cwd(),input_file)
    another_join_path=join_path.absolute().as_posix()
    join_new_path=path_lib.joinpath(join_path.parent,input_old_file)
    another_join_new_path=join_new_path.absolute().as_posix()

