# ldtt-ref-mav-observer (Phase 2 Draft)

**LDTT = Linked Drone Tool Trust** (not “Lineage”)  
**Phase 2** Observe reference connector · Lead: creator · Corrector reviews via creator — **not final**

Read-only **MAVLink 2** telemetry observer. Local CLI display only. No egress. No hardware. SITL or fake-peer smoke. **$0** spend.

## Purpose

- Receives: `HEARTBEAT`, `SYS_STATUS`, `GLOBAL_POSITION_INT`, `ATTITUDE`, `BATTERY_STATUS`
- Sends only Observe TX: `HEARTBEAT`, `PARAM_REQUEST_LIST`, `COMMAND_LONG`
- Commands: `MAV_CMD_REQUEST_MESSAGE`, `MAV_CMD_SET_MESSAGE_INTERVAL` only
- **Locked out:** `REQUEST_DATA_STREAM`, `LOG_REQUEST_*` (creator Phase 2 locks)
- Scope: `observe:telemetry` only
- C4 revocation + cosign (Observe fail-open if cosign missing), C5 audit, C6 rate limits

## Quick start

```bash
python3 -m venv .venv && source .venv/bin/activate
pip install -e ".[dev]"
pytest -q
python scripts/validate_ldtt_yaml.py

# Local signed placeholders (DoD #5) — schema list_url stays https until public repo exists
python -m ldtt_ref_mav_observer \
  --revocation-list placeholders/revocations/revocations.json \
  --cosign-key placeholders/keys/ldtt-placeholder.pub \
  --connection udpin:127.0.0.1:14550
```

### Smoke (no Docker / no ArduPilot SITL required)

```bash
python scripts/sitl_smoke.py
```

See `placeholders/README.md` for swap-to-public-URL steps. See `ARCHITECTURE.md` §7 for lock status.

## License

Apache-2.0 (connector). pymavlink LGPL-3.0 — see `sbom.spdx.json`.

---
*Phase 2 draft · Linked Drone Tool Trust · connector stamp only; not aircraft certification; no FAA claims.*
