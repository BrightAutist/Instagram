target_profile = 'erling.haaland'

from instaloader import Instaloader, Profile
loader = Instaloader()

profile = Profile.from_username(loader.context, target_profile)

num_followers = profile.followers
total_num_likes = 0
total_num_comments = 0
total_num_posts = 0

counter = 0
poststocount = 10
for post in profile.get_posts():
    if(counter >= poststocount):
        break
    total_num_likes += post.likes
    total_num_comments += post.comments
    total_num_posts += 1


engagement = float(total_num_likes + total_num_comments) / (num_followers * total_num_posts)
print(engagement * 100)