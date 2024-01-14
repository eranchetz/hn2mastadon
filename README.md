Here's a detailed `README.md` file for your project:

---

# Hacker News to Mastodon Poster

This project automatically posts the top story from Hacker News to a Mastodon account once a day.

## Contents

- [Requirements](#requirements)
- [Setup](#setup)
  - [Mastodon API Key](#mastodon-api-key)
  - [Environment Setup](#environment-setup)
- [Usage](#usage)
  - [With Docker](#with-docker)
  - [Without Docker](#without-docker)
- [Automation](#automation)
  - [Cron Job Setup](#cron-job-setup)
- [License](#license)

## Requirements

- Python 3.9 or higher (for running without Docker).
- Docker (optional, for Docker usage).
- A Mastodon account.

## Setup

### Mastodon API Key

To use this script, you need an access token from Mastodon. Follow these steps to get it:

1. **Log in to your Mastodon account.**
2. **Go to Settings > Development > New Application.**
3. **Create an application.**  
   - Application name: `HackerNewsPoster` (or any name you prefer).
   - Redirect URI: `urn:ietf:wg:oauth:2.0:oob`.
   - Scopes: `write`.
4. **Submit to create the application.**
5. **Copy the access token provided.**

### Environment Setup

1. Clone or download this repository to your local machine.
2. Install the necessary Python libraries:
   ```bash
   pip install requests mastodon.py
   ```

## Usage

### With Docker

1. **Create a Dockerfile** in the project directory with the following content:
   ```Dockerfile
   FROM python:3.9-slim
   WORKDIR /app
   COPY . /app
   RUN pip install requests mastodon.py
   CMD ["python", "./hn_to_mastodon.py"]
   ```

2. **Build the Docker image**:
   ```bash
   docker build -t hn_to_mastodon .
   ```

3. **Run the Docker container**:
   ```bash
   docker run --env MASTODON_ACCESS_TOKEN=YOUR_MASTODON_ACCESS_TOKEN hn_to_mastodon
   ```

### Without Docker

1. **Set up your environment** as described in [Environment Setup](#environment-setup).
2. **Run the script**:
   ```bash
   python hn_to_mastodon.py
   ```

## Automation

### Cron Job Setup

To automate the script to run once a day:

1. Open your terminal and enter `crontab -e`.
2. Add the following line to schedule the job (example for 9 AM daily):
   ```
   0 9 * * * /usr/bin/docker run --env MASTODON_ACCESS_TOKEN=YOUR_MASTODON_ACCESS_TOKEN hn_to_mastodon
   ```
3. Save and close the editor.

## License

This project is open source and available under the [MIT License](LICENSE).

---

Remember to replace `YOUR_MASTODON_ACCESS_TOKEN` with the actual token you obtained from Mastodon. This `README.md` provides a comprehensive guide for setting up and running the project, both with and without Docker.
