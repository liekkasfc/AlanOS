import json
import shutil
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
INIT_SCRIPT = ROOT / "scripts" / "init_daily_workspace.py"
VALIDATE_SCRIPT = ROOT / "scripts" / "validate_records.py"
SAMPLE_DIR = ROOT / "data" / "sample"


def run_validate(records_dir: Path) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        [sys.executable, str(VALIDATE_SCRIPT), "--records-dir", str(records_dir)],
        capture_output=True,
        text=True,
        check=False,
    )


def run_validate_ready(records_dir: Path) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        [sys.executable, str(VALIDATE_SCRIPT), "--records-dir", str(records_dir), "--ready"],
        capture_output=True,
        text=True,
        check=False,
    )


def copy_sample_dir(tmp_path: Path) -> Path:
    copied = tmp_path / "sample"
    shutil.copytree(SAMPLE_DIR, copied)
    return copied


def init_day(daily_root: Path, *extra: str) -> Path:
    result = subprocess.run(
        [
            sys.executable,
            str(INIT_SCRIPT),
            "--date",
            "2026-06-29",
            "--daily-root",
            str(daily_root),
            *extra,
        ],
        capture_output=True,
        text=True,
        check=False,
    )
    assert result.returncode == 0, result.stderr
    return daily_root / "2026-06-29"


def test_validate_records_accepts_initialized_manual_templates(tmp_path):
    day_dir = init_day(tmp_path / "daily")

    result = run_validate(day_dir)

    assert result.returncode == 0, result.stderr
    assert "validated" in result.stdout


def test_validate_records_accepts_sample_records():
    result = run_validate(SAMPLE_DIR)

    assert result.returncode == 0, result.stderr
    assert "validated" in result.stdout


def test_validate_records_reports_file_path_and_field_error(tmp_path):
    day_dir = init_day(tmp_path / "daily")
    todays_bet_path = day_dir / "todays_bet.json"
    todays_bet = json.loads(todays_bet_path.read_text())
    todays_bet.pop("give_up_rule")
    todays_bet_path.write_text(json.dumps(todays_bet, indent=2) + "\n")

    result = run_validate(day_dir)

    assert result.returncode != 0
    assert str(todays_bet_path) in result.stderr
    assert "give_up_rule" in result.stderr


def test_validate_records_ready_fails_on_todo_placeholders(tmp_path):
    day_dir = init_day(tmp_path / "daily")

    result = run_validate_ready(day_dir)

    assert result.returncode != 0
    assert str(day_dir / "todays_bet.json") in result.stderr
    assert "action" in result.stderr
    assert "TODO" in result.stderr


def test_validate_records_ready_passes_sample_records():
    result = run_validate_ready(SAMPLE_DIR)

    assert result.returncode == 0, result.stderr
    assert "ready" in result.stdout


def test_validate_records_ready_fails_on_empty_target_personas(tmp_path):
    sample_dir = copy_sample_dir(tmp_path)
    todays_bet_path = sample_dir / "todays_bet.sample.json"
    todays_bet = json.loads(todays_bet_path.read_text())
    todays_bet["target_personas"] = []
    todays_bet_path.write_text(json.dumps(todays_bet, indent=2) + "\n")

    result = run_validate_ready(sample_dir)

    assert result.returncode != 0
    assert str(todays_bet_path) in result.stderr
    assert "target_personas" in result.stderr
