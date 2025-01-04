# All About Linux

## [Linux folder usage](https://www.debian.org/releases/buster/amd64/apcs02.en.html)

![Linux-fhs](./png/linux-fhs.png)

## File Permissions

### Umask

The umask (short for "user file creation mode mask") is a Linux/Unix system setting that determines the default permissions for newly created files and directories. It effectively "masks out" certain permission bits, preventing them from being set when new files or directories are created.

Understanding File and Directory Permissions  
In Linux, file and directory permissions are represented by three sets of bits, each corresponding to the user (owner), group, and others. These are usually represented as three digits in octal (base-8), where each digit can be a combination of:

4: Read (r)  
2: Write (w)  
1: Execute (x)

For example:

7 (4 + 2 + 1) means read, write, and execute permissions.  
6 (4 + 2) means read and write permissions.  
5 (4 + 1) means read and execute permissions.  

666 defined as read and write for everyone.

Default Permissions Before umask  
Files: The default permissions for a newly created file are usually 666 (read and write for everyone). Files do not have execute permissions by default.  
Directories: The default permissions for a newly created directory are 777 (read, write, and execute for everyone).  
How umask Works  
The umask subtracts (or masks out) permissions from these defaults. The umask value is subtracted from the default permissions to determine the actual permissions of a new file or directory.

For example:

A umask of 022 masks out the write permission for the group and others:  
Files: 666 (default) - 022 = 644 (read and write for the owner, read-only for group and others).  
Directories: 777 (default) - 022 = 755 (read, write, and execute for the owner, read and execute for group and others).

Common umask Values
022: Common default value, resulting in 755 for directories and 644 for files.  
002: Allows group members to have write permissions, resulting in 775 for directories and 664 for files.  
077: Highly restrictive, giving full access only to the owner, resulting in 700 for directories and 600 for files.  

### chmod

Chmod is use for Modify permission of file/directory

```shell
#drwxrwxrwx > rwx abbreviates as Read, Write , Delete/Execute

chmod 777 "file-name/folder-name"
```

Chown is use for providing permissions or changing the ownership to other User

```shell
#change Owner/User
chown "user-name" "file/folder-name"

#change Owner and Group
chown "user-name":"group-name" "file/folder-name"
```

Chmod [calculator](https://chmod-calculator.com/)

### Steps to Add New User

```shell
# To add user in linux
sudo adduser <user-name>  #it will ask for password enter new password

# After adding the user, you can switch to the new user's shell environment using the following command:
su - <user-name>

# after login with new user, try to execute
apt-get update #you may be get error as incident will be reported.

# update the permissions for new user, intially logout from the new user
exit

# from the root user, execute the following command
sudo visudo

# update members of the admin group

%<username> ALL=(ALL) NOPASSWD:ALL     #add this line
```

### Change host name

```shell
sudo hostnamectl set-hostname <enter-hostname>
/bin/bash
```

## Linux commands

### Mostly used commands

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
| extract files                                  | x
| list the contents of archive                   | t
| append files to existing archive               | r
| use gzip compression                           | z
| use bzip2 compression                          | j
| create tar file                                | tar cf "file-name.tar" "file/directory-name"
| extract tar file           | tar -xvf "file-name.tar"  -v: contents of tar, -f: tar filename
| compress files                   | gzip  "file-name"
| decompress files                   | gunzip "file-name"
| to update system                     | sudo apt update

### Advance Commands

| Execute                                        | Command
| ---------------------------------------------- | -------------------------------------
| send file to other system using IP add.        | scp "file-path" root@IPofothersystem:/path
| check network connectivity                     | ping google.com
| display network configure                      | ifconfig
| display network connection                     | netstat
| control system service & settings              | `systemctl`
| to start nginx | `systemctl start nginx` `systemctl status nginx` `systemctl stop nginx`
| add new user                                   | useradd "user-name"
| change password for user                       | passwd "user-name"
| switch user                                    | su
| check current user                             | whoami
| system Disk usage                              | df
| mount file system                              | sudo mount /dev/folder /mnt/folder
| check packages or app install path             | which cmake
| save terminal output to txt file               | `touch file.txt` or `ls \| tee file.txt`
| Check cPU, RAM usage                           | htop
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
|Display command history                         | history
| Print a message to the terminal                | echo
| Format and print data                          | printf
| Displays hardware information                 | lshw
| Displays information about PCI buses and devices.  | lspci
| Displays information about USB buses and devices.  | lsusb
| Displays detailed hardware information.        | hwinfo
| Displays memory usage.                         | free
| Displays system memory, processor, and I/O statistics.  | vmstat
| Displays CPU and disk I/O statistics.          | iostat
| Displays system uptime and load averages.      | uptime
| Displays the system journal.                   | journalctl
| Displays the kernel ring buffer.               | dmesg
| Schedules recurring tasks.                     | crontab
| Schedules a one-time task.                     | at
| Manages system services.                       | service
| Controls system services in systemd-based distributions.  | systemctl
| Traces the network path to a remote host.      | traceroute
| Compresses files using the bzip2 algorithm.    | bzip2
| Extracts files from a ZIP archive.             | unzip
| Redirect output to multiple files              | tee
| Change the root directory for a process        | chroot
| Display information about all running processes  | ps aux
| Display file contents in a paginated format    | less
| Display file contents one page at a time       | more
| Create links between files                     | ln
| Print the resolved absolute path of a file     | realpath
| Execute a command periodically and display the output  | watch
| Display a calendar                             | cal
| Extract files from a compressed archive        | tar -xzvf
| Create a compressed archive                    | tar -czvf
| Locate the binary, source, and manual page files for a command  | whereis
| Find files by name                             | locate
| Display the full path to an executable         | which

### Other commands

- Clean up the packages:
  
`rm -rf /var/lib/apt/lists/*` - This command used to clean up the package list cache after installing packages, especially in Docker, to reduce image size.

Advantages: Reduces image size and keeps environments clean.

Disadvantages: Deletes package metadata, requiring you to run apt-get update again before installing or upgrading packages. Not suitable for long-running environments where package management might be needed later.

- dev/null

In Linux, /dev/null is a special device file known as the "null device" or "null file." It discards anything written to it and immediately returns an end-of-file (EOF) to any process that reads from it. You can think of /dev/null as a "black hole" for data—it simply deletes anything sent to it. This can be useful in several scenarios, especially when you want to suppress output/error or ignore specific data streams.

Common Uses of /dev/null:

1. Suppress Command Output.  
    You may want to run a command without displaying any output. By redirecting the output to /dev/null, you effectively ignore it.

    Example: Suppresses standard output

    ```bash
    ls > /dev/null
    ```

    In this example, ls would normally list directory contents, but by redirecting > it to /dev/null, the output is discarded and not shown in the terminal.

2. Suppress Error Messages.  

    Sometimes, you only want to discard error messages, which are typically directed to the standard error (stderr) stream (file descriptor 2).

    Example: Suppresses only the error output  

    ```bash
    ls nonexistentfile 2> /dev/null
    ```

    This command tries to list a file that doesn’t exist. Normally, it would produce an error message, but by redirecting 2> to /dev/null, you discard only the error output and keep the standard output unaffected.

3. Suppress All Output (Standard and Error)

    In some cases, you may want to suppress both standard output and error messages from a command.

    Example: Suppresses both standard output and error output  

    ```bash
    ls nonexistentfile > /dev/null 2>&1
    ```

    Here, > redirects standard output, and 2>&1 redirects standard error to the same place as standard output, which is now /dev/null. This effectively hides all output from ls, including any error messages.

4. Run Command in Background Without Output

    When running a command in the background, the output can clutter the terminal. Sending output to /dev/null avoids this.

    Example: Runs `ping` in the background without showing output

    ```bash
    ping -c 4 google.com > /dev/null 2>&1 &
    ```

    This runs ping in the background for 4 packets, discarding all output, so you won’t see any results or messages in the terminal.

5. Check if a File or Directory Exists Without Output

    Sometimes, you only need to check if a file or directory exists without producing any output. /dev/null helps here by discarding the output of the command.

    Example:

    ```bash
    # Checks if a file exists without output
    if ls /path/to/file > /dev/null 2>&1; then
        echo "File exists."
    else
        echo "File does not exist."
    fi
    ```

    In this example, ls checks if the file exists. If it does, the script echoes "File exists." If not, it says "File does not exist." The command's output is sent to /dev/null, so you don’t see anything unless there is a specific message in the if or else statement.

    Summary  
    Suppress command output: command > /dev/null  
    Suppress error messages: command 2> /dev/null  
    Suppress both output and error: command > /dev/null 2>&1  
    Run in background without output: command > /dev/null 2>&1 &
