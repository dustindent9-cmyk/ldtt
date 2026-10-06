"""Phase 2: cosign-missing fail-open + locked TX + local placeholder path."""

import json
from datetime import datetime, timezone
from pathlib import Path

import pytest

from ldtt_ref_mav_observer.cosign_verify import find_cosign, verify_blob
from ldtt_ref_mav_observer.revocation_checker import RevocationChecker

ROOT = Path(__file__).resolve().parents[1]
PLACEHOLDER = ROOT / "placeholders" / "revocations" / "revocations.json"
PUB = ROOT / "placeholders" / "keys" / "ldtt-placeholder.pub"
BUNDLE = ROOT / "placeholders" / "revocations" / "revocations.json.sigstore.json"


def test_placeholder_files_exist():
    assert PLACEHOLDER.is_file()
    assert BUNDLE.is_file()
    assert PUB.is_file()
    data = json.loads(PLACEHOLDER.read_text())
    assert data["revoked"] == []
    assert data["list_version"] >= 1


def test_cosign_verify_placeholder_when_available():
    cosign = find_cosign()
    if cosign is None:
        pytest.skip("cosign not installed on this host")
    result = verify_blob(PLACEHOLDER, bundle_path=BUNDLE, key_path=PUB, cosign_path=cosign)
    assert result.ok, result.detail
    assert result.mode == "verified"


def test_observe_fail_open_missing_cosign():
    now = datetime(2026, 10, 6, 12, 0, 0, tzinfo=timezone.utc)
    body = PLACEHOLDER.read_bytes()
    bundle = BUNDLE.read_bytes()

    def fetch(url: str) -> bytes:
        if url.endswith(".sigstore.json"):
            return bundle
        return body

    def verify_missing(_b, _s):
        # Simulate cosign missing
        return False

    c = RevocationChecker(
        list_url=str(PLACEHOLDER),
        connector_id="org.ldtt.ref-mav-observer",
        version="0.1.0",
        digest="sha256:" + ("00" * 32),
        max_staleness_s=86400 * 365,
        fetch_fn=fetch,
        verify_fn=verify_missing,
        bundle_url=str(BUNDLE),
        observe_fail_open_missing_cosign=True,
    )
    c._last_verify_mode = "cosign_missing"
    outcome = c.check(now=now)
    assert outcome == "cosign_missing_fail_open"
    assert not c.is_fail_closed
