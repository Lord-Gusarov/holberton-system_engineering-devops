# Makes sure 2 setting are in the client SSH configuration file
$path_conf = '/etc/ssh/ssh_config'
file_line { 'Turn off passwd auth':
  path    => $path_conf,
  line    => '    PasswordAuthentication no',
  match   => '^\s*PasswordAuthentication',
}
file_line { 'Declare identity file':
  path    => $path_conf,
  line    => '    IdentityFile ~/.ssh/holberton',
  match   => '^\s*IdentityFile',
}
