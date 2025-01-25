import praw
from prawcore.exceptions import NotFound, PrawcoreException
from transformers import pipeline
pipe = pipeline("text-classification", model="tabularisai/multilingual-sentiment-analysis")
from Ingester.models import Comments

reddit = praw.Reddit(
    client_id='5zbmu2suUNmCsK0Fup9p0A',
    client_secret='z3GdZEske7oLRUnC8V6-hqqcbqtt0Q',
    user_agent='Ingester'
)


def retrieve_from_reddit(subreddit, subject, user, count=100):
    try:
        subreddit = reddit.subreddit(subreddit)
        for submission in subreddit.search(subject, sort='hot', limit=count):  # Adjust limit as needed
            submission.comments.replace_more(limit=count)
            for comment in submission.comments.list():
                try:
                    result = pipe(comment.body)
                    # Print the result
                    comment = Comments(
                        title=submission.title,
                        content=comment.body,
                        url=submission.url,
                        score=submission.score,
                        author=user,
                        subreddit=subreddit,
                        subject=subject,
                        sentiment=result[0]['label'],
                        sentiment_score=result[0]['score'],
                        user=user
                    )
                    comment.save()
                except Exception:
                    continue


    except NotFound as e:
        print(f"Error: {e} - The subreddit or submission was not found.")
    except PrawcoreException as e:
        print(f"Error: {e} - A PRAW core exception occurred.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
