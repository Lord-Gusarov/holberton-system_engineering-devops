# Makes sure 2 setting are in the client SSH configuration file
file_line { 'Turn off passwd auth':
  path => '/etc/ssh/ssh_config'
  line => '    IdentityFile ~/.ssh/holberton'
}
file_line { 'Declare identity file':
  path => '/etc/ssh/ssh_config'
  line => '    PasswordAuthentication no'
}
