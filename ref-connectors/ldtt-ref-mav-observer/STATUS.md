# STATUS — ldtt-ref-mav-observer (Phase 2)

**Brand:** Linked Drone Tool Trust · **Lead:** creator · Corrector reviews via creator  
**Tag:** Phase 2 · **Do not call final / PASS**

Updated: 2026-10-06 ~03:45 America/Chicago

## Milestones this turn (creator locks + DoD advance)

| Item | State |
|---|---|
| Creator locks applied (cosign, REQUEST_DATA_STREAM, LOG_REQUEST_*, placeholders, P4, Operate NO, protected draft widen) | Applied |
| `ldtt.yaml` tx without REQUEST_DATA_STREAM / LOG_REQUEST_* + known_limitations C4/C3 | Drafted |
| Cosign runtime path + CI workflow (keyless) + local signed placeholders | Drafted |
| Fake HEARTBEAT peer smoke (`scripts/sitl_smoke.py`) | Drafted (real SITL blocked: no Docker/sim_vehicle) |
| Evidence E1–E8 advanced | Partial — see evidence checklist |
| Unit tests updated for locked TX | Drafted |
| Mapping + protected-settings drafts updated | Drafted |
| $0 / no hardware / no DJI RE | Met |

## Definition of done (toward — not claimed complete)

| # | DoD | Status |
|---|---|---|
| 1 | `ldtt.yaml` validates vs schema | Done (re-validate after locks) |
| 2 | C4 revocation vs signed list + staleness + rollback | Logic + tests; cosign verify when available; Observe fail-open if cosign missing |
| 3 | C5 audit + C6 rate limits | Writers/enforcers + unit tests + E5 sample from smoke |
| 4 | Evidence E1–E8 filled | Partial — see checklist |
| 5 | First stamp + empty revocation cosign-signed | Local placeholder key signed; CI keyless workflow drafted; public HTTPS URL TBD |
| 6 | $0 spend | Met |

## Confirmations

- Spend: **$0**
- Hardware: **none**
- Brand: **Linked Drone Tool Trust** (not Lineage)
- Drafts only — **never call final/PASS**
