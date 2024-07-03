# Ensure the SSH config directory exists
file { '/home/ubuntu/.ssh':
  ensure => 'directory',
  owner  => 'ubuntu',
  group  => 'ubuntu',
  mode   => '0700',
}

# Ensure the SSH config file exists
file { '/home/ubuntu/.ssh/config':
  ensure  => 'file',
  owner   => 'ubuntu',
  group   => 'ubuntu',
  mode    => '0600',
  content => '',
}

# Add or replace the Host configuration
file_line { 'Host myserver':
  ensure => present,
  path   => '/home/ubuntu/.ssh/config',
  line   => 'Host myserver',
}

# Add or replace the HostName configuration
file_line { 'HostName 100.26.11.179':
  ensure => present,
  path   => '/home/ubuntu/.ssh/config',
  line   => '    HostName 100.26.11.179',
  match  => '^\\s*HostName\\s+.*',
  append_on_no_match => true,
}

# Add or replace the User configuration
file_line { 'User ubuntu':
  ensure => present,
  path   => '/home/ubuntu/.ssh/config',
  line   => '    User ubuntu',
  match  => '^\\s*User\\s+.*',
  append_on_no_match => true,
}

# Add or replace the IdentityFile configuration
file_line { 'IdentityFile ~/.ssh/school':
  ensure => present,
  path   => '/home/ubuntu/.ssh/config',
  line   => '    IdentityFile ~/.ssh/school',
  match  => '^\\s*IdentityFile\\s+.*',
  append_on_no_match => true,
}

# Add or replace the PasswordAuthentication configuration
file_line { 'PasswordAuthentication no':
  ensure => present,
  path   => '/home/ubuntu/.ssh/config',
  line   => '    PasswordAuthentication no',
  match  => '^\\s*PasswordAuthentication\\s+.*',
  append_on_no_match => true,
}

