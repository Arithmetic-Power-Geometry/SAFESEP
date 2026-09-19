# Android emulator validation boundary

## Purpose

This workflow is a defensive platform-semantics sanity check on an ephemeral
GitHub-hosted Android emulator. It does not target a third-party app, access
user data, bypass a security control, or claim an Android vulnerability.

## Synthetic package

The repository builds a minimal synthetic code-bearing package,
`org.safesep.probe`, declaring the runtime `CAMERA` permission.

## Sequence

1. install the synthetic package;
2. force the permission to denied;
3. verify denied state;
4. grant the permission with Android package-manager tooling;
5. verify granted state;
6. revoke the permission;
7. verify denied state again;
8. uninstall the package.

## Interpretation

A green workflow demonstrates only that the CI emulator exposes a real
grant/revoke authority transition matching the basic token-state intuition.

The revocation step is especially important scientifically: revocation is
outside the monotone BRAC completeness theorem. Therefore the workflow should
not be used to claim that BRAC normalizes arbitrary Android authorization
behavior.

A stronger empirical SAFESEP result would require a real sequence in which
evidence acquisition, observation branching, and authorization applicability
interact in a way predicted by the theory. That remains future work unless a
separate owned/emulated-device experiment establishes it.
