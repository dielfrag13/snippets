# Top 10 Debugging Habits

Use these as repeatable behaviors, not one-off tricks.

1. Reproduce before you fix
- Make the failure happen consistently with one exact command/route/input.
- If you cannot reproduce, you cannot reliably verify a fix.

2. Read the first meaningful error
- Focus on the earliest actionable line in logs/stack traces.
- Later errors are often cascade noise.

3. Classify the problem first
- Bucket quickly: environment, build/config, runtime logic, or data contract.
- This avoids random trial-and-error edits.

4. Verify assumptions with one direct check
- Add one log, one network inspection, one path check, or one port check.
- Prefer evidence over intuition.

5. Isolate a minimal failing case
- Shrink the failing area to the smallest file/flow/input.
- Smaller surface area means faster root-cause discovery.

6. Change one thing at a time
- Single-variable experiments make cause/effect clear.
- Multi-change edits hide what actually solved the issue.

7. Check boundaries first
- Validate inputs/outputs across component, API, and module boundaries.
- Most bugs are contract mismatches at handoff points.

8. Use tooling intentionally
- Browser DevTools: Network + Console + Sources.
- Build logs, lints, and type errors are guidance, not interruptions.

9. Keep a short debug journal
- Write: symptom, hypothesis, check, result, next step.
- Prevents loops and speeds future debugging.

10. Confirm with a regression check
- Re-run the original failure path and one nearby happy path.
- Ensure the fix solves root cause without collateral breakage.

## Mindset shifts

- From "Why is this broken?" to "Which assumption is wrong?"
- From "I’ll try random fixes" to "I’ll run one falsifiable test"
- From "The tool is wrong" to "What contract did I violate?"
- From "It works once" to "It reproduces and stays fixed"

## 60-second triage routine

1. Capture exact failing command/screen.
2. Read first actionable error line.
3. Choose one hypothesis.
4. Run one confirming check.
5. Apply smallest fix.
6. Re-test failure + adjacent success case.
