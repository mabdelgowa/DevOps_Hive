provider "aws" {
  region = "us-east-1"
}

variable "vpc_cidr_block" {}
variable "private_subnet_cidr_blocks" {}
variable "public_subnet_cidr_blocks" {}
data "aws_availability_zones" "azs" {}
module "vpc" {
  source  = "terraform-aws-modules/vpc/aws"
  version = "5.1.1"
  name = "myapp-vpc"
  cidr = var.vpc_cidr_block
  private_subnets = var.private_subnet_cidr_blocks
  public_subnets = var.public_subnet_cidr_blocks
  azs = data.aws_availability_zones.azs.names
  enable_nat_gateway = true
  single_nat_gateway = true
  enable_dns_hostnames = true
  tags = {
    "kubernates.io/cluster/myapp-eks-cluster" = "shared"
  }
  public_subnet_tags = {
    "kubernates.io/cluster/myapp-eks-cluster" = "shared"
    "kubernates.io/role/elb" = 1
  }
  private_subnet_tags = {
    "kubernates.io/cluster/myapp-eks-cluster" = "shared"
    "kubernates.io/role/internal-elb" = 1
  }
}
