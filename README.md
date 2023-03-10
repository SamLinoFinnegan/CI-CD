# My Project

To complete this task, working with an SSH key was essential.
Although I had not used one before, I now understand that it is a secure method of authentication.
I used the SSH key to connect to both the Digital Ocean server and GitHub.
I also learned how to use GitHub Actions, which was new to me.
It took some time to grasp the YAML syntax, but it was helpful in triggering a set of actions on a certain GitHub event, such as a push.

To ensure the security of my private information, including the SSH keys and server information for Digital Ocean, I used GitHub secrets.
This method stores and encrypts my data, which can be accessed through variables in GitHub Actions.

I encountered some challenges during this project.
Initially, I had some trouble setting up pytest and getting it to work, I resolved this by adding pytest to the reqirements file and installing it.
I also struggled with the workflow logic. By default, several actions run simultaneously, but I only wanted to update the files on the server if the tests passed.
To achieve this, I used 'needs: run-tests' in my deploy action.

The most significant problem I faced was connecting to the Digital Ocean server with the SSH keys.
I didn't know that in order to use SSH keys you must declare them at the time of creating the server.
After trying several solutions, I ended up starting over with a new droplet and creating a new SSH key.
While not the most elegant solution, it did resolve the issue.
