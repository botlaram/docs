### Linux Directory usage:

- Linux folder usage detail [link](https://www.debian.org/releases/buster/amd64/apcs02.en.html)

### Basic Permissions

#### chmod
  Change the permissions of a file or directory in Linux. The command `chmod` is used to change the mode (permissions)

  ```
  drwxrwxrwx > rwx abbrevates as Read, Write , Delete/Execute

  It contains Owner, Group, Public
  note: d define as Dir / f define as File
  

  r:read=4 / w:write=2 / x:execute=1
    
  + add / - remove  / = assign

  User(owner)=u / Group(Usergroup)=g / Other(All user in systm)=o / All=a
  ```  

  - let go through example (using simple method):  
  
    1. If we want to add Owner with execute permissions and group/user with write permission  
    ```chmod o+x,g+w,o+w "file_name.ext" / chmod o+x,go+w "file_name.ext"```  

    2. for removing permissions  
    ```chmod g-w,o-w "filename.ext"```

    3. using assign symbol (i.e "=")  
    ```chmod u=rw,g=r,o=r "filename.ext```

    4. add permissions for all (here a=All)  
    ```chmod ugo=rwx "filename.ext" / chmod a=rwx "filename.ext"```

    5. add permissions for whole dir using -r (recursive)  
    ```chmod -R 700 "foldername"```

  - let go through example (using Binary method):  
  
    1. If we want to add Owner with all permissions and group with read&execute permission , user with read permissions   
    ```chmod 754 "file_name.ext"```  

    2. Only read permissions for Owner  
    ```chmod 400 "file_name.ext"```  


#### chown/chgrp
  changing the ownership/group of the file  

  - let go through example:  
  
    1. change the owner / grp name   
  ```chown "name" "filename.ext"  /  chgrp "groupname" "filename.ext"```

    2. change owner:group at same
  ```chown "name":"name" "filename.ext/foldername"```

#### chmod Calculator

- [calculator](https://chmod-calculator.com/) 

### Linux commands

| Execute                                        | Command
| ---------------------------------------------- | ------------------------------------------------
| check current user                             | `whoami`
| for Help command                               | man "ls", man "mkdir"
| Change directory                               | cd                                              
| List directory contents                        | ls                                              
| Print working directory                        | pwd                                             
| Create a new directory                         | `mkdir "dir-name"`                  
| Remove an empty directory                      | rmdir "dir-name"
| Delete directory                               | rm -r "dir-name"  
| Remove files                                   | rm "file-name"
| Delete files using extension                   | `rm *.txt | rm /path/to/directory/*.txt`
| Copy Files                                     | cp "source_path" "destination path"
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
| send file to other system using IP add.         | `scp "file-path" root@IPofothersystem:/path`
| check network connectivity           | `ping google.com`
| display network configure   | `ifconfig`
| display network connection             | `netstat`
| control system service & settings     | `systemctl`
| to start nginx | `systemctl start nginx` `systemctl status nginx` `systemctl stop nginx`
| add new user                  | `useradd "user-name"`
| change password for user          | `passwd "user-name"`
| switch user          | `su`
| system Disk usage |` df `
| mount file system           | `sudo mount /dev/folder /mnt/folder`
| check packages or app install path  | `which cmake`
| save terminal output to txt file | `touch file.txt` `ls | tee file.txt`
| Check cPU, RAM usage  | `htop`