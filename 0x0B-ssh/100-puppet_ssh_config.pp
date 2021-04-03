# Makes sure 2 setting are in the client SSH configuration file
exec { 'Turn off passwd auth':
  path    => '/bin',
  command => "echo 'PasswordAuthentication no' >> /etc/ssh/ssh_config"
}
exec { 'Declare identity file':
  path    => '/bin',
  command => "echo 'IdentityFile ~/.ssh/holberton' >> /etc/ssh/ssh_config",
}
