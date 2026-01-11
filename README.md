# Boot.dev Activity Sync

This repository automatically syncs your [Boot.dev](https://boot.dev) activity to your GitHub contribution graph. When you complete lessons, exercises, or other activities on Boot.dev, this repository creates commits to reflect that activity on GitHub.

## 🚀 Features

- **Automatic Syncing**: GitHub Actions runs every 6 hours to sync your Boot.dev activity
- **Manual Trigger**: Sync on-demand using GitHub Actions workflow dispatch
- **Activity Tracking**: Maintains a log of all synced activities in `data/activity.json`
- **Easy Setup**: Simple configuration with environment variables

## 📋 Setup Instructions

### 1. Fork or Clone This Repository

Fork this repository to your own GitHub account, or clone it if you prefer.

### 2. Configure Boot.dev API Credentials

You need to add your Boot.dev credentials as GitHub repository secrets:

1. Go to your repository on GitHub
2. Navigate to **Settings** → **Secrets and variables** → **Actions**
3. Click **New repository secret**
4. Add the following secrets:
   - `BOOTDEV_API_KEY`: Your Boot.dev API key
   - `BOOTDEV_USERNAME`: Your Boot.dev username

**Note**: To get your Boot.dev API key, visit your Boot.dev account settings. If Boot.dev doesn't have a public API yet, you may need to contact their support or wait for API availability.

### 3. Enable GitHub Actions

1. Go to the **Actions** tab in your repository
2. If prompted, enable GitHub Actions for your repository
3. The workflow will now run automatically every 6 hours

### 4. Manual Sync (Optional)

To trigger a sync manually:

1. Go to the **Actions** tab
2. Select the "Sync Boot.dev Activity" workflow
3. Click **Run workflow**
4. Click the green **Run workflow** button

## 🔧 Local Development

You can also run the sync script locally:

### Prerequisites

- Python 3.7 or higher
- Git configured on your machine

### Local Setup

1. Clone the repository:
   ```bash
   git clone https://github.com/YOUR_USERNAME/Boot.dev.git
   cd Boot.dev
   ```

2. Copy the example environment file:
   ```bash
   cp .env.example .env
   ```

3. Edit `.env` and add your Boot.dev credentials:
   ```
   BOOTDEV_API_KEY=your_actual_api_key
   BOOTDEV_USERNAME=your_actual_username
   ```

4. Run the sync script:
   ```bash
   python sync_activity.py
   ```

5. Push the changes to GitHub:
   ```bash
   git push
   ```

## 📁 Repository Structure

```
Boot.dev/
├── .github/
│   └── workflows/
│       └── sync-activity.yml    # GitHub Actions workflow
├── data/
│   └── activity.json            # Activity log (auto-generated)
├── sync_activity.py             # Main sync script
├── .env.example                 # Environment variables template
├── .gitignore                   # Git ignore rules
└── README.md                    # This file
```

## 🔒 Privacy & Security

- Your Boot.dev API key is stored securely as a GitHub secret
- The `.env` file (containing credentials) is ignored by git
- Only activity metadata is committed to the repository

## 🤝 Contributing

This is a personal activity sync repository, but if you have suggestions or improvements, feel free to open an issue or submit a pull request!

## 📝 How It Works

1. **GitHub Actions** triggers the workflow on a schedule (every 6 hours) or manually
2. The **sync script** fetches recent activity from Boot.dev API
3. Activity is logged to `data/activity.json`
4. A git commit is created for the activity
5. Changes are pushed to GitHub, updating your contribution graph

## ⚠️ Important Notes

- **Boot.dev API**: This implementation assumes Boot.dev provides an API for fetching activity. If they don't have a public API yet, you'll need to implement an alternative method (web scraping, manual logging, etc.)
- **Rate Limits**: Be mindful of any API rate limits from Boot.dev
- **Activity Frequency**: The workflow runs every 6 hours by default. Adjust the cron schedule in `.github/workflows/sync-activity.yml` if needed

## 🐛 Troubleshooting

### No commits are being created

- Check that your `BOOTDEV_API_KEY` and `BOOTDEV_USERNAME` secrets are set correctly
- Verify the workflow has permissions to push commits (Settings → Actions → General → Workflow permissions)
- Check the Actions tab for workflow run logs

### Workflow fails

- Review the error logs in the Actions tab
- Ensure Boot.dev API credentials are valid
- Check if Boot.dev API is accessible and working

## 📄 License

This project is open source and available under the MIT License.

## 🔗 Links

- [Boot.dev](https://boot.dev) - Learn backend development
- [GitHub Actions Documentation](https://docs.github.com/en/actions)

---

**Happy coding! 🚀** Keep learning on Boot.dev and watch your GitHub graph light up!
