import os
from pathlib import Path
cur_path=Path()
print(list(cur_path.iterdir()))

new_path =cur_path.joinpath(cur_path.parent).absolute()
print(list(new_path.iterdir()))

print(list(cur_path.glob("*.tmp")))
print(list(cur_path.glob("?.tmp")))
print(list(cur_path.glob("[0-9].tmp")))

old_path=Path(cur_path.joinpath(cur_path.cwd(),'registry.bkp'))
new_path=Path('registry.bkp.old')
with old_path.open('w') as new_file:
    new_file.write("test")
    print(f'create test file :{old_path.absolute()}')
old_path.rename(new_path)
print(f'{old_path.absolute()} rename to {new_path}')
print(list(cur_path.iterdir()))
remove_path=Path('registry.bkp.old')
remove_path.unlink()
print(f'{remove_path.absolute()} revmoved')
print(list(cur_path.iterdir()))

new_dir_path =Path("testDir")
new_dir_path.mkdir()
print(list(new_dir_path.iterdir()))
print(new_dir_path.is_dir())
new_dir_path.rmdir()

new_sub_dir_path=Path(os.path.join('d1','d2'))
new_sub_dir_path.mkdir(parents=True)
new_sub_dir_path.rmdir()