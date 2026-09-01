# Plentific AWS Infrastructure Ops Control Plane

Independent proof-of-work inspired by Plentific's AWS Infrastructure Engineer role.

This project models a reliability-first operational control plane for an AWS estate where the job is not simply to provision infrastructure, but to run it safely every day: respond to P1/P2 incidents, diagnose Linux/AWS/network failures, recover data, operate Terraform state correctly, maintain Ansible automation, and turn recurring break-fix work into permanent engineering improvements.

> Based only on the public job description; no claim is made about Plentific's private architecture.

## Core workflow

```text
Alert / failed deploy / outage
            |
            v
        TRIAGE
            |
            +--> AWS infrastructure?
            +--> Linux host?
            +--> Network/DNS?
            +--> Terraform/IaC?
            +--> Application?
            |
            v
        MITIGATE
            |
            +--> rollback
            +--> restart/failover
            +--> restore from backup/snapshot
            +--> repair drift/state
            |
            v
        VALIDATE
            |
            v
       RCA + automation
            |
            +--> Terraform
            +--> Ansible
            +--> runbook
            +--> monitoring
```

## Operational contract

A production service is considered operationally ready only when evidence exists for AWS health, Linux health, Terraform safety, Ansible idempotence, incident ownership, data recovery, observability, and security/compliance operations.

### AWS
EC2, EKS, ALB, VPC/networking, RDS backups, S3 recovery, Route 53, IAM, CloudWatch ownership.

### Linux
Disk/memory pressure, service state, patch cadence, log growth, CPU/load, safe restart/recovery, time synchronization.

### Terraform
Remote state, locking, plan-before-apply, drift detection, failed apply recovery, import/state recovery, environment isolation, peer review.

### Ansible
Idempotent roles, inventory ownership, check mode, failure handling, rollback path, no plaintext secrets, reusable roles.

### Incident response
P1/P2 severity model, incident commander, impact, recent-change check, evidence preservation, mitigation owner, communications, RCA and permanent corrective action.

### Data recovery
RDS restore tests, snapshot ownership, S3 recovery, restore verification, RTO/RPO awareness, recovery decision tree.

### Observability
CloudWatch alarms, actionable thresholds, logs, infrastructure metrics, dependency health, deployment markers, recurring-failure detection.

### Security / compliance operations
IAM access review, asset inventory, patching, audit evidence, incident support, secrets handling.

## Evidence sources in production

The JSON examples are deterministic PoC fixtures. A real implementation should derive evidence from AWS APIs/CloudWatch, Terraform plan/state, Ansible inventory/playbooks, Linux agents/SSM, CI/CD metadata, incident systems, ownership catalogues, and restore-test results. Operators should not self-attest that a service is safe; the platform should gather evidence.

## Run locally

```bash
python -m unittest -v tests.test_gate
python src/cli.py examples/healthy.json
python src/cli.py examples/unsafe.json
```

## 30 / 60 / 90

**0-30:** learn estate topology and ownership, shadow P1/P2s, map recurring failures, validate restore/runbook reality, baseline Terraform/Ansible operational debt.

**31-60:** remove top toil, improve failed-apply/state runbooks, harden Linux operational checks, validate RDS/S3 recovery, improve CloudWatch signal quality.

**61-90:** automate common break-fix paths, reduce repeat incidents, standardize readiness, shorten MTTR, feed recurring failure modes back into platform engineering.

## Success metrics
MTTR/MTTD, repeat incident rate, failed deployment recovery time, Terraform apply failure recurrence, restore-test success, patch compliance, alert actionability, manual toil, and percentage of incidents resulting in permanent corrective action.
