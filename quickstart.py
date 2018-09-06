from instapy import InstaPy

session = InstaPy(username='', password='')

session.login()

session.set_relationship_bounds (enabled=True, potency_ratio=None, delimit_by_numbers=True, max_followers=22668, max_following=10200, min_followers=0, min_following=0)
session.set_do_follow(enabled=False, percentage=100)
session.set_do_like(True, percentage=100)
session.interact_by_users(['vesselgolf'], amount=150, randomize=False, media='Photo')


session.end()