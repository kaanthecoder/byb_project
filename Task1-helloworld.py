'''
1. Login to GitHub using your account.
2. Create a new repository named "byb_project" and ensure it's set to public.
3. Create an empty folder named "byb_project" on your local machine.
4. Open your terminal or command prompt and navigate to the newly created folder.
5. Initialize a new Git repository using the command `git init`.
6. Check the status of the repository with `git status` to ensure a clean working directory.
7. Create a new file named "helloWorld.py" or "helloWorld.js" inside the "byb_project" folder and write a program that prints "Hello World!".
8. Check the status again with `git status`, and you should see the new file listed as untracked.
9. Add the new file to the staging area using `git add helloWorld.py`.
10. Check the status again to confirm that the file is now tracked and staged.
11. Modify the content of "helloWorld.py" to print "Git is Awesome!".
12. Check the status again to see that the file is now listed under "Changes not staged for commit".
13. Stage the modified file again with `git add helloWorld.py`.
14. Commit your changes with `git commit -m "Your commit message"`.
15. Verify the status to ensure a clean working directory.
16. Open your terminal or command prompt, navigate to the "byb_project" folder.
17. Add your GitHub repository as a remote using `git remote add [remote-name] [url]`, replacing `[remote-name]` with any name you choose, and `[url]` with the URL of your GitHub repository.
18. Push your local repository to the remote repository using `git push -u [remote-name] master`, replacing `[remote-name]` with the name you assigned in the previous step.
19. Make sure the repository is public on GitHub.
20. Add the link to your GitHub repository to your Google answers doc, indicating that it's for the Compulsory section. '''

#1. Navigate to the folder where you want to create the project:

cd path/to/parent/folder

#2. Initialize a new Git repository:

git init

#3. Create a new file named "helloWorld.py" and write the program:

#For Python:

echo 'print("Hello World!")' > helloWorld.py

#For JavaScript:

echo 'console.log("Hello World!");' > helloWorld.js

#4. Add the file to the staging area:

git add helloWorld.py   # If you chose Python

or
git add helloWorld.js   # If you chose JavaScript

#5. Commit your changes:

#git commit -m "Initial commit"

#6. Modify the content of the file:

echo 'print("Git is Awesome!")' > helloWorld.py   # If you chose Python

or

echo 'console.log("Git is Awesome!");' > helloWorld.js   # If you chose JavaScript

#7. Add the modified file to the staging area:

git add helloWorld.py   # If you chose Python

or

git add helloWorld.js   # If you chose JavaScript


#8. Commit your changes again:

git commit -m "Updated helloWorld.py"

#9. Add your remote repository:

git remote add origin [your_repository_url]

#10. Push your changes to GitHub:

git push -u origin master

