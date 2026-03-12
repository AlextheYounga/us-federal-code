#!/usr/bin/env python3
"""
Rename all directories with ':' in their names to use '-' instead.
Also collapses resulting '--' (from ':-' patterns) to single '-'.
Uses `git mv` so renames are tracked by Git.

Usage:
    python3 fix_colon_names.py [repo_path]

    repo_path defaults to the current working directory.
"""
import os
import subprocess
import sys


def find_dirs_with(pattern, repo):
    matches = []
    for dirpath, dirnames, _ in os.walk(repo):
        dirnames[:] = [d for d in dirnames if d != ".git"]
        for d in dirnames:
            if pattern in d:
                matches.append(os.path.join(dirpath, d))
    # Deepest first so nested renames don't break parent paths
    matches.sort(key=lambda p: p.count(os.sep), reverse=True)
    return matches


def git_mv(old, new, repo):
    result = subprocess.run(
        ["git", "mv", old, new],
        capture_output=True, text=True, cwd=repo
    )
    if result.returncode != 0:
        print(f"  ERROR: {result.stderr.strip()}", file=sys.stderr)
        return False
    return True


def rename_all(dirs, replace_from, replace_to, repo):
    renamed = errors = 0
    for old_path in dirs:
        parent = os.path.dirname(old_path)
        old_name = os.path.basename(old_path)
        new_name = old_name.replace(replace_from, replace_to)
        if new_name == old_name:
            continue
        new_path = os.path.join(parent, new_name)
        if git_mv(old_path, new_path, repo):
            print(f"  {old_name}\n  -> {new_name}\n")
            renamed += 1
        else:
            errors += 1
    return renamed, errors


def main():
    repo = sys.argv[1] if len(sys.argv) > 1 else os.getcwd()
    repo = os.path.abspath(repo)
    print(f"Repo: {repo}\n")

    # Pass 1: replace ':' with '-'
    colon_dirs = find_dirs_with(":", repo)
    print(f"Found {len(colon_dirs)} directories with ':'.\n")
    renamed1, errors1 = rename_all(colon_dirs, ":", "-", repo)

    # Pass 2: collapse '--' to '-' (produced by ':-' patterns)
    double_dirs = find_dirs_with("--", repo)
    print(f"Found {len(double_dirs)} directories with '--'.\n")
    renamed2, errors2 = rename_all(double_dirs, "--", "-", repo)

    total_errors = errors1 + errors2
    print(f"Done: {renamed1} colon renames, {renamed2} double-hyphen fixes, "
          f"{total_errors} errors.")
    if total_errors:
        sys.exit(1)


if __name__ == "__main__":
    main()
