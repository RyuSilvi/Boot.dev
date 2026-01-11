#!/usr/bin/env python3
"""
Boot.dev Activity Sync Script

This script fetches activity data from Boot.dev and creates commits
to sync your Boot.dev activity with your GitHub contribution graph.
"""

import os
import json
import sys
from datetime import datetime
from pathlib import Path
import subprocess


class BootdevActivitySync:
    """Handles syncing Boot.dev activity to GitHub."""
    
    def __init__(self):
        """Initialize the sync manager."""
        self.data_dir = Path(__file__).parent / "data"
        self.data_dir.mkdir(exist_ok=True)
        self.activity_file = self.data_dir / "activity.json"
        
    def load_activity(self):
        """Load existing activity data."""
        if self.activity_file.exists():
            with open(self.activity_file, 'r') as f:
                return json.load(f)
        return {"syncs": []}
    
    def save_activity(self, activity_data):
        """Save activity data to file."""
        with open(self.activity_file, 'w') as f:
            json.dump(activity_data, f, indent=2)
    
    def fetch_bootdev_activity(self):
        """
        Fetch activity from Boot.dev API.
        
        In a real implementation, this would call the Boot.dev API
        to get recent activity (lessons completed, exercises done, etc.)
        
        For now, this is a placeholder that would need to be implemented
        with actual Boot.dev API endpoints.
        """
        api_key = os.getenv('BOOTDEV_API_KEY')
        username = os.getenv('BOOTDEV_USERNAME')
        
        if not api_key or not username:
            print("Warning: BOOTDEV_API_KEY or BOOTDEV_USERNAME not set")
            print("Please set these environment variables to sync activity")
            return None
        
        # TODO: Implement actual Boot.dev API call
        # For now, return a mock activity entry
        print(f"Fetching activity for user: {username}")
        print("Note: This is a placeholder. Implement Boot.dev API integration.")
        
        return {
            "timestamp": datetime.now().isoformat(),
            "username": username,
            "activity_type": "sync",
            "message": "Boot.dev activity sync"
        }
    
    def create_activity_commit(self, activity):
        """Create a git commit for the activity."""
        if not activity:
            print("No activity to commit")
            return False
        
        # Load existing activity
        activity_data = self.load_activity()
        
        # Add new activity
        activity_data["syncs"].append(activity)
        
        # Save updated activity
        self.save_activity(activity_data)
        
        # Create git commit
        try:
            subprocess.run(['git', 'add', str(self.activity_file)], check=True)
            
            commit_message = f"Boot.dev activity: {activity.get('message', 'sync')}"
            subprocess.run(['git', 'commit', '-m', commit_message], check=True)
            
            print(f"✓ Created commit: {commit_message}")
            return True
        except subprocess.CalledProcessError as e:
            print(f"Error creating commit: {e}")
            return False
    
    def sync(self):
        """Main sync method."""
        print("=== Boot.dev Activity Sync ===")
        print(f"Timestamp: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        print()
        
        # Fetch activity from Boot.dev
        activity = self.fetch_bootdev_activity()
        
        if activity:
            # Create commit for the activity
            if self.create_activity_commit(activity):
                print("\n✓ Sync completed successfully")
                return 0
            else:
                print("\n✗ Failed to create commit")
                return 1
        else:
            print("\n✗ No activity to sync")
            return 1


def main():
    """Main entry point."""
    # Load environment variables from .env file if it exists
    env_file = Path(__file__).parent / '.env'
    if env_file.exists():
        with open(env_file) as f:
            for line in f:
                line = line.strip()
                if line and not line.startswith('#') and '=' in line:
                    key, value = line.split('=', 1)
                    os.environ[key] = value
    
    syncer = BootdevActivitySync()
    return syncer.sync()


if __name__ == '__main__':
    sys.exit(main())
