from config import SYMSYNC_SETTINGS
import os.path
from pathlib import Path

def main():
    for s in SYMSYNC_SETTINGS:

        target_full_path = s['target'] + s['name']
        source_full_path = s['source'] + s['name']

        target_dir_exists = os.path.exists(s['target'])
        source_dir_exists = os.path.exists(s['source'])
        target_file_exists = os.path.exists(target_full_path)
        source_file_exists = os.path.exists(source_full_path)


        if source_file_exists:

            if not target_file_exists:
                os.makedirs(s['target'], exist_ok=True)
                Path(target_full_path).touch()
                target_file_exists = os.path.exists(target_full_path)

            if target_file_exists:
                os.remove(target_full_path)

            os.symlink(source_full_path, target_full_path)
            print('Successfully created symlink: ' + source_full_path + ' --> ' + target_full_path)


        # if source_file_exists:
        #     if not target_file_exists:
        #         os.makedirs(s['target'], exist_ok=True)
        #     os.remove(s['target'])
        #     os.symlink(s['source'], s['target'])
        #     print('symlink success')
        # else:
        #     print('ERROR: source file: ' + s['source'] + ' does not exist.')


if __name__ == "__main__":
    main()

