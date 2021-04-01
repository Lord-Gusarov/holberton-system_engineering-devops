## Learning Objectives
At the end of this project, you are expected to be able to explain to anyone, without the help of Google:

## General
* What is a server
* Where servers usually live
* What is SSH
* How to create an SSH RSA key pair
* How to connect to a remote host using an SSH RSA key pair
* The advantage of using #!/usr/bin/env bash instead of /bin/bash

# TASKS

### 0. Use a private key
Write a Bash script that uses ssh to connect to your server using the private key ~/.ssh/holberton with the user ubuntu.
* Only use ssh single-character flags
* You cannot use -l
* You do not need to handle the case of a private key protected by a passphrase
	* File: [0-use_a_private_key](0-use_a_private_key)

### 1. Create an SSH key pair
Write a Bash script that creates an RSA key pair.
* Name of the created private key must be holberton
* Number of bits in the created key to be created 4096
* The created key must be protected by the passphrase betty
	* File: [1-create_ssh_key_pair](1-create_ssh_key_pair)

### 2. Client configuration file
Your Ubuntu Vagrant machine has an SSH configuration file for the local SSH client, let’s configure it to our needs so that you can connect to a server without typing a password. Share your SSH client configuration in your answer file.
* Your SSH client configuration must be configured to use the private key ~/.ssh/holberton
* Your SSH client configuration must be configured to refuse to authenticate using a password
	* File: [2-ssh_config](2-ssh_config)

### 3. Let me in!
Now that you have successfully connected to your server, we would also like to join the party.
Add the SSH public key below to your server so that we can connect using the ubuntu user.
```
ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQDNdtrNGtTXe5Tp1EJQop8mOSAuRGLjJ6DW4PqX4wId/Kawz35ESampIqHSOTJmbQ8UlxdJuk0gAXKk3Ncle4safGYqM/VeDK3LN5iAJxf4kcaxNtS3eVxWBE5iF3FbIjOqwxw5Lf5sRa5yXxA8HfWidhbIG5TqKL922hPgsCGABIrXRlfZYeC0FEuPWdr6smOElSVvIXthRWp9cr685KdCI+COxlj1RdVsvIo+zunmLACF9PYdjB2s96Fn0ocD3c5SGLvDOFCyvDojSAOyE70ebIElnskKsDTGwfT4P6jh9OBzTyQEIS2jOaE5RQq4IB4DsMhvbjDSQrP0MdCLgwkN
```

# ADVANCED TASK

### 4. Client configuration file (w/ Puppet)
Let’s practice using Puppet to make changes to our configuration file. Just as in the previous configuration file task, we’d like you to set up your client SSH configuration file so that you can connect to a server without typing a password.
* Your SSH client configuration must be configured to use the private key ~/.ssh/holberton
* Your SSH client configuration must be configured to refuse to authenticate using a password
	* File: [100-puppet_ssh_config.pp](100-puppet_ssh_config.pp)
