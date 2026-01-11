# Contributing to Boot.dev Activity Sync

Thank you for your interest in improving this project! This guide will help you customize and extend the sync functionality.

## 🔧 Customizing the Sync Script

The main sync logic is in `sync_activity.py`. Here are the key areas you might want to customize:

### 1. Boot.dev API Integration

The `fetch_bootdev_activity()` method is where you'll implement the actual Boot.dev API calls:

```python
def fetch_bootdev_activity(self):
    """Fetch activity from Boot.dev API."""
    api_key = os.getenv('BOOTDEV_API_KEY')
    username = os.getenv('BOOTDEV_USERNAME')
    
    # TODO: Replace this with actual Boot.dev API call
    # Example (pseudocode):
    # response = requests.get(
    #     f'https://api.boot.dev/v1/users/{username}/activity',
    #     headers={'Authorization': f'Bearer {api_key}'}
    # )
    # return response.json()
```

### 2. Sync Frequency

Adjust the workflow schedule in `.github/workflows/sync-activity.yml`:

```yaml
on:
  schedule:
    # Change this cron expression to adjust frequency
    - cron: '0 */6 * * *'  # Current: Every 6 hours
    # Examples:
    # - cron: '0 */1 * * *'  # Every hour
    # - cron: '0 0 * * *'    # Once per day at midnight
    # - cron: '0 0,12 * * *' # Twice per day (midnight and noon)
```

### 3. Commit Message Format

Customize the commit messages in `sync_activity.py`:

```python
def create_activity_commit(self, activity):
    # Customize this message format
    commit_message = f"Boot.dev activity: {activity.get('message', 'sync')}"
    
    # You could make it more detailed:
    # commit_message = f"✅ Completed: {activity.get('lesson_name')} on Boot.dev"
```

## 🚀 Adding Features

### Activity Filtering

You might want to only sync certain types of activities:

```python
def should_sync_activity(self, activity):
    """Determine if an activity should be synced."""
    # Only sync lesson completions
    if activity.get('type') == 'lesson_completed':
        return True
    return False
```

### Multiple Commits Per Sync

If you want to create separate commits for each activity:

```python
def sync(self):
    activities = self.fetch_bootdev_activity()
    for activity in activities:
        self.create_activity_commit(activity)
```

### Detailed Activity Logs

Add more information to the activity log:

```python
activity_data["syncs"].append({
    "timestamp": activity["timestamp"],
    "username": activity["username"],
    "activity_type": activity["type"],
    "lesson": activity.get("lesson_name"),
    "course": activity.get("course_name"),
    "points": activity.get("points_earned"),
    "message": activity["message"]
})
```

## 📝 Development Workflow

1. **Fork the repository** to your own account
2. **Clone your fork** locally
3. **Create a branch** for your feature: `git checkout -b feature/my-feature`
4. **Make your changes** and test them locally
5. **Commit your changes**: `git commit -m "Add my feature"`
6. **Push to your fork**: `git push origin feature/my-feature`
7. **Open a Pull Request** to the main repository

## 🧪 Testing

Test your changes locally before pushing:

```bash
# Test with mock credentials
BOOTDEV_API_KEY=test_key BOOTDEV_USERNAME=test_user python sync_activity.py

# Check what would be committed
git status
git diff

# Reset if needed
git reset --hard HEAD
```

## 🐛 Debugging

Enable verbose logging by modifying the script:

```python
import logging

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

# Then use logger.debug() throughout the code
logger.debug(f"Fetched activity: {activity}")
```

## 📚 Resources

- [Boot.dev](https://boot.dev) - Platform documentation
- [GitHub Actions](https://docs.github.com/en/actions) - Workflow documentation
- [Python Requests](https://requests.readthedocs.io/) - For API calls

## ❓ Questions?

If you have questions or need help:

1. Check the README.md for setup instructions
2. Look at the existing code and comments
3. Open an issue on GitHub
4. Reach out to the Boot.dev community

## 📄 Code Style

- Follow PEP 8 for Python code
- Use meaningful variable names
- Add docstrings to functions
- Keep functions focused and small
- Handle errors gracefully

Happy coding! 🎉
