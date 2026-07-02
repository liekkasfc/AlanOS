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


def run_validate_result(records_dir: Path) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        [sys.executable, str(VALIDATE_SCRIPT), "--records-dir", str(records_dir), "--result"],
        capture_output=True,
        text=True,
        check=False,
    )


def run_validate_links(records_dir: Path) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        [sys.executable, str(VALIDATE_SCRIPT), "--records-dir", str(records_dir), "--links"],
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


def test_validate_records_ready_ignores_post_execution_placeholders(tmp_path):
    sample_dir = copy_sample_dir(tmp_path)
    validation_record_path = sample_dir / "validation_record.sample.json"
    validation_record = json.loads(validation_record_path.read_text())
    validation_record["outcome"] = "TODO: record this after execution"
    validation_record_path.write_text(json.dumps(validation_record, indent=2) + "\n")

    result = run_validate_ready(sample_dir)

    assert result.returncode == 0, result.stderr
    assert "ready" in result.stdout


def test_validate_records_result_fails_before_execution_placeholders(tmp_path):
    day_dir = init_day(tmp_path / "daily")

    result = run_validate_result(day_dir)

    assert result.returncode != 0
    assert str(day_dir / "validation_record.json") in result.stderr
    assert "actions_taken" in result.stderr
    assert "outcome" in result.stderr
    assert "time_spent_minutes" in result.stderr


def test_validate_records_links_fails_on_broken_opportunity_id(tmp_path):
    sample_dir = copy_sample_dir(tmp_path)
    todays_bet_path = sample_dir / "todays_bet.sample.json"
    todays_bet = json.loads(todays_bet_path.read_text())
    todays_bet["opportunity_id"] = "missing_opp"
    todays_bet_path.write_text(json.dumps(todays_bet, indent=2) + "\n")

    result = run_validate_links(sample_dir)

    assert result.returncode != 0
    assert str(todays_bet_path) in result.stderr
    assert "opportunity_id" in result.stderr
    assert "missing_opp" in result.stderr


def test_validate_records_links_passes_sample_records():
    result = run_validate_links(SAMPLE_DIR)

    assert result.returncode == 0, result.stderr
    assert "links valid" in result.stdout
