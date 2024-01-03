
### Document for Linux Directory usage:

[Linux folder usage](https://www.debian.org/releases/buster/amd64/apcs02.en.html)

### Chmod

`drwxrwxrwx > rwx abbrevates as Read, Write , Delete/Execute`

 - Chmod is use for Modify permission of file/directory. 
   - syntax `chmod 777 "file-name/folder-name"`


 - Chown is use for providing permissions or changing the ownership to other User
   - syntax to change Owner/User `chown "user-name" "file/folder-name"`
   - to change Owner and Group `chown "user-name":"group-name" "file/folder-name"`

### Add User
 - to add user in linux
   - syntax `sudo adduser <user-name>`  #it will ask for password enter new password
 
 - switch to new user
   - syntax `su - <user-name>`  
 
 - after login with new user
   - try to execute `apt-get update` #you may be get error as incident will be reported.
 
 - update the permissions for new user
   - `exit`  #logout from the new user
 
 - for the root user
   - `sudo visudo`
   - update members of the admin group
     - `%<username> ALL=(ALL) NOPASSWD:ALL`     #add this line


It contains Owner, Group, Public

#### chmod [calculator](https://chmod-calculator.com/) 

### Linux commands

| Execute                                        | Command
| ---------------------------------------------- | ------------------------------------------------
| for Help command                               | man "ls", man "mkdir"
| Change directory                               | cd                                              
| List directory contents                        | ls                                              
| Print working directory                        | pwd                                             
| Create a new directory                         | mkdir "dir-name"                                
| Remove an empty directory                      | rmdir "dir-name"
| Delete directory                               | rm -r "dir-name"  
| Remove files                                   | rm "file-name"
| Concatenate and display files                  | cat "file-name"                                 
| Create an empty file                           | touch "file-name"                               
| create file with adding content                | vim "file-name"                                    
| Vim command      | to write use `i` as insert, to save `ESC : wq`, to save without editing `ESC : q!`
| Move or rename files and directories            | mv "file-name" "dir-name"/"file-name" 
| Copy file to new file                | cp "file-name1" "file-name2"                                 
| Copy file to other folder             | cp "file-name1" "dir-name"/"file-name1"           
| Modify Permission of file/dir           | chmod "777" "file/dir-name"
| Change ownership of file/dir           | chown "user-name" "file/dir-name"
| Change ownership & group for file/dir           | chown "user-name":"grp-name" "file/dir-name"

### Tar Commands

| Execute                                        | Command
| ---------------------------------------------- | ------------------------------------------------
| for Help command                               | man "tar"
| extract files                         | x                             
| list the contents of archive           | t                               
| append files to existing archive         | r                            
| use gzip compression                    | z                              
| use bzip2 compression                             | j                               
| create tar file             | tar cf "file-name.tar" "file/directory-name"                           
| extract tar file               | tar -xvf "file-name.tar"  -v: contents of tar, -f: tar filename                      
| compress files                   | gzip  "fil-ename"
| decompress files                   | gunzip "file-name"  
| to update system                     | sudo apt update

### Advance Commands

| Execute                                        | Command
| ---------------------------------------------- | ------------------------------------------------
| send file to other system using IP add.         | scp "file-path" root@IPofothersystem:/path
| check network connectivity           | ping google.com
| display network configure   | ifconfig
| display network connection             | netstat
| control system service & settings     | `systemctl`
| to start nginx | `systemctl start nginx` `systemctl status nginx` `systemctl stop nginx`
| add new user                  | useradd "user-name"
| change password for user          | passwd "user-name"
| switch user          | su
| check current user   | whoami
| system Disk usage | df 
| mount file system           | sudo mount /dev/folder /mnt/folder
| check packages or app install path  | which cmake
| save terminal output to txt file | `touch file.txt` `ls | tee file.txt`
| Check cPU, RAM usage  | htop




|cut                                             | Cut out sections of a file
|gzip                                            | Compress or decompress files using gzip
|gunzip                                          | Decompress files compressed with gzip
|find                                            | Find files and directories matching a pattern
|grep                                            | Search for a pattern in a file
|awk                                             | Pattern scanning and processing language
|sed                                             | Stream editor for filtering and transforming text
|head                                            | Display the first few lines of a file
|tail                                            | Display the last few lines of a file
|sort                                            | Sort lines of a file
|uniq                                            | Remove duplicate lines from a file
|wc                                              | Count lines, words, and characters in a file
|diff                                            | Compare two files line by line
|patch                                           | Apply a patch to a file
|chmod                                           | Change permissions of files and directories
|chown                                           | Change the owner of a file or directory
|chgrp                                           | Change the group ownership of a file or directory
|ps                                              | List running processes
|top                                             | Display system resource usage and process information
|kill                                            | Send a signal to a process to terminate it
|du                                              | Display disk usage of files and directories
|df                                              | Display free disk space on the file system
|mount                                           | Mount a file system
|umount                                          | Unmount a file system
|ping                                            | Test connectivity to a network host
|ssh                                             | Secure shell remote login and command execution
|scp                                             | Secure copy files between hosts
|rsync                                           | Remote file and directory synchronization
|curl                                       | Transfer data from or to a server using various protocols
|wget                                       | Retrieve files from the web using various protocols
|ftp                                             | File Transfer Protocol client
|sftp                                            | Secure File Transfer Protocol client
|telnet                                          | Telnet client
|nslookup                                        | DNS lookup utility
|dig                                             | DNS lookup utility
|netstat                                         | Display network connections and statistics
|ifconfig                                        | Configure network interfaces
|route                                           | Display or modify the routing table
|iptables                                        | Firewall and packet filtering utility
|hostname                                        | Display or set the hostname of the system
|date                                            | Display or set the system date and time
|timedatectl                                     | Control the system date and time
|uname                                           | Display system information
|whoami                                          | Display the current user ID
|id                                              | Display user and group information
|su                                              | Switch user to become another user
|sudo                                            | Execute a command with superuser privileges
|passwd                                          | Change the password of a user account
|useradd                                         | Create a new user account
|userdel                                         | Delete a user account
|usermod                                         | Modify a user account
|groupadd                                        | Create a new group
|groupdel                                        | Delete a group
|groupmod                                        | Modify a group
|finger                                          | Display information about users on the system
|last                                            | Display information about recent logins

history — Display command history
echo — Print a message to the terminal
printf — Format and print data
lshw — Displays hardware information
lspci — Displays information about PCI buses and devices.
lsusb — Displays information about USB buses and devices.
hwinfo — Displays detailed hardware information.
free — Displays memory usage.
vmstat — Displays system memory, processor, and I/O statistics.
iostat — Displays CPU and disk I/O statistics.
uptime — Displays system uptime and load averages.
journalctl — Displays the system journal.
dmesg — Displays the kernel ring buffer.
crontab — Schedules recurring tasks.
at — Schedules a one-time task.
service — Manages system services.
systemctl — Controls system services in systemd-based distributions.
traceroute — Traces the network path to a remote host.
bzip2 — Compresses files using the bzip2 algorithm.
unzip — Extracts files from a ZIP archive.
tee — Redirect output to multiple files
chroot — Change the root directory for a process
ps aux — Display information about all running processes
less — Display file contents in a paginated format
more — Display file contents one page at a time
ln — Create links between files
realpath — Print the resolved absolute path of a file
watch — Execute a command periodically and display the output
cal — Display a calendar
tar -xzvf — Extract files from a compressed archive
tar -czvf — Create a compressed archive
whereis — Locate the binary, source, and manual page files for a command
locate — Find files by name
which — Display the full path to an executable
