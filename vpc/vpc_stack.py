from aws_cdk import  (
    aws_ec2 as ec2,
    aws_cloudformation as cloudformation,
    core
)


class VpcStack(core.Stack):

    def __init__(self, scope: core.Construct, id: str, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)

        # create defalut vpc (us-east-1)
        # 1 VPC
        # 2 PublicSubnet, 2 Private Subnet
        # 4 Route Table, Each subnet will get each route table
        # Private Route Table will attach NATGateway (2 NATGateway, 2 EIP)
        # Public Route Table will attach InternetGateway
        # vpc = ec2.Vpc(self, "Mindy-VPC")

        #############################
        # VPC
        #############################
        # https://docs.aws.amazon.com/cdk/api/latest/python/aws_cdk.aws_ec2/Vpc.html

        subnet_amount = 2
        subnet_list = []
        
        # public subnet
        public_subnet = ec2.SubnetConfiguration(
            name = 'My-Public', 
            subnet_type = ec2.SubnetType.PUBLIC, 
            cidr_mask=24
        )
        subnet_list.append(public_subnet)
        
        # private subnet
        # private_subnet = ec2.SubnetConfiguration(
        #     name = 'My-Private', 
        #     subnet_type = ec2.SubnetType.PRIVATE, 
        #     cidr_mask=24
        # )
        # subnet_list.append(private_subnet)

        # vpc setting
        VPC_id = 'My Lab VPC'
        CIDR = '10.0.0.0/16'
        vpc = ec2.Vpc(
            self,
            VPC_id,
            cidr=CIDR,
            max_azs=subnet_amount,
            nat_gateways=0, 
            nat_gateway_subnets=None, 
            subnet_configuration=subnet_list, 
            vpn_connections=None, 
            vpn_gateway=None, 
            vpn_gateway_asn=None, 
            vpn_route_propagation=None
            )
        
        # output 
        core.CfnOutput(
            self, 
            'VPC-CIDR', 
            value=vpc.vpc_cidr_block
        )
        core.CfnOutput(
            self, 
            'VPC-id', 
            value=vpc.vpc_id
        )
        
        for i in range(len(vpc.availability_zones)):
            core.CfnOutput(
                self, 
                'VPC-AZ-%s'%(i+1), 
                value=vpc.availability_zones[i]
            )
        
        for i in range(len(vpc.public_subnets)):
            core.CfnOutput(
                self, 
                'VPC-Public-Subnet-%s'%(i+1), 
                value=vpc.public_subnets[i].subnet_id
            )
            core.CfnOutput(
                self, 
                'VPC-Public-Subnet-%s-Route-Table-id'%(i+1), 
                value=vpc.public_subnets[i].route_table.route_table_id
            )
        
        # for i in range(len(vpc.private_subnets)):
        #     core.CfnOutput(
        #         self, 
        #         'VPC-Private-Subnet-%s'%(i+1), 
        #         value=vpc.private_subnets[i].subnet_id
        #     )
        #     core.CfnOutput(
        #         self, 
        #         'VPC-Private-Subnet-%s-Route-Table-id'%(i+1), 
        #         value=vpc.private_subnets[i].route_table.route_table_id
        #     )