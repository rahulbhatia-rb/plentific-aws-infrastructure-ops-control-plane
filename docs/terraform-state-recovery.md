# Terraform State / Failed Apply Recovery

1. Stop concurrent applies.
2. Inspect backend availability and lock ownership.
3. Review failed plan/apply.
4. Compare live resources with state.
5. Recover prior state only when justified.
6. Import existing resources rather than blindly recreating them.
7. Run a fresh plan and peer review before apply.
8. Document and prevent recurrence in CI.
