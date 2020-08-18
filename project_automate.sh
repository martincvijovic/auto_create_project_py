#!/bin/bash
mkdir $1
cd $1
python ../project_automate.py $1
git init
echo "THIS IS AN AUTOMATED DESCRIPTION..." >> README.md
rm geckodriver.log
git add *
git commit -m "initial commit"
git remote add origin git@github.com:martincvijovic/$1.git
git push -u origin master