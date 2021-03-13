# This file just deletes everything you have scraped...

# Basically just think of this file as cleaning up this directory.

import os
import shutil


def del_recs():
    # This walk block is just an anxiety control, to make sure not all dependencies don't get deleted by this file
    repo_content = []
    for root, dirs, files in os.walk(os.getcwd()):
        for dir in dirs:
            for folder in repo_folders:
                if folder == dir:
                    #print(f'{folder} is a folder in the repo')
                    repo_content.append(folder)
        for f in files:
            for file in repo_files:
                if file == f:
                    #print(f'{file} is file in the repo')
                    repo_content.append(file)
    
    #print(f'{len(repo_content)} total content')

    deleted = []
    for content in os.listdir(os.getcwd()):
        if content in repo_content:
            continue
            #print(f'{content} will not get deleted')
        else:
            deleted.append(content)
            shutil.rmtree(content)
    
    for x in deleted:
        print(f'{x} has been deleted')


if __name__ == '__main__':
    repo_files = ['.gitignore', 'LICENSE', 'README.md', 'read_data.py',
                    'requirements.txt', 'search_jobs.py', 'del_all.py']
    repo_folders = ['img', '.git']

    del_recs()