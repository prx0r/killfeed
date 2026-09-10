# Storage layout

Start simple: raw JSONL partitioned by source/date, normalized Parquet, DuckDB for analysis, NetworkX for dependency/counterfactual graph calculations, SQLite only for lightweight state/dedup.

Suggested tables: `entities`, `dependency_edges`, `signals`, `claims`, `claim_lineage`, `source_calibration`, `market_probabilities`, `security_exposures`, `lab_capital_events`, `patent_families`, `government_awards`, `physical_readings`, `action_board`.

Never overwrite an old dependency edge when architecture changes. Close `valid_to`, create a new state and preserve history for backtesting. Consider Graphiti only after validity-aware queries become painful in DuckDB/Parquet.
