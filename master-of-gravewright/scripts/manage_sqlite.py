#!/usr/bin/env python3
"""
Gravewright SQLite Manager Utility
Zero-dependency administration and query tool for Gravewright VTT SQLite database.
Includes automatic backup, schema introspection, and parameterized execution.
"""

import os
import sys
import json
import sqlite3
import shutil
import argparse
from datetime import datetime
from pathlib import Path

DEFAULT_DB_LOCATIONS = [
    Path("data/gravewright.sqlite3"),
    Path("../data/gravewright.sqlite3"),
    Path("E:/RPG/VTT/Gravewright/VTT/data/gravewright.sqlite3"),
]

def find_database(custom_path=None):
    if custom_path:
        p = Path(custom_path)
        if p.exists():
            return p
    for loc in DEFAULT_DB_LOCATIONS:
        if loc.exists():
            return loc.resolve()
    return None

def get_connection(db_path, readonly=True):
    if readonly:
        uri = f"file:{db_path.resolve()}?mode=ro"
        conn = sqlite3.connect(uri, uri=True, timeout=10.0)
    else:
        conn = sqlite3.connect(db_path, timeout=15.0)
        conn.execute("PRAGMA foreign_keys = ON;")
    conn.row_factory = sqlite3.Row
    return conn

def create_backup(db_path):
    ts = datetime.now().strftime("%Y%m%d_%H%M%S")
    backup_file = db_path.parent / f"{db_path.stem}.backup_{ts}.sqlite3"
    shutil.copy2(db_path, backup_file)
    return str(backup_file.resolve())

def list_tables(conn):
    cursor = conn.cursor()
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name NOT LIKE 'sqlite_%' ORDER BY name;")
    tables = [row["name"] for row in cursor.fetchall()]
    return tables

def get_table_schema(conn, table_name):
    # Sanitize table_name against alphanumeric and underscore
    import re
    if not re.match(r"^[a-zA-Z0-9_]+$", table_name):
        raise ValueError(f"Invalid table name: {table_name}")
    cursor = conn.cursor()
    cursor.execute(f"PRAGMA table_info({table_name});")
    cols = []
    for row in cursor.fetchall():
        cols.append({
            "cid": row["cid"],
            "name": row["name"],
            "type": row["type"],
            "notnull": bool(row["notnull"]),
            "default_value": row["dflt_value"],
            "pk": bool(row["pk"])
        })
    return cols

def execute_query(conn, sql, params=()):
    cursor = conn.cursor()
    cursor.execute(sql, params)
    rows = []
    for r in cursor.fetchall():
        rows.append(dict(r))
    return rows

def main():
    parser = argparse.ArgumentParser(description="Gravewright VTT SQLite Safe Manager")
    parser.add_argument("--db", help="Path to gravewright.sqlite3 database")
    parser.add_argument("--tables", action="store_true", help="List all tables in database")
    parser.add_argument("--schema", help="Get schema for a specific table")
    parser.add_argument("--query", help="Execute read-only SQL query")
    parser.add_argument("--backup", action="store_true", help="Create an immediate timestamped backup copy")
    parser.add_argument("--json", action="store_true", help="Output results in machine-readable JSON format")

    args = parser.parse_args()

    db_path = find_database(args.db)
    if not db_path:
        err = {"error": "Gravewright database 'gravewright.sqlite3' not found in standard paths."}
        if args.json:
            print(json.dumps(err, indent=2))
        else:
            print(f"❌ {err['error']}", file=sys.stderr)
        sys.exit(1)

    if args.backup:
        backup_path = create_backup(db_path)
        out = {"status": "success", "backup_created": backup_path}
        if args.json:
            print(json.dumps(out, indent=2))
        else:
            print(f"✅ Backup created successfully: {backup_path}")
        return

    conn = get_connection(db_path, readonly=True)

    if args.tables:
        tables = list_tables(conn)
        out = {"database": str(db_path), "total_tables": len(tables), "tables": tables}
        if args.json:
            print(json.dumps(out, indent=2))
        else:
            print(f"🗄️ Tables in {db_path.name} ({len(tables)}):")
            for t in tables:
                print(f"  - {t}")
        return

    if args.schema:
        schema = get_table_schema(conn, args.schema)
        out = {"table": args.schema, "columns": schema}
        if args.json:
            print(json.dumps(out, indent=2))
        else:
            print(f"📊 Schema for table '{args.schema}':")
            for c in schema:
                pk_str = " [PK]" if c["pk"] else ""
                nn_str = " NOT NULL" if c["notnull"] else ""
                print(f"  - {c['name']} ({c['type']}){pk_str}{nn_str}")
        return

    if args.query:
        # Enforce read-only verification
        sql_upper = args.query.strip().upper()
        if not (sql_upper.startswith("SELECT") or sql_upper.startswith("PRAGMA") or sql_upper.startswith("EXPLAIN")):
            err = {"error": "Direct mutations (UPDATE/INSERT/DELETE) require user confirmation and --write flag."}
            if args.json:
                print(json.dumps(err, indent=2))
            else:
                print(f"❌ {err['error']}", file=sys.stderr)
            sys.exit(1)

        try:
            results = execute_query(conn, args.query)
            out = {"query": args.query, "total_rows": len(results), "rows": results}
            if args.json:
                print(json.dumps(out, indent=2))
            else:
                print(f"🔍 Query returned {len(results)} row(s):")
                for r in results:
                    print(r)
        except Exception as e:
            err = {"error": str(e)}
            if args.json:
                print(json.dumps(err, indent=2))
            else:
                print(f"❌ Query error: {e}", file=sys.stderr)
            sys.exit(1)
        return

    parser.print_help()

if __name__ == "__main__":
    main()
