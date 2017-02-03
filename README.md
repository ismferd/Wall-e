[![Build Status](https://travis-ci.org/ismFerDev/Wall-e.svg?branch=master)](https://travis-ci.org/ismFerDev/Wall-e)
# Wall-e(In progress)
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;![Alt text](walle.jpg?raw=true "WALL-E")

Tool for clean AWS objects...
## Install
```
pip install wall-e
```
```
pip install git+https://git@github.com/ismFerDev/Wall-e.git
```

## How it works:
You must have in your aws credentials your api keys like:

```
cat ~/credentials
[account aws-name]
aws_access_key_id = AKIA****************
aws_secret_access_key = ****************************************
```

### Enter into src directory
```
cd Wall-e/src/
```

### Cleaning CloudFormations:
```
wall-e -a your-aws-name -r cloudformation -d dust/cloudformation_dust
```

This command will clean all cloudformations if there are not in "dust/cloudformation_dust"

### Cleaning LaunchConfigurations:
if you launch:

```
python wall-e.py -r autoscaling -a your-aws-name
```
This command clean all your launchConfigurations.

### Cleaning your instances:
You must have tagged your instance with tag:Name.

and Run:

```
python cli.py -r ec2 -t tag_name1 tag_name2 tag_name3 -a aws_account
```

You will delete all instance not tagged with tag_name1 tag_name2 tag_name3

### Cleaning your snapshots:
You must specify how many days you want to retain.

and Run:

```
python wall-e.py -r snapshot -D days -a aws_account
```

You will delete all snapshots older than days
You will delete all instance not tagged with tag_name1 tag_name2 tag_name3 
