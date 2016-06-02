# Wall-e(In progress)
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;![Alt text](walle.jpg?raw=true "WALL-E")

Tool for delete AWS objects... if it is not in the dustlist

##How it works:
You must have in your aws credentials your api keys like:
```
cat ~/credentials
[account aws-name]
aws_access_key_id = AKIA****************
aws_secret_access_key = ****************************************
```

###Enter into src directory
```
cd Wall-e/src/
```

###Cleaning CloudFormations:
```
python wall_e.py -a your-aws-name -r cloudformation -d dust/cloudformation_dust
```
This command will clean all cloudformations if there are not in "dust/cloudformation_dust"

###Cleaning LaunchConfigurations:
if you launch:
```
python wall_e.py -r autoscaling -a your-aws-name
```
This command clean all your launchConfigurations.