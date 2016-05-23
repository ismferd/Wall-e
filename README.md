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
and launch:
```
python "aws-name" "cloudformation"
```
This command will clean all cloudformations if there are not in "dust/cloudformation_dust"

