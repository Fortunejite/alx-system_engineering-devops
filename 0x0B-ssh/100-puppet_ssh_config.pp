#Using puppet to write the previous code
  
ssh::client::config { '~/.ssh/config':
  ensure => present,
}

ssh::client::host { 'ubuntu@18.235.255.210':
  user     => 'ubuntu',
  identity => '~/.ssh/school',
  password => false,
}
