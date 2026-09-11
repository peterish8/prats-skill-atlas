# Command risk and permission policy

Classify the concrete action, not only the command name. A normally passive tool becomes higher risk when pointed at a live target, given write flags, run with elevation, or combined with credentials.

## R0 — passive inspection

No additional permission is needed when the action is already within the user's request and remains local and read-only.

Examples: list files, read text, inspect metadata, calculate hashes, run `git status` or `git diff`, parse routing JSON, inspect imports/strings, or search source code. Do not contact a target, execute the sample, or change files.

## R1 — bounded local analysis

No additional permission is needed when the user requested the work, the action stays inside the designated workspace, and it is reversible without touching external systems.

Examples: create case notes, write reports, unpack or statically decompile a user-supplied offline artifact into a new analysis directory, generate diagrams, or run a non-networked parser. Validate output paths before overwrite or cleanup.

Escalate to R2 if a third-party script will run, executable code from the sample may load, global state changes, credentials are involved, or any network/device interaction occurs.

## R2 — sensitive or externally mutating

Ask for explicit permission immediately before execution. This includes:

- cloning, downloading, updating, installing, uninstalling, or executing third-party code;
- package-manager, bootstrap, setup, MCP-registration, or global-configuration commands;
- network requests, enumeration, scanning, fuzzing, interception, replay, or authentication against a target;
- browser automation against a live service, dynamic instrumentation, debugging, emulation, VM/container startup, or local service startup;
- patching, rebuilding, signing, sideloading, or installing an APK/binary, including actions against a connected device;
- use of secrets, tokens, cookies, private keys, production data, or credential-testing tools;
- elevation, registry/firewall changes, persistence-like configuration, recursive deletion, overwrite, or security-control changes;
- password cracking, exploit proof-of-concept execution, or transmitting artifacts outside the approved environment.

## R3 — critical impact

Require both documented authorized scope and explicit permission for the exact action. If policy or law disallows the action, refuse even when permission is given.

Examples: exploitation of a remote/live system, privilege escalation, payload delivery, persistence, credential dumping, lateral movement, EDR/AV bypass, destructive testing, denial-of-service behavior, bulk sensitive-data extraction, production cloud/identity mutation, or operations that could affect third parties.

Prefer a safer lab reproduction, passive validation, or defensive proof whenever it can answer the question.

## Approval message

Use this format and wait for a clear answer:

```text
Permission required — R2 or R3
Purpose: <why this is needed>
Authorized scope: <exact target, sample, account, device, and boundary>
Exact command(s):
<verbatim commands, one per line>
Expected side effects: <network, files, installs, services, device, or data>
Rollback/containment: <how impact is limited or reversed>
Proceed with exactly these commands? (yes/no)
```

Approval covers only the listed commands and scope. Ask again when the target, destination, flags, privileges, persistence, data movement, or likely impact changes. Never bundle an R2/R3 action into an R0/R1 command batch to avoid the gate.
