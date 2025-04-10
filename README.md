# MLOps Project

이 프로젝트는 FastAPI 기반의 ML 애플리케이션을 AWS EKS에 배포하고, Terraform, Helm, GitHub Actions를 사용하며, Prometheus와 Grafana로 모니터링을 설정한 MLOps 워크플로우를 보여줍니다.

## 사용된 기술
- **FastAPI**: ML 모델 서빙
- **Docker**: 컨테이너화
- **AWS EKS**: 쿠버네티스 클러스터
- **Terraform**: 인프라 프로비저닝
- **Helm**: 쿠버네티스 리소스 관리
- **Prometheus/Grafana**: 모니터링

## 배포 방법
1. **Terraform으로 EKS 클러스터 배포**:
   ```bash
   cd terraform
   terraform apply
   ```

2. **Helm으로 FastAPI 앱 배포**:
   ```bash
   helm install mlops-app ./mlops-chart --set image.repository=mlopsparkminwoo/mlops-project --set image.tag=latest
   ```

3. **앱 확인**:
   ```bash
   kubectl get svc mlops-app
   ```
   브라우저에서 `EXTERNAL-IP`로 접속하세요.

## 모니터링 설정
- **Prometheus/Grafana 설치**:
  ```bash
  helm install prometheus prometheus-community/kube-prometheus-stack
  ```

- **메트릭 확인**:
  HTTP 요청 수: `http_requests_total`

- **Grafana 접속**:
  ```bash
  kubectl get svc prometheus-grafana
  ```
  브라우저에서 `EXTERNAL-IP`로 접속 (기본 계정: `admin`, 비밀번호: `prom-operator`)

   ![Grafana Dashboard](/images/grafana_dashboard.png)