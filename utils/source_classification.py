# -*- coding: iso-8859-1 -*-

"""This script classifies a source used to post a tweet.

The string to be classified as manual or automated is extracted from the source
field. For more information check at https://dev.twitter.com/overview/api/tweets

Example
-------
>>> # the source extracted from tweet to be classified
>>> source = "<a href=\"http://itunes.apple.com/us/app/twitter/id409789998?mt=12\" rel=\"nofollow\">Twitter for Mac</a>"
>>> # split source into source_name and source_url
>>> source_name, source_url = split_tweeting_source(source)
>>> # classify the source
>>> 'manual' if is_a_manual_tweeting_source(source_name, source_url) else 'automated'

"""


import re


# Each item (i.e., a source definition) in the following list is a
# one-dimensional array whose index 0 is the regular expression (regex)
# which matches the source name; instead, index 1 is the regex which
# matches the source URL, when it corresponds.
# Note that "tweets from the Twitter website have a source value of web."
MANUAL_SOURCES_RE = [
    [
        r'twitter for (?:android|iphone|ipad|samsung)',
        r'https?://(?:www\.)?twitter\.com/(?:#!/)?download/(?:android|iphone|ipad)'],
    [
        r'twitter for (?:windows|blackberry|mediatek)',
        r'https?://(?:www\.)?twitter\.com'],
    [r'twitter for blackberry', r'https?://blackberry\.com/twitter'],
    [r'twitter web client', r'https?://twitter\.com'],
    [r'tweetdeck', r'https?://about\.twitter\.com/products/tweetdeck'],
    [r'twitter for websites', r'https?://dev\.twitter\.com/docs/tfw'],
    [r'mobile web', r'https?://mobile\.twitter\.com'],
    [r'^(?:ios|os x)', r'https?://(?:www\.)?apple\.com'],
    [
        r'tweetcaster for (?:android|ios)', 
        r'(?:https?://(?:www\.)?tweetcaster\.com|https?://(?:www\.)?handmark\.com)'],
    [
        r'twitter for mac',
        r'https?://itunes\.apple\.com/us/app/twitter/id409789998\?mt=12'],
    [
        r'tweetbot for (?:ios|mac)',
        r'https?://(?:www\.)?tapbots\.com/(?:software/)?tweetbot'],
    [
        r'ubersocial(?: pro)? for (?:android|blackberry|iphone)',
        r'https?://(?:www\.)?ubersocial\.com'],
    [
        r'ubersocial pro for iphone', 
        r'https?://itunes\.apple\.com/us/app/ubersocial-pro-for-iphone/id580192609\?mt=8&uo=4'],
    [r'twitter for nokia s40', r'https?://store\.ovi\.com/content/256340'],
    [r'echofon', r'https?://(?:www\.)?echofon\.com'],
    [r'windows phone', r'https?://(?:www\.)?windowsphone\.com'],
    [r'plume for android', r'https?://(?:www\.)?myplume\.com'],
    [r'samsung mobile', r'https?://(?:www\.)?samsungmobile\.com'],
    [r'social by nokia', r'https?://messaging\.nokia\.com'],
    [r'twicca', r'https?://twicca\.r246\.jp'],
    [r'fenix for android', r'https?://(?:www\.)?mvilla\.it'],
    [r'lg phone', r'https?://(?:www\.)?lg\.com'],
    [r'jigtwi', r'https?://jigtwi\.jp'],
    [r'carbon for android', r'https?://(?:www\.)?twitter\.com/carbonandroid'],
    [r'carbon v2', r'https?://(?:www\.)?gplus\.to/carbonandroid'],
    [r'kindle', r'https?://kindle\.amazon\.com'],
    [r'twidere for android', r'https?://play\.google\.com/store/apps/'],
    [r'motorola mtweet', r'https?://(?:www\.)?motorola\.com'],
    [r'silver bird', r'https?://chrome\.google\.com'],
    [r'peregrine', r'https?://(?:www\.)?windowsphone\.com'],
    [r'tweetings for android', r'https?://play\.google\.com/store/apps/'],
    [r'twitterrific', r'https?://(?:www\.)?twitterrific\.com'],
    [r'dotgo sms', r'https?://(?:www\.)?dotgo\.com/res/twitter/'],
    [r'twittelator', r'https?://(?:www\.)?stone\.com/twittelator'],
    [r'twittnuker', r'https?://(?:www\.)?twittnuker\.org'],
    [r'blaq for blackberry', r'https?://(?:www\.)?backtoblaq\.com'],
    [r'turpial', r'https?://(?:www\.)?turpial\.org\.ve'],
    [
        r'falcon (?:pro|for android)',
        r'(?:https?://(?:www\.)?getfalcon\.pro|https?://(?:www\.)?twitter\.com/(?:#!/)?joenrv)'],
    [r'talon plus', r'https?://(?:www\.)?klinkerapps\.com'],
    [r'metrotwit', r'https?://(?:www\.)?metrotwit\.com'],
    [r'cloudhopper', r'https?://(?:www\.)?cloudhopper\.com'],
    [r'sony xperia tm smartphone', r'https?://(?:www\.)?sonymobile\.com'],
    [r'samsung smart tv', r'https?://(?:www\.)?samsung\.com/apps'],
    [r'safari on ios', r'https?://(?:www\.)?apple\.com'],
    [r'web', None],
    [r'bravia', r'https?://(?:www\.)?sony\.jp/bravia/technology/applicast/'],
    [r'alcatel mtweet', r'https?://(?:www\.)?alcatel-mobilephones\.com'],
    [r'tweet it for wp8', r'https?://(?:www\.)?windowsphone\.com'],
    [r'sony ericsson xperia tm play', r'https?://(?:www\.)?sonyericsson\.com']
]

SOURCE_RE = re.compile(
    r"""<a href=(?:"|')(.+)(?:"|') rel=.+>(.+)</a>""",
    re.I | re.UNICODE)


def split_tweeting_source(source):
    """Split the tweeting source into source name and source url.
    """
    source = source.decode("utf-8") if (isinstance(source, str)) else source

    match = SOURCE_RE.search(source)
    if match:
        source_url, source_name = match.groups()
    else:
        source_url, source_name = None, source

    source_name = re.sub(r'\s{2,}', ' ', 
        re.sub('\W', ' ', source_name, flags=re.UNICODE).strip()).lower()

    return source_name, source_url


def is_a_manual_tweeting_source(source_name, source_url):
    """Return True if the source is a manual tweeting source.
    """
    is_a_manual_source = False
    for source_re in MANUAL_SOURCES_RE:
        if (source_name is not None and source_url is not None
                and re.search(source_re[0], source_name, re.I)
                and source_re[1] is not None
                and re.search(source_re[1], source_url, re.I)):
            is_a_manual_source = True
            break
        elif (source_name is not None and source_url is None
                and re.search(source_re[0], source_name, re.I)
                and source_re[1] is None):
            is_a_manual_source = True
            break
    return is_a_manual_source

