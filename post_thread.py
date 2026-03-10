#!/usr/bin/env python3
"""Post an X thread from a Claude Chronicles markdown file."""

import sys
import re
import time
from pathlib import Path
from dotenv import load_dotenv
import os
import tweepy

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


def post_thread(filepath: str, dry_run: bool = False):
    """Post a thread to X."""
    load_dotenv(Path(__file__).parent / '.env')

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
        print("\n[DRY RUN] No tweets posted.")
        return

    client = tweepy.Client(
        consumer_key=os.environ['X_CONSUMER_KEY'],
        consumer_secret=os.environ['X_CONSUMER_SECRET'],
        access_token=os.environ['X_ACCESS_TOKEN'],
        access_token_secret=os.environ['X_ACCESS_TOKEN_SECRET'],
    )

    print("\nPosting...")
    previous_id = None
    for i, tweet in enumerate(tweets, 1):
        response = client.create_tweet(
            text=tweet,
            in_reply_to_tweet_id=previous_id,
        )
        previous_id = response.data['id']
        print(f"  Posted tweet {i}/{len(tweets)} (id: {previous_id})")
        if i < len(tweets):
            time.sleep(1)  # Be nice to the API

    print(f"\nThread posted! https://x.com/scottfox95/status/{tweets and previous_id}")


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Usage: python3 post_thread.py <thread.md> [--dry-run]")
        sys.exit(1)

    filepath = sys.argv[1]
    dry_run = '--dry-run' in sys.argv
    post_thread(filepath, dry_run)
