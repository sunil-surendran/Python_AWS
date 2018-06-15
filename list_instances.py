#!/usr/bin/python

import boto3

ec2 = boto3.resource('ec2')
for instances in ec2.instances.all():
	print instances.id, instances.state
