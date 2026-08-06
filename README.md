# Capstone Project: Full CI/CD Pipeline

## 🚀 Pipeline Flow
- **Continuous Integration:** GitHub commits automatically trigger builds.
- **Continuous Deployment:** Handled via Vercel connecting repository folders (`week4_task1` and `week4_task2`).

## 📉 Monitoring & Alerting
- **Telemetric Tracking:** Monitored via Vercel Dashboard logs.
- **Simulated Failure:** Testing with `requirments.txt` triggered a `500: FUNCTION_INVOCATION_FAILED` error, showing an instant pipeline status block (❌).

## 🔄 Rollback Procedure
- In case of failure, we can instantly navigate to Vercel Deployments, select the last working deployment (🟢), and click **Redeploy** to roll back with zero downtime.
