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
kubectl apply -f .\k8s\secret.yaml
kubectl apply -f .\k8s\service.yaml
kubectl apply -f .\k8s\deployment.yaml
```

# Output
![Output](./images/Screenshot%202025-01-05%20155642.png)

Now we can upload our wav audio and get text by submiting form

Note: Considering in minikube but note we can deploy in EKS cluster as well.