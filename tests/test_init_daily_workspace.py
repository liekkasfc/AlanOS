import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "init_daily_workspace.py"


EXPECTED_FILES = [
    "signal.json",
    "information_gap.json",
    "opportunity.json",
    "todays_bet.json",
    "validation_plan.json",
    "validation_record.json",
    "revenue_signal.json",
    "rejection_signal.json",
    "alan_memory.json",
]


def run_init(daily_root: Path, date: str = "2026-06-29", *extra: str) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        [
            sys.executable,
            str(SCRIPT),
            "--date",
            date,
            "--daily-root",
            str(daily_root),
            *extra,
        ],
        capture_output=True,
        text=True,
        check=False,
    )


def test_init_daily_workspace_creates_date_folder_with_manual_templates(tmp_path):
    daily_root = tmp_path / "daily"

    result = run_init(daily_root)

    assert result.returncode == 0, result.stderr
    day_dir = daily_root / "2026-06-29"
    assert day_dir.is_dir()
    assert sorted(path.name for path in day_dir.glob("*.json")) == sorted(EXPECTED_FILES)
    todays_bet = json.loads((day_dir / "todays_bet.json").read_text())
    revenue_signal = json.loads((day_dir / "revenue_signal.json").read_text())
    rejection_signal = json.loads((day_dir / "rejection_signal.json").read_text())
    assert todays_bet["date"] == "2026-06-29"
    assert todays_bet["status"] == "planned"
    assert todays_bet["opportunity_id"].startswith("opp_20260629")
    assert "Post-execution placeholder" in revenue_signal["notes"]
    assert "Post-execution placeholder" in rejection_signal["notes"]


def test_init_daily_workspace_from_sample_copies_example_records(tmp_path):
    daily_root = tmp_path / "daily"

    result = run_init(daily_root, "2026-06-29", "--from-sample")

    assert result.returncode == 0, result.stderr
    signal = json.loads((daily_root / "2026-06-29" / "signal.json").read_text())
    assert signal["id"] == "sig_sample_001"
    assert signal["summary"].startswith("Small AI vendor")


def test_init_daily_workspace_refuses_to_overwrite_existing_day(tmp_path):
    daily_root = tmp_path / "daily"
    first = run_init(daily_root)
    second = run_init(daily_root)

    assert first.returncode == 0, first.stderr
    assert second.returncode != 0
    assert "already exists" in second.stderr
