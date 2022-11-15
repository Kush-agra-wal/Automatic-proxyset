# Automatic-proxyset
Enable proxy in Windows automatically when connected to specific network and disable when connected to any other network

To set this first download the python file in repo and in the python file change values of username to your roll number ~~joe~~ and password of your LDAP ~~mama~~ and save.

Steps to make the python file run automatically when you connect to a network in WINDOWS

(1) Open "Task Scheduler" in Windows.

(2) Go to Action -> Creat Task.

(3) Give any random name to your task.

(4) Go to Triggers -> New.

(5) Change Begin the task option to "On an event".

(6) From dropdown menu in Log select "Microsoft-Windows-NetworkProfile/Oprational" and Source as "NetworkProfile".

(7) Set Event ID as 10000 and press Ok.

(8) Go to Actions -> New -> Action = Start a program and browse the location of python file in the repositry and press Ok.

(9) Change Conditions as per your requirments and after all this press ok to save the Scheduled task.

This runs the python file everytime you connect to a network and enable proxy accordingly.

# will make it easy for your lazy a**.
