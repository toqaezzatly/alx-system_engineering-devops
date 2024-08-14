# 0-strace_is_your_friend.pp
# This Puppet manifest installs the missing PHP module required by WordPress

package { 'php5-mysql':
  ensure => installed,
}

service { 'apache2':
  ensure => running,
  enable => true,
  subscribe => Package['php5-mysql'],
}
