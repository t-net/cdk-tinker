from aws_cdk import core
from aws_cdk.aws_ec2 import (
    Vpc,
    SubnetConfiguration,
    SubnetType
)

class CustomVpcStack(core.Stack):

    def __init__(self, scope: core.Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        custom_vpc = Vpc(
            self,
            "Vpc",
            max_azs=3,
            cidr="10.0.0.0/16",
            subnet_configuration=[
                SubnetConfiguration(
                    cidr_mask=24,
                    name="ingress",
                    subnet_type=SubnetType.PUBLIC
                ),
                SubnetConfiguration(
                    cidr_mask=24,
                    name="app",
                    subnet_type=SubnetType.ISOLATED
                ),
            ]
        )

        core.Tag.add(custom_vpc, "Author", "Tinette")

        core.CfnOutput(
            self,
            "Vpc",
            value=custom_vpc.vpc_id,
            export_name="custom_vpc_id"
        )
