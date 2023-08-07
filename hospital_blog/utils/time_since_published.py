
from datetime import datetime

def time_since_published(blogs):
    publisheds = []
    for blog in blogs:
        published_time = blog.date_published
        current_time = datetime.now(published_time.tzinfo)
        delta = current_time - published_time

        if delta.days >= 365:
            published = f"{delta.days // 365} years"
        elif delta.days >= 30:
            published = f"{delta.days // 30} months"
        else:
            published = f"{delta.days} days"
        
        published = ' '.join(published.split(' ')[:2])
        publisheds.append(published)
    # if publisheds:
    return publisheds
    
    # else:
    #     return publisheds

