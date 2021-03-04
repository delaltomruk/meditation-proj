import requests
import json


# we will be doing this many times -> use modularization
def get_posts(subreddit_name):
    num_posts = 100

    data = requests.get(f'http://api.reddit.com/r/{subreddit_name}/new?limit={num_posts}', 
                        headers={'User-Agent':'windows: requests (by /u/dtomruk)'})
    
    content = data.json()['data']
    return  (content['children'])


def main():
    
    #subreddit 1 --> sample1.json
    all_subs = ['Meditation', 'Buddhism', 'Mindfulness', 'ZenHabits', 'yoga', 'Meditopia']
    data = []
    sub_posts = []
    for subreddit in all_subs:
        sub_posts = get_posts(subreddit)
        data += sub_posts
    
    j=[]
    for line in data:
        j.append(line)
        
    with open('reddit.json', 'w') as outfile:
        for line in j:
            json.dump(line, outfile)
            outfile.write('\n')
        
    
if __name__=='__main__':
    main()
