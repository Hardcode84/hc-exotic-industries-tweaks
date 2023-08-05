import json
import os
import shutil

with open('info.json', 'r') as f:
  info = json.load(f)


name = info['name']
version = info['version']
dir_name = f'{name}_{version}'
build_dir = 'build'
full_dir_name = os.path.join(build_dir, dir_name)

print(name)
print(version)
print(dir_name)
print(full_dir_name)

exclude = ('.git', '*.zip', build_dir, dir_name)


shutil.rmtree(build_dir, ignore_errors=True)

os.mkdir(build_dir)
shutil.copytree('.', full_dir_name, ignore=shutil.ignore_patterns(*exclude), dirs_exist_ok=True)
shutil.make_archive(dir_name, 'zip', build_dir)
shutil.rmtree(build_dir)
print('done')
