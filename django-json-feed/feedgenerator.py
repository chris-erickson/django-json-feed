import json

from django.contrib.syndication.views import Feed
from django.utils.feedgenerator import Atom1Feed, SyndicationFeed
from django.core.serializers.json import DjangoJSONEncoder

from .models import Post


class JSONFeed(SyndicationFeed):
    content_type = 'application/json; charset=utf-8'
    version = 'https://jsonfeed.org/version/1'

    # Need to pull these from the feed settings
    title = 'The feed title'

    valid_root_elements = set([
        'version',
        'title',
        'homepage_url',
        'feed_url',
        'description',
        'user_comment',
        'next_url',
        'icon',
        'favicon',
        'author',
        'expired',
        'hubs',
        'items',
    ])

    def write(self, outfile, encoding):
        print(json.dumps(self.feed))
        self.add_root_elements()
        self.add_optional_root_elements()
        self.update_author()
        self.remove_excess_root_elements()
        self.remove_empty_root_elements()
        print(json.dumps(self.feed))

        feed = self.feed
        items = self.items
        feed['items'] = items

        # Write out the feed, fin.
        json.dump(self.feed, outfile, cls=DjangoJSONEncoder)

    def add_root_elements(self):
        """
        Returns the root attributes of the feed.

        version:        required, String
        title:          required, String
        hone_page_url:  optional, String
        feed_url:       optional, String
        description:    optional, String
        user_comment:   optional, String
        next_url:       optional, String
        icon:           optional, String
        favicon:        optional, String
        author:         optional, object
            name:       optional, String
            url:        optional, String
            avatar:     optional, String
        expired:        optional, String
        hubs:           optional, bool
        items:          required, Array (not added here)
        """

        # Required Elements
        self.feed.update({
            'version': self.version,
        })

    def add_optional_root_elements(self):
        """Adds optional root parameters."""
        # TODO: Finish building this
        self.feed.update({'test_optional': "the value" })

    def remove_excess_root_elements(self):
        """Removes unused root parameters that django provides."""

        # TODO: Do this - should this jsut happen in init or si that even all that effective?

        excess_keys = set(self.feed.keys()) - set(self.valid_root_elements)
        for excess_key in excess_keys:
            del self.feed[excess_key]

    def remove_empty_root_elements(self):
        keys =  set(self.feed.keys())

        for key in keys:
            if not self.feed[key]:
                del self.feed[key]


    def update_author(self):
        self.feed['author'] = {
            'name': self.feed['author_name'],
            'url': self.feed['author_link'],
            'avatar': self.feed['author_avatar'],
        }


class PostFeed(Feed):
    feed_type = JSONFeed
    link = "/stuff/"

    # Supplements to the JSON feed
    title = "This is the title"
    # Not provided by django
    homepage_url = "https://homepage.com"
    user_comment = "this is some comment"
    next_url = "not sure what this should be yet"
    icon = "icon"
    favicon = "favicon"
    expired = False
    hubs = ""
    author_avatar = "gravatar link or somehting"

    def feed_extra_kwargs(self, obj):
        """
        Returns an extra keyword arguments dictionary that is used when
        initializing the feed generator.
        """
        return {
            "homepage_url": self.homepage_url,
            "user_comment": self.user_comment,
            "next_url": self.next_url,
            "icon": self.icon,
            "favicon": self.favicon,
            "expired": self.expired,
            "hubs": self.hubs,
            "author_avatar": self.author_avatar,
        }

    def link(self):
        return 'http://www.apple.com'

    def items(self):
        return Post.objects.order_by('-created')[:5]

    def item_title(self, item):
        return item.title
