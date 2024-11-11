## Flow de Atividades

Logando o terminal no GCP:
```
gcloud auth login
```

Selecionando o projeto:
```
gcloud config set project machine-learning-ada-1
```

Criando uma conta de serviço:
```
gcloud iam service-accounts create mle-service --display-name=mle-service --project=machine-learning-ada-1
```

#### Dando autorizações especificas do projeto para conta de serviço criada.

Storage Object Viewer
```
gcloud projects add-iam-policy-binding --member=serviceAccount:your_service_account@project_id.iam.gserviceaccout.com --role=roles/storage.objectViewer
```
Storage Admin
```
gcloud projects add-iam-policy-binding machine-learning-ada-1 --member=serviceAccount:your_service_account@project_id.iam.gserviceaccout.com --role=roles/storage.admin
```
Cloud Run Admin
```
gcloud projects add-iam-policy-binding machine-learning-ada-1     --member=serviceAccount:your_service_account@project_id.iam.gserviceaccout.com     --role=roles/run.admin
```
Monitoring Admin
```
gcloud projects add-iam-policy-binding machine-learning-ada-1     --member=serviceAccount:your_service_account@project_id.iam.gserviceaccout.com     --role=roles/monitoring.admin
```
Loggin Admin
```
gcloud projects add-iam-policy-binding machine-learning-ada-1     --member=serviceAccount:your_service_account@project_id.iam.gserviceaccout.com     --role=roles/logging.admin
```

Updated IAM policy for project [machine-learning-ada-1].
bindings:
- members:
  - serviceAccount:your_service_account@project_id.iam.gserviceaccout.com
  role: roles/logging.admin
- members:
  - serviceAccount:your_service_account@project_id.iam.gserviceaccout.com
  role: roles/monitoring.admin
- members:
  - user:juanvieir4@gmail.com
  role: roles/owner
- members:
  - serviceAccount:your_service_account@project_id.iam.gserviceaccout.com
  role: roles/run.admin
- members:
  - serviceAccount:your_service_account@project_id.iam.gserviceaccout.com
  role: roles/storage.admin
- members:
  - serviceAccount:your_service_account@project_id.iam.gserviceaccout.com
  role: roles/storage.objectViewer
etag: xxxxxxx=
version: 1

Create Bucket for logs
```
gsutil mb -l us-central1 gs://credit-logs-mle
```
