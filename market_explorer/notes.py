"""
Notes management per profile and company.
"""

import json
from pathlib import Path
from typing import Dict


NOTES_DIR = Path("notes")


def _profile_path(profile: str) -> Path:
    NOTES_DIR.mkdir(exist_ok=True)
    return NOTES_DIR / f"{profile}.json"


def load_notes(profile: str) -> Dict[str, str]:
    """Load notes for a given user profile."""
    path = _profile_path(profile)
    if not path.exists():
        return {}
    return json.loads(path.read_text())


def save_notes(profile: str, notes: Dict[str, str]) -> None:
    """Save notes for a given user profile."""
    path = _profile_path(profile)
    path.write_text(json.dumps(notes, indent=2))


def reset_notes(profile: str) -> None:
    """Delete all notes for a profile."""
    path = _profile_path(profile)
    if path.exists():
        path.unlink()


def company_key(name: str, country: str) -> str:
    """Create a stable key for a company."""
    return f"{name}__{country}".lower()


def upsert_note(
    profile: str,
    company_name: str,
    country: str,
    note: str,
) -> None:
    """Add or update a note for a company."""
    notes = load_notes(profile)
    key = company_key(company_name, country)
    notes[key] = note
    save_notes(profile, notes)
