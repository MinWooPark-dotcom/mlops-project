provider "aws" {
    region = "ap-northeast-2"
}

module "eks" {
    source = "terraform-aws-modules/eks/aws"
    version = "~> 19.0"

    cluster_name    = "mlops-cluster"
    cluster_version = "1.29"

    vpc_id  = "vpc-af2998c4"
    subnet_ids = ["subnet-fdc26096", "subnet-5c930c27", "subnet-7a110736", "subnet-527d9d0d"]

    cluster_endpoint_public_access = true
    cluster_endpoint_private_access = false

    eks_managed_node_groups = {
        default = {
            min_size     = 1
            max_size     = 3
            desired_size = 1
            instance_types = ["t3.medium"]
        }
    }
}

output "cluster_endpoint" {
    value = module.eks.cluster_endpoint
}