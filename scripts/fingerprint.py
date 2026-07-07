#!/usr/bin/env python3
"""
Print a content fingerprint (SHA-256) for a file, prefixed with "sha256:".

Usage:
    python3 scripts/fingerprint.py <path>

Used by the proposal-router and knowledge-trainer for idempotency ("train only
once"). A content hash is stable across git clones (unlike file mtime), so the
committed training-ledger.json stays valid after someone clones the repo —
`/train` then correctly skips unchanged solutions instead of re-ingesting all of
them. Only stdlib is used, so this runs under any Python 3 (venv not required).
"""

import hashlib
import sys


def main(argv):
    if len(argv) != 2:
        print("usage: fingerprint.py <path>", file=sys.stderr)
        return 2
    h = hashlib.sha256()
    with open(argv[1], "rb") as f:
        for chunk in iter(lambda: f.read(65536), b""):
            h.update(chunk)
    print("sha256:" + h.hexdigest())
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
