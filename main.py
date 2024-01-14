import requests
from mastodon import Mastodon

# Retrieve access token from environment variable
MASTODON_ACCESS_TOKEN = os.getenv('MASTODON_ACCESS_TOKEN')
if not MASTODON_ACCESS_TOKEN:
    raise ValueError("MASTODON_ACCESS_TOKEN environment variable is not set")

# Configuration (Fill these in with your details)
MASTODON_API_BASE_URL = 'https://tooot.im'  # Change if using a different instance
HACKER_NEWS_API_URL = 'https://hacker-news.firebaseio.com/v0'

def get_top_hacker_news_story():
    top_stories_response = requests.get(f"{HACKER_NEWS_API_URL}/topstories.json")
    top_story_id = top_stories_response.json()[0]
    top_story_response = requests.get(f"{HACKER_NEWS_API_URL}/item/{top_story_id}.json")
    return top_story_response.json()

def post_to_mastodon(story):
    mastodon = Mastodon(access_token=MASTODON_ACCESS_TOKEN, api_base_url=MASTODON_API_BASE_URL)
    title = story.get('title', 'No Title')
    url = story.get('url', '')
    post_text = f"{title}\n{url}"
    mastodon.status_post(post_text)

def main():
    top_story = get_top_hacker_news_story()
    post_to_mastodon(top_story)

if __name__ == "__main__":
    main()

