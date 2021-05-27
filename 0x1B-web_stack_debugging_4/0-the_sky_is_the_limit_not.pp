# Increases the limit
exec { 'sed -i "s/ULIMIT=\"-n 15\"/ULIMIT=\"-n 5000\"/g" /etc/default/nginx':
  path => '/usr/bin:/usr/sbin:/bin',
}
-> exec {'nginx restart':
  command => '/usr/sbin/service nginx restart',
}
