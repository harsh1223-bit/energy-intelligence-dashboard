import hashlib, json
from datetime import datetime, timezone
from pathlib import Path
import requests
from .config import DATA_URL, RAW_DIR, RAW_FILE, METADATA_FILE


def sha256_file(path: Path) -> str:
    h = hashlib.sha256()
    with path.open('rb') as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b''):
            h.update(chunk)
    return h.hexdigest()


def download_if_needed() -> dict:
    RAW_DIR.mkdir(parents=True, exist_ok=True)
    if RAW_FILE.exists():
        checksum = sha256_file(RAW_FILE)
        metadata = {
            'url': DATA_URL,
            'downloaded_at_utc': None,
            'file': str(RAW_FILE.relative_to(RAW_FILE.parents[2])),
            'sha256': checksum,
            'reused_existing_file': True,
        }
    else:
        r = requests.get(DATA_URL, timeout=120)
        r.raise_for_status()
        RAW_FILE.write_bytes(r.content)
        metadata = {
            'url': DATA_URL,
            'downloaded_at_utc': datetime.now(timezone.utc).isoformat(),
            'file': str(RAW_FILE.relative_to(RAW_FILE.parents[2])),
            'sha256': sha256_file(RAW_FILE),
            'reused_existing_file': False,
        }
    METADATA_FILE.write_text(json.dumps(metadata, indent=2), encoding='utf-8')
    return metadata

if __name__ == '__main__':
    print(json.dumps(download_if_needed(), indent=2))
