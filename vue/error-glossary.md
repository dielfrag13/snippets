# Error Glossary (Vue 2 / JS / TS / Tooling)

Use this as a quick diagnosis playbook.

Mindset pattern:
- Symptom: what you see
- First thought: what to assume first
- Verify: fastest checks
- Fix: likely solution

## Alphabetized errors

### Cannot find module 'X' (or Module not found)
- First thought: dependency missing, misspelled import path, or wrong relative path.
- Verify: check package in `package.json`, run install, confirm file path/casing.
- Fix: install missing package, fix import path, or update file name/case.
- Mindset shift: Assume path/package mismatch before assuming compiler bugs.

### Command not found: yarn / npm / node
- First thought: tool not installed or shell PATH not configured.
- Verify: run `node -v`, `npm -v`, `yarn -v`, inspect PATH.
- Fix: install tool, restart shell, or use full path/corepack.
- Mindset shift: Environment issue first, code issue second.

### CORS policy blocked request
- First thought: backend response headers don’t allow this origin/method/header.
- Verify: browser Network tab → response headers/status + preflight request.
- Fix: configure backend CORS policy correctly.
- Mindset shift: Browser is enforcing a contract, not “randomly failing”.

### EADDRINUSE (address already in use)
- First thought: another process is already using your port.
- Verify: inspect process listening on port, check existing dev server terminals.
- Fix: stop old process or switch to a new port.
- Mindset shift: Treat ports as shared resources that must be managed.

### EACCES / permission denied
- First thought: attempting write/install in restricted location.
- Verify: inspect target path ownership/permissions.
- Fix: install in user scope, use sudo carefully, or adjust permissions.
- Mindset shift: Permission model issue, not package-manager logic.

### ESLint: 'X' is defined but never used
- First thought: dead code or refactor left unused variable/import.
- Verify: check references and intended side effects.
- Fix: remove unused symbol or use it intentionally.
- Mindset shift: Lint warnings are design feedback, not just noise.

### JSON.parse error (Unexpected token ...)
- First thought: malformed JSON string.
- Verify: validate JSON structure (quotes, commas, braces).
- Fix: correct JSON format and add try/catch guards.
- Mindset shift: Data contract first; parser is usually right.

### Missing required prop (Vue warning)
- First thought: parent didn’t pass a required prop.
- Verify: inspect parent template usage and prop definition.
- Fix: pass the prop or make prop optional/defaulted.
- Mindset shift: Component APIs are contracts—treat them like function signatures.

### Network Error (Axios/fetch generic)
- First thought: DNS/connectivity/SSL/proxy/backend unavailable.
- Verify: curl endpoint directly, inspect browser network details.
- Fix: correct base URL, backend status, certificates, proxy settings.
- Mindset shift: Distinguish transport failures from application errors.

### npm ERR! peer dep missing / dependency conflict
- First thought: incompatible dependency versions.
- Verify: inspect peer dependency ranges and installed versions.
- Fix: align versions, upgrade/downgrade package, or pin known-compatible versions.
- Mindset shift: Version resolution is a constraint problem, not a random failure.

### TypeError: Cannot read property 'X' of undefined
- First thought: data is not initialized when accessed.
- Verify: inspect lifecycle timing and null/undefined checks.
- Fix: initialize defaults, guard access, or defer logic until data loads.
- Mindset shift: Assume timing/state shape mismatch before syntax issue.

### TypeError: X is not a function
- First thought: wrong import shape, wrong value type, or typo.
- Verify: inspect symbol at runtime/logging and export/import style.
- Fix: correct import (`default` vs named), rename, or pass function correctly.
- Mindset shift: Validate assumptions about value types at call site.

### TS2339: Property 'X' does not exist on type 'Y'
- First thought: type definition doesn’t match runtime object shape.
- Verify: inspect interface/type, generic constraints, and narrowing.
- Fix: update type, refine union checks, or narrow before access.
- Mindset shift: Type errors are model-mismatch hints, not compiler stubbornness.

### TS2345: Argument of type 'X' is not assignable to 'Y'
- First thought: function contract mismatch.
- Verify: inspect parameter type and calling code value type.
- Fix: convert value, broaden types carefully, or refactor function signature.
- Mindset shift: Let types guide better API boundaries.

### Unexpected token '<' in JSON at position 0
- First thought: received HTML (often error page) instead of JSON.
- Verify: check response body/status in network tab.
- Fix: correct endpoint, auth, proxy, or server route fallback.
- Mindset shift: Always inspect actual payload before debugging parser.

### Vue warn: Avoid mutating a prop directly
- First thought: child component is trying to edit parent-owned state.
- Verify: search child for direct prop assignment.
- Fix: copy prop into local state and emit events for parent updates.
- Mindset shift: In Vue, data ownership should flow down (props) and up (events).

### Vue warn: Duplicate keys detected
- First thought: non-unique `:key` values in `v-for`.
- Verify: confirm each item has stable unique key.
- Fix: use unique IDs, not index-only keys for dynamic lists.
- Mindset shift: Keys are identity, not just list rendering syntax.

### Vue warn: Unknown custom element
- First thought: component not registered/imported correctly.
- Verify: import path, registration name, and case conventions.
- Fix: register component in `components` or globally.
- Mindset shift: Treat template tags as symbols needing scope registration.

### webpack: Module parse failed
- First thought: missing loader or unsupported syntax for current config.
- Verify: inspect file type and corresponding loader rules.
- Fix: add/configure loader or transpilation step.
- Mindset shift: Build pipeline configuration is part of runtime behavior.

### webpack-dev-server compiled successfully but browser unchanged
- First thought: stale tab/cache or wrong server/port.
- Verify: hard refresh, disable cache, confirm active server URL/port.
- Fix: hard reload, restart one dev server, clear cache if needed.
- Mindset shift: Verify serving path and cache before changing code.

## Fast triage checklist

1. Reproduce consistently (same command, same route, same input).
2. Read the first useful error line, not the final cascade line.
3. Separate categories: environment vs build config vs app logic vs data.
4. Validate assumptions with one direct check (log, network tab, port, import path).
5. Apply smallest fix, rerun, and confirm symptom changed.
