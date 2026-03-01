# 🚀 DevOps CI/CD Kubernetes Deployment (GitOps Style)

This project demonstrates a complete end-to-end DevOps CI/CD pipeline using Docker, GitHub Actions, and Kubernetes with GitOps-style manifest updates.

When code is pushed to `main`, the system automatically:

• Builds a Docker image  
• Tags the image using the Git commit SHA  
• Pushes the image to Docker Hub  
• Updates the Kubernetes deployment manifest with the new image tag  
• Updates the APP_VERSION environment variable  
• Commits the updated manifest back to GitHub  
• Deploys the new version inside Kubernetes  

---

## 🏗 Architecture Flow

Developer Push → GitHub Actions → Docker Hub → Manifest Update → Git Commit → Kubernetes Deployment

This creates a fully traceable pipeline from Git commit → container image → running Kubernetes workload.

---

## 🔁 Deployment Process

1. Code is pushed to `main`
2. GitHub Actions:
   - Extracts short commit SHA
   - Builds Docker image tagged with SHA
   - Pushes image to Docker Hub
   - Updates `k8s/deployment.yaml`
   - Commits the updated manifest back to GitHub
3. Kubernetes deploys the new image
4. Application returns the running version via API

---

## 🧪 Version Verification

After deployment:

kubectl port-forward service/cicd-service 8002:80

Then visit:

http://localhost:8002

Example response:

{
  "message": "CI/CD Kubernetes Deployment",
  "version": "5aa093d"
}

The version matches the Git commit SHA that triggered the deployment.

---

## 🛠 Tech Stack

Docker  
Docker Hub  
GitHub Actions  
Kubernetes (Kind for local cluster)  
YAML automation via yq  
GitOps-style workflow  

---

## 📂 Repository Structure

app/
  main.py
  Dockerfile
  requirements.txt

k8s/
  deployment.yaml
  service.yaml

.github/workflows/
  cicd.yaml

---

## 💡 What This Demonstrates

• CI/CD automation  
• Immutable Docker image tagging  
• GitOps-style manifest updates  
• Automated version traceability  
• Kubernetes deployment management  
• Infrastructure-as-code principles  

---

## 🎯 Portfolio Relevance

This project demonstrates practical DevOps engineering skills used in modern cloud-native environments:

• Automated container build & push  
• Git-based release workflows  
• Manifest mutation via pipeline  
• Version-controlled deployments  
• Kubernetes workload management  

Built by Liam — aspiring DevOps / Cloud Engineer.
