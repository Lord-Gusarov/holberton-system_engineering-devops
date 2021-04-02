# TASKS

### 0. Create a file
Using Puppet, create a file in /tmp.

Requirements:
* File path is /tmp/holberton
* File permission is 0744
* File owner is www-data
* File group is www-data
* File contains I love Puppet
	* File: [0-create_a_file.pp](0-create_a_file.pp)

### 1. Install a package
Using Puppet, install puppet-lint.

Requirements:
* Install puppet-lint
* Version must be 2.1.1
	* File: [1-install_a_package.pp](1-install_a_package.pp)

### 2. Execute a command
Using Puppet, create a manifest that kills a process named [killmenow](killmenow).

Requirements:
* Must use the exec Puppet resource
* Must use pkill
	* File: [2-execute_a_command.pp](2-execute_a_command.pp)
