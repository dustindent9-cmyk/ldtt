# Placeholders — stamps + revocations (Phase 2 draft, DoD #5)

**Brand:** Linked Drone Tool Trust · **Not final**

## Why local files?

The LDTT public repo URL is **unknown** (creator lock). Schema `revocation.list_url`
requires `^https://`, so `ldtt.yaml` keeps a documented HTTPS placeholder. For local
SITL/smoke and DoD #5 signing work, use the **signed files in this directory**.

```
placeholders/
  revocations/revocations.json
  revocations/revocations.json.sigstore.json
  stamps/org.ldtt.ref-mav-observer/0.1.0.json
  stamps/org.ldtt.ref-mav-observer/0.1.0.json.sigstore.json
  keys/ldtt-placeholder.pub          # public key for local verify
  keys/ldtt-placeholder.key          # PRIVATE — gitignored; local/dev only
```

## Runtime: use file path override

```bash
export LDTT_REVOCATION_LIST_PATH=placeholders/revocations/revocations.json
# or:
ldtt-ref-mav-observer \
  --revocation-list placeholders/revocations/revocations.json \
  --cosign-key placeholders/keys/ldtt-placeholder.pub \
  --connection udpin:127.0.0.1:14550
```

Cosign verify-blob runs at startup and on `check_interval_s` when `cosign` is on PATH
(or `tools/cosign`). If cosign is missing: **Observe fail-open** + audit +
`known_limitations` C4 entry. **Never** fail-open for Operate/Command.

## Swap-to-public-URL (when creator confirms org/repo)

1. Publish `revocations/revocations.json` + `.sigstore.json` and
   `stamps/org.ldtt.ref-mav-observer/0.1.0.json` + `.sigstore.json` to the LDTT
   public git repo (spec §5 paths).
2. Re-sign with **cosign keyless** from GitHub Actions (see `.github/workflows/ci.yml`).
3. Set `revocation.list_url` in `ldtt.yaml` to the raw HTTPS URL of
   `revocations/revocations.json` (must match schema `^https://`).
4. Remove reliance on `--revocation-list` / `LDTT_REVOCATION_LIST_PATH` for production.
5. Point runtime verify at keyless identity regexp (CI), not the local placeholder key.
6. Delete or rotate `placeholders/keys/ldtt-placeholder.key` (never publish the private key).

## Local re-sign

```bash
export COSIGN_PASSWORD=
cosign sign-blob --yes --key placeholders/keys/ldtt-placeholder.key \
  --bundle placeholders/revocations/revocations.json.sigstore.json \
  placeholders/revocations/revocations.json
```

---
*Phase 2 draft · Linked Drone Tool Trust · drafts only — never call final/PASS*
