DATE ?= 2026-06-29

.PHONY: sample-output test init-day validate-day validate-ready render-day

sample-output:
	python3 scripts/generate_daily_output.py --sample-dir data/sample --date 2026-06-29

test:
	pytest -q

init-day:
	python3 scripts/init_daily_workspace.py --date $(DATE)

validate-day:
	python3 scripts/validate_records.py --records-dir data/daily/$(DATE)

validate-ready:
	python3 scripts/validate_records.py --records-dir data/daily/$(DATE) --ready

render-day:
	python3 scripts/generate_daily_output.py --records-dir data/daily/$(DATE) --date $(DATE)
