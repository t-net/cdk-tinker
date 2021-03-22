#!/usr/bin/env python3
from aws_cdk import core

from cdk_tinker.cdk_tinker_stack import CdkTinkerStack


app = core.App()
CdkTinkerStack(app, "TinetteMergeTinkerStack")

app.synth()
