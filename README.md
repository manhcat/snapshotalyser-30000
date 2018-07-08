# snapshotalyser-30000
A demo project to manage AWS EC2 instance snapshots

# Configuring

shotty uses the Configuration file created by
AWS cli. e.g.
'aws configure --profile shotty'

#Running

'pipenv run python .\shotty\shotty.py <command> <--project=PROJECT>'

"command" is instances, volumes or snapshots
"subcommand" is depends on command
"project" is optional
