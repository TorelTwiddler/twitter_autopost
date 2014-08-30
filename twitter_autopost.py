import twitter
import ConfigParser
import sqlite3


def get_twitter_api():
    """
    Gets the python-twitter api using the credentials saved in 'twitter.cfg'.

    :return: The API object used to communicate to Twitter.
    :rtype: twitter.Api
    """
    config = ConfigParser.SafeConfigParser()
    config.read('twitter.cfg')
    consumer_key = config.get('Twitter Credentials', 'consumer_key')
    consumer_secret = config.get('Twitter Credentials', 'consumer_secret')
    access_token = config.get('Twitter Credentials', 'access_token')
    access_token_secret = config.get('Twitter Credentials', 'access_token_secret')

    api = twitter.Api(consumer_key=consumer_key, consumer_secret=consumer_secret,
                      access_token_key=access_token, access_token_secret=access_token_secret)
    return api


def get_database():
    """
    Gets the sqlite3 database that holds the information to be posted.
    :return:
    """
    db = sqlite3.connect('database.db')
    return db


def setup_database():
    """
    Sets up the database for first use.
    """
    db = get_database()
    cursor = db.cursor()
    cursor.execute("CREATE TABLE sentences (sentence text, when_to_post text, posted integer)")
    db.commit()
    db.close()


def main():
    """
    The main function, called directly.
    :return:
    """
    # api = get_twitter_api()
    # api.PostUpdate()
