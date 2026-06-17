import sys
from pathlib import Path
from datetime import datetime

import pytest
from pytest_html import extras as extras_module

sys.path.insert(0, str(Path(__file__).parent))


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()

    if report.when == "call" and report.failed:
        if "page" in item.funcargs:
            page = item.funcargs["page"]
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            screenshots_dir = Path("reports/screenshots")
            screenshots_dir.mkdir(parents=True, exist_ok=True)
            screenshot_path = screenshots_dir / f"{item.name}_failed_{timestamp}.png"
            page.screenshot(path=str(screenshot_path))
            extras = getattr(report, "extras", [])
            extras.append(extras_module.image(f"screenshots/{screenshot_path.name}"))
            report.extras = extras
