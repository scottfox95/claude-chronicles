#!/usr/bin/env python3
"""Save an X thread draft from a Claude Chronicles markdown file."""

import sys
import re
import json
from pathlib import Path
from datetime import datetime


def parse_thread(filepath: str) -> list[str]:
    """Extract tweets from a thread markdown file."""
    content = Path(filepath).read_text()

    # Match numbered tweets: **1/** through **N/**
    pattern = r'\*\*\d+/\*\*\s*\n(.*?)(?=\n\*\*\d+/\*\*|\n---|\Z)'
    matches = re.findall(pattern, content, re.DOTALL)

    tweets = []
    for match in matches:
        tweet = match.strip()
        if tweet:
            tweets.append(tweet)

    return tweets


def save_draft(filepath: str, dry_run: bool = False):
    """Save a thread as a local draft for manual posting on X."""
    tweets = parse_thread(filepath)

    if not tweets:
        print("No tweets found in file.")
        sys.exit(1)

    # Validate character counts
    for i, tweet in enumerate(tweets, 1):
        if len(tweet) > 280:
            print(f"Tweet {i} is {len(tweet)} chars (max 280):")
            print(f"  {tweet[:80]}...")
            sys.exit(1)

    print(f"Thread: {len(tweets)} tweets")
    for i, tweet in enumerate(tweets, 1):
        print(f"\n  [{i}/{len(tweets)}] ({len(tweet)} chars)")
        print(f"  {tweet[:100]}{'...' if len(tweet) > 100 else ''}")

    if dry_run:
        print("\n[DRY RUN] No draft saved.")
        return

    # Save draft as JSON for easy copy-paste when posting manually
    drafts_dir = Path(__file__).parent / 'drafts'
    drafts_dir.mkdir(exist_ok=True)

    source_name = Path(filepath).stem
    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
    draft_path = drafts_dir / f"{source_name}_{timestamp}.json"

    draft = {
        'source': filepath,
        'created_at': datetime.now().isoformat(),
        'tweet_count': len(tweets),
        'tweets': [
            {'index': i, 'text': tweet, 'chars': len(tweet)}
            for i, tweet in enumerate(tweets, 1)
        ],
    }

    draft_path.write_text(json.dumps(draft, indent=2))
    print(f"\nDraft saved to: {draft_path}")

    # Also save a plain text version for easy copy-paste
    txt_path = draft_path.with_suffix('.txt')
    lines = []
    for i, tweet in enumerate(tweets, 1):
        lines.append(f"--- Tweet {i}/{len(tweets)} ({len(tweet)} chars) ---")
        lines.append(tweet)
        lines.append("")
    txt_path.write_text("\n".join(lines))
    print(f"Plain text copy-paste version: {txt_path}")

    print(f"\nReady to post! Open X and copy each tweet from the draft files above.")


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Usage: python3 post_thread.py <thread.md> [--dry-run]")
        sys.exit(1)

    filepath = sys.argv[1]
    dry_run = '--dry-run' in sys.argv
    save_draft(filepath, dry_run)
