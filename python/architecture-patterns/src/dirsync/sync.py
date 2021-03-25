import hashlib
import os
import shutil
from pathlib import Path
from dirsync.hashing import hash_file


def read_paths_and_hashes(root):
    hashes={}
    for folder,_,files in os.walk(root):
        for file in files:
            key =hash_file(Path(folder).joinpath(file))
            hashes[key]=file
    return hashes

def determine_actions(src_hashes,dest_hashes,src_folder,dest_folder):
    for sha,filename in src_hashes.items():
        if sha not in dest_hashes:
            source_path=Path(src_folder).joinpath(filename)
            dest_path=Path(dest_folder).joinpath(filename)
            yield 'copy',source_path,dest_path
            
        elif dest_hashes[sha] !=filename:
            old_path=Path(dest_folder).joinpath(dest_hashes[sha])
            new_path=Path(dest_folder).joinpath(filename)
            yield 'move',old_path,new_path
            
    for sha,filename in dest_hashes.items():
        if sha not in src_hashes:
            yield 'delete',Path(dest_folder).joinpath(filename)

def sync(source,dest):
    source_hashes=read_paths_and_hashes(source)
    dest_hashes=read_paths_and_hashes(dest)
    #keep track of the files filenames and hashes
    
    actions=determine_actions(source_hashes,dest_hashes,source,dest)
    #walk the target folder and get the filenames and hashes
    
    for action,*paths in actions:
        if action=='copy':
            shutil.copyfile(*paths)
        if action=='move':
            shutil.move(*paths)
        if action == 'delete':
            os.remove(paths[0])
    # for folder,_,files in os.walk(dest):
    #     for dest_file in files:
    #         dest_path=Path(folder).joinpath(dest_file)
    #         dest_hash=hash_file(dest_path)
    #         seen.add(dest_hash)
            
    #         #if there's a file in target that has not in source, delete it
    #         if dest_hash not in source_hashes:
    #             os.remove(dest_path)
    #         elif dest_hash in source_hashes and dest_path!=source_hashes[dest_hash]:
    #             shutil.move(dest_path,Path(folder).joinpath(source_hashes[dest_hash]))

    # for src_hash,file in source_hashes.items():
    #     if src_hash not in seen:
    #         source_file_path=Path(source).joinpath(file)
    #         dest_file_path=Path(dest).joinpath(file)
    #         shutil.copy(source_file_path,dest_file_path)