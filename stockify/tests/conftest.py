import os
from pathlib import Path

TEST_DB = Path(__file__).parent / "test_stockify.db"
if TEST_DB.exists():
    TEST_DB.unlink()
os.environ["STOCKIFY_DATABASE_URL"] = f"sqlite:///{TEST_DB}"
os.environ["STOCKIFY_PUBLIC_BASE_URL"] = "http://testserver"
