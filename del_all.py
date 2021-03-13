# This file just deletes everything you have scraped...

# Basically just think of this file as cleaning up this directory.

import os
import shutil
import colorama


def del_recs():
    deleted = []
    for content in os.listdir(os.getcwd()):
        if not content in repo_content:
            deleted.append(content)
            shutil.rmtree(content)
    
    if not deleted == []:
        for x in deleted:
            print(f'{x} has been deleted')
    else:
        print(colorama.Fore.GREEN,
            '[*] Repository is clean. Nothing to delete here.',
            colorama.Style.RESET_ALL)


if __name__ == '__main__':
    colorama.init()
    repo_content = ['img', '.git', '.gitignore', 'LICENSE', 'README.md', 'read_data.py',
                    'requirements.txt', 'search_jobs.py', 'del_all.py']
    del_recs()