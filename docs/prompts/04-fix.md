Address review findings for task <TASK_ID>, change <CHANGE>.

Review findings: <REVIEW>.

Check each finding against the implementation and specification. Fix confirmed defects within scope. If a finding is incorrect, explain why with evidence; do not dismiss it without verification.

Add regression tests for real defects when appropriate. Preserve requirement IDs and the sole decision log. Do not weaken analyzers, gates, tests or specifications to make checks pass.

Rerun affected checks and the final required set before claiming readiness. If code changed after SonarQube analysis, analyze the new version. Preserve the single compose.yaml.

Use verification-before-completion. Report each finding as fixed, not confirmed with evidence, or requiring a decision. Identify changes that need another review. Do not archive the change until review and acceptance are complete.
