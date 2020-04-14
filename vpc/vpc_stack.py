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

        # #############################
        # # VPC
        # #############################
        # # https://docs.aws.amazon.com/cdk/api/latest/python/aws_cdk.aws_ec2/Vpc.html

        # subnet_amount = 2
        # subnet_list = []
        
        # # public subnet
        # public_subnet = ec2.SubnetConfiguration(
        #     name = 'My-Public', 
        #     subnet_type = ec2.SubnetType.PUBLIC, 
        #     cidr_mask=24
        # )
        # subnet_list.append(public_subnet)
        
        # # private subnet
        # # private_subnet = ec2.SubnetConfiguration(
        # #     name = 'My-Private', 
        # #     subnet_type = ec2.SubnetType.PRIVATE, 
        # #     cidr_mask=24
        # # )
        # # subnet_list.append(private_subnet)

        # # vpc setting
        # VPC_id = 'My Lab VPC'
        # CIDR = '10.0.0.0/16'
        # vpc = ec2.Vpc(
        #     self,
        #     VPC_id,
        #     cidr=CIDR,
        #     max_azs=subnet_amount,
        #     nat_gateways=0, 
        #     nat_gateway_subnets=None, 
        #     subnet_configuration=subnet_list, 
        #     vpn_connections=None, 
        #     vpn_gateway=None, 
        #     vpn_gateway_asn=None, 
        #     vpn_route_propagation=None
        #     )
        
        # # output 
        # core.CfnOutput(
        #     self, 
        #     'VPC-CIDR', 
        #     value=vpc.vpc_cidr_block
        # )
        # core.CfnOutput(
        #     self, 
        #     'VPC-id', 
        #     value=vpc.vpc_id
        # )
        
        # for i in range(len(vpc.availability_zones)):
        #     core.CfnOutput(
        #         self, 
        #         'VPC-AZ-%s'%(i+1), 
        #         value=vpc.availability_zones[i]
        #     )
        
        # for i in range(len(vpc.public_subnets)):
        #     core.CfnOutput(
        #         self, 
        #         'VPC-Public-Subnet-%s'%(i+1), 
        #         value=vpc.public_subnets[i].subnet_id
        #     )
        #     core.CfnOutput(
        #         self, 
        #         'VPC-Public-Subnet-%s-Route-Table-id'%(i+1), 
        #         value=vpc.public_subnets[i].route_table.route_table_id
        #     )
        
        # # for i in range(len(vpc.private_subnets)):
        # #     core.CfnOutput(
        # #         self, 
        # #         'VPC-Private-Subnet-%s'%(i+1), 
        # #         value=vpc.private_subnets[i].subnet_id
        # #     )
        # #     core.CfnOutput(
        # #         self, 
        # #         'VPC-Private-Subnet-%s-Route-Table-id'%(i+1), 
        # #         value=vpc.private_subnets[i].route_table.route_table_id
        # #     )
##########################
# Resource
##########################
    ##########################
    # VPC setting
    ##########################
        # VPC
        # https://docs.aws.amazon.com/cdk/api/latest/python/aws_cdk.aws_ec2/CfnVPC.html#
        vpc = ec2.CfnVPC(
            self,
            'My Lab VPC',
            cidr_block='10.0.0.0/16',
            enable_dns_hostnames=None, 
            enable_dns_support=None, 
            instance_tenancy=None, 
            tags=[{'key':'Name','value':'My Lab VPC'}]
        )

        # Sets the deletion policy of the resource based on the removal policy specified.
        vpc.apply_removal_policy(policy=core.RemovalPolicy.DESTROY)
        
        # Internet Gateway
        # https://docs.aws.amazon.com/cdk/api/latest/python/aws_cdk.aws_ec2/CfnInternetGateway.html
        igw = ec2.CfnInternetGateway(
            self,
            'My Internet Gateway',
            tags=[{'key':'Name','value':'My IGW'}]
            )
        igw.apply_removal_policy(policy = core.RemovalPolicy.DESTROY)

        # VPC Gateway Attachment 
        # https://docs.aws.amazon.com/cdk/api/latest/python/aws_cdk.aws_ec2/CfnVPCGatewayAttachment.html
        vpc_gateway_attachment = ec2.CfnVPCGatewayAttachment(
            self,
            'My VPC Gateway Attachment',
            vpc_id = vpc.ref,
            internet_gateway_id = igw.ref
            )
        
        # Public Route Table
        # https://docs.aws.amazon.com/cdk/api/latest/python/aws_cdk.aws_ec2/CfnRouteTable.html
        public_route_table = ec2.CfnRouteTable(
            self,
            'My Public Route Table',
            vpc_id = vpc.ref,
            tags=[{'key':'Name','value':'My Public Route Table'}]
        )

        # Public Route
        # https://docs.aws.amazon.com/cdk/api/latest/python/aws_cdk.aws_ec2/CfnRoute.html
        public_route = ec2.CfnRoute(
            self,
            'My Public Route',
            destination_cidr_block = '0.0.0.0/0',
            route_table_id = public_route_table.ref,
            gateway_id = igw.ref
        )

        # get all az in this regions
        # https://docs.aws.amazon.com/cdk/api/latest/python/aws_cdk.core/Fn.html
        azs = core.Fn.get_azs()

        # Public Subnet
        # https://docs.aws.amazon.com/cdk/api/latest/python/aws_cdk.aws_ec2/CfnSubnet.html
        public_sunet1 = ec2.CfnSubnet(
            self, 
            'Public-Subnet-1', 
            cidr_block = '10.0.1.0/24', 
            vpc_id = vpc.ref, 
            assign_ipv6_address_on_creation=None, 
            availability_zone=core.Fn.select(0,azs), 
            ipv6_cidr_block=None, 
            map_public_ip_on_launch=True, 
            tags=[{'key':'Name','value':'Public-Subnet-1'}]
        )

        public_sunet2 = ec2.CfnSubnet(
            self, 
            'Public-Subnet-2', 
            cidr_block = '10.0.3.0/24', 
            vpc_id = vpc.ref, 
            assign_ipv6_address_on_creation=None, 
            availability_zone= core.Fn.select(1,azs), 
            ipv6_cidr_block=None, 
            map_public_ip_on_launch=True, 
            tags=[{'key':'Name','value':'Public-Subnet-2'}]
        )

        # Route Table Association (Public-Subnet-1, Public-Subnet-2)
        # https://docs.aws.amazon.com/cdk/api/latest/python/aws_cdk.aws_ec2/CfnSubnetRouteTableAssociation.html
        associate_public_subnet1 = ec2.CfnSubnetRouteTableAssociation(
            self, 
            'PublicSubnet1RouteTableAssociation',
            route_table_id = public_route_table.ref, 
            subnet_id = public_sunet1.ref
        )

        associate_public_subnet2 = ec2.CfnSubnetRouteTableAssociation(
            self, 
            'PublicSubnet2RouteTableAssociation',
            route_table_id = public_route_table.ref, 
            subnet_id = public_sunet2.ref
        )

        # NACL Association to subnets
        # https://docs.aws.amazon.com/cdk/api/latest/python/aws_cdk.aws_ec2/CfnSubnetNetworkAclAssociation.html    
        public_subnet1_network_acl_association = ec2.CfnSubnetNetworkAclAssociation(
            self, 
            'PublicSubnet1NetworkAclAssociation', 
            network_acl_id = vpc.attr_default_network_acl, 
            subnet_id = public_sunet1.ref
            )
        public_subnet2_network_acl_association = ec2.CfnSubnetNetworkAclAssociation(
            self, 
            'PublicSubnet2NetworkAclAssociation', 
            network_acl_id = vpc.attr_default_network_acl, 
            subnet_id = public_sunet2.ref
        )

##########################
# Output
##########################
        core.CfnOutput(
            self, 
            'vpc-id', 
            value=vpc.ref
        )
        core.CfnOutput(
            self, 
            'vpc-CIDR', 
            value=vpc.cidr_block
        )
        core.CfnOutput(
            self, 
            'igw-id', 
            value=igw.ref
        )
        core.CfnOutput(
            self, 
            'Public Sunet 1', 
            value=public_sunet1.ref
        )
        core.CfnOutput(
            self, 
            'Public Sunet 2', 
            value=public_sunet2.ref
        )