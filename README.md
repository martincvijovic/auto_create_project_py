Python & bash automation tool for creating a github repo, a local repo, linking and starting vscode.

TODO : Make everything a single python script.

PREREQUISITIES: 1. webdriver for chrome / geckodriver for firefox(included in $PATH/PATH)
                2. GIT bash shell, properly set up with username and email
                3. (OPTIONAL) SSH keys linked between local machine and github account for not having to type your credentials when running the script


'INSTALLATION' : 

1) put your login credentials in py_user_pass.txt file

2) check .py file and replace the browser if not using firefox

3) replace vscode for any other editor/remove the line if not needed

4) uncomment line 48 if you want to close the automated browser upon creating the github repo

5) check the .sh file and replace my username with yours in the github repo link.

USAGE: bash project_automate.sh 'folder_name'