# Deploy using docker compose
Step 1 Login to Deepgram get a new api key

Step 2 In Windows, create a .env file
```bash
DEEPGRAM_API_KEY=DEEPGRAM_KEY
```
Step 3 Deploy setup
```bash
docker compose up -d
```
# Deploy using k8s
Step 1 Login to Deepgram get a new api key

Step 2 In Windows, start Minikube
```bash
minikube start
```
Step 2 In Windows, Create a image
```bash
docker build -t deepgram-app:latest .
```
Step 4 Load Docker Image into Minikube
```bash
minikube image load deepgram-app:latest
```
Step 5 Load Docker Image into Minikube
```bash
minikube image load deepgram-app:latest
```
Step 6 Deploy setup
```bash
kubectl apply -f .\k8s\secret.yaml # Note: add api key in base64 encoded format in k8s/secret.yaml 
kubectl apply -f .\k8s\service.yaml
kubectl apply -f .\k8s\deployment.yaml
```

# Output
![Output](./images/Screenshot%202025-01-05%20155642.png)

Now we can upload our wav audio and get text by submiting form


# Scaling and Production Cost

### Comparison Summary

| Feature              | GKE Autopilot                                      | AWS Karpenter                                          | GKE NAP (Node Autoprovisioning)                    |
|----------------------|----------------------------------------------------|--------------------------------------------------------|-------------------------------------------------------|
| Autoscaling          | Fully managed, automatic node and pod scaling      | Dynamic node scaling based on workload demand          | Automatic node pool scaling with Cluster Autoscaler    |
| Node Management      | No need to manage nodes; fully abstracted          | Node provisioning based on pod requirements            | Automatically manages node pools                      |
| Flexibility          | Limited customization of node types                | Highly flexible, selects instance types based on needs | More control over node pools but requires management |
| Cost Optimization    | Optimized for simplicity and predictability        | Optimized for cost with EC2 instance selection         | Optimized for node pool management but still pays for node capacity |
| Billing Model        | Pay for consumed resources (CPU, memory)           | Pay for EC2 instances (includes unused capacity)       | Pay for the resources of the node pools               |
| Ease of Use          | Easy setup, no need for manual intervention        | Requires AWS setup and IAM roles                       | Requires some Kubernetes and GCP knowledge            |
| Use Case             | Best for users who want a fully managed Kubernetes experience | Best for users with EKS who want fine-grained control over resources | Best for GKE users who want automatic node scaling with some level of control |


# Optimise muliple weight files
Question: ⁠How to optimise multiple weight files of deep learning models in one service/ pod ?


1. Storage: Store the model weights in a shared location e.g object storage like MinIO, AWS S3, EFS. If we are using k8s, we can consider using a persistent volume (PV) with AWS EFS or GCP file store a shared volume to store the weights.
2. Model Versioning: If we have multiple versions of the models, keep track of the version number to avoid issues with outdated weights.
3. Model File Format: To ensure that the models are stored in efficient formats like TensorFlow SavedModel, ONNX, or PyTorch .pth files, depending on the framework.
4. Preload Model: We can load models dynamically when needed or when API hit.


# References
- [Karpenter](https://karpenter.sh/)
- [Reducing GKE production costs](https://medium.com/@omers1414/reducing-gke-production-costs-314602419647)
- [GKE Autopilot vs. AWS Karpenter: A Deep Dive into Billing Efficiency and Discount Models](https://medium.com/@garfield13579/gke-autopilot-vs-aws-karpenter-a-deep-dive-into-billing-efficiency-and-discount-models-01829636dd9d)
- [How to optimize Kubernetes performance for machine learning workloads](https://www.ivinco.com/blog/how-to-optimize-kubernetes-performance-for-machine-learning-workloads)


Note: Considering in minikube but note we can deploy in EKS cluster as well.