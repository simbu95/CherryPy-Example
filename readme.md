Steps...

Download Python: https://www.python.org/downloads/

During install, make sure to include in path environment variables.

After install, open up a shell (cmd or powershell on windows) and enter 'python' if that isn't recognized... try 'python3'. If successful, you should enter the python shell.

If failed, attempt installation again.

To exit the shell, you need to enter a certain command that changes based on version... usually quit or quit() will work... also ctrl+d or ctrl+z tend to work.

Next is package management. The one used in for this repo is cherrypy, so try 'pip install cherrypy'. 

Once cherrypy is installed, you can run the python script by typing 'python scriptname.py' in this case python example.py

This python script creates a cherrypy webserver using the index.html file in the folder, and serves it to any hosts. to check on your local computer, type localhost into your web browser.
