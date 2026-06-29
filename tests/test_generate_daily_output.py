import json
import shutil
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "generate_daily_output.py"
SAMPLE_DIR = ROOT / "data" / "sample"


def run_generator(sample_dir: Path, date: str = "2026-06-29") -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        [sys.executable, str(SCRIPT), "--sample-dir", str(sample_dir), "--date", date],
        capture_output=True,
        text=True,
        check=False,
    )


def run_generator_with_records_dir(records_dir: Path, date: str = "2026-06-29") -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        [sys.executable, str(SCRIPT), "--records-dir", str(records_dir), "--date", date],
        capture_output=True,
        text=True,
        check=False,
    )


def copy_sample_dir(tmp_path: Path) -> Path:
    copied = tmp_path / "sample"
    shutil.copytree(SAMPLE_DIR, copied)
    return copied


def test_daily_output_contains_exactly_one_todays_bet_section():
    result = run_generator(SAMPLE_DIR)

    assert result.returncode == 0, result.stderr
    assert result.stdout.count("## Today's Bet") == 1
    assert "bet_sample_001" in result.stdout


def test_daily_output_supports_records_dir_alias():
    result = run_generator_with_records_dir(SAMPLE_DIR)

    assert result.returncode == 0, result.stderr
    assert result.stdout.count("## Today's Bet") == 1
    assert "bet_sample_001" in result.stdout


def test_daily_output_contains_required_action_fields():
    result = run_generator(SAMPLE_DIR)

    assert result.returncode == 0, result.stderr
    assert "Give-up rule" in result.stdout
    assert "If there are no replies after two follow-ups" in result.stdout
    assert "Expected signal" in result.stdout
    assert "A serious reply, booked call, paid review request" in result.stdout


def test_daily_output_contains_validation_plan_and_recording_prompts():
    result = run_generator(SAMPLE_DIR)

    assert result.returncode == 0, result.stderr
    assert "## Validation Plan" in result.stdout
    assert "Founders with active enterprise deals will discuss or pay" in result.stdout
    assert "## Recording Prompts" in result.stdout
    assert "Record RevenueSignals" in result.stdout
    assert "Record RejectionSignals" in result.stdout


def test_generator_fails_with_multiple_active_bets_for_same_date(tmp_path):
    sample_dir = copy_sample_dir(tmp_path)
    original = json.loads((sample_dir / "todays_bet.sample.json").read_text())
    duplicate = {
        **original,
        "id": "bet_sample_002",
        "status": "active",
        "action": "Second same-day bet that should not be rendered.",
    }
    (sample_dir / "todays_bet_duplicate.sample.json").write_text(
        json.dumps(duplicate, indent=2) + "\n"
    )

    result = run_generator(sample_dir)

    assert result.returncode != 0
    assert "more than one active Today's Bet" in result.stderr
