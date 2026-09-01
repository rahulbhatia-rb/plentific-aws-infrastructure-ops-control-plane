REQUIRED = {'aws': ['ec2_health', 'eks_health', 'alb_target_health', 'vpc_checks', 'rds_backup', 's3_recovery', 'route53_health', 'iam_least_privilege', 'cloudwatch_owner'], 'linux': ['disk_pressure', 'memory_pressure', 'service_state', 'patch_cadence', 'log_growth', 'cpu_load', 'recovery_procedure', 'time_sync'], 'terraform': ['remote_state', 'locking', 'plan_before_apply', 'drift_detection', 'failed_apply_recovery', 'import_procedure', 'state_recovery', 'env_isolation', 'peer_review'], 'ansible': ['idempotent_roles', 'inventory_owner', 'check_mode', 'failure_handling', 'rollback_path', 'no_plaintext_secrets', 'reusable_roles'], 'incident': ['severity_model', 'incident_commander', 'customer_impact', 'recent_change_check', 'mitigation_owner', 'evidence_preservation', 'communication_cadence', 'rca_owner', 'permanent_corrective_action', 'recurrence_prevention'], 'recovery': ['rds_restore_test', 'snapshot_owner', 's3_recovery_procedure', 'restore_verification', 'rto_rpo', 'recovery_decision_tree'], 'observability': ['cloudwatch_alarms', 'actionable_thresholds', 'logs', 'infra_metrics', 'dependency_health', 'deployment_markers', 'recurring_failure_detection'], 'security': ['iam_access_review', 'asset_inventory', 'patching', 'audit_evidence', 'incident_support', 'secrets_handling']}

def evaluate(spec):
    findings=[]
    for section, fields in REQUIRED.items():
        values=spec.get(section,{})
        for field in fields:
            if not values.get(field):
                findings.append(f'{section}.{field} is required')
    return {'allowed': not findings, 'findings': findings}
