"""
This module contains the tests for the articles services.
"""
from tests.utils import get_resources
from aria.articles.services import summarize_text, SummarizerMode
import json

def test_summarize_text():
    """
    Test the summarize_text function.
    """
    with open(get_resources("long_article.txt"), "r", encoding="utf-8") as file:
        summary = summarize_text(file.read(), SummarizerMode.FAST)
    assert summary is not None


def test_post_article(test_app):
    """
    Test the post method of the ArticleAPI class.
    """
    # create a post request for articles
    client = test_app.test_client()
    content = {
        "title": "test",
        "link": "test",
        "content": "test"
    }
    response = client.post(
        "/api/articles",
        data= json.dumps(content),
        content_type='application/json'
        )
    
    # assert that the response is correct
    assert response.status_code == 201
    assert response.json["title"] == "test"
    assert response.json["link"] == "test"
    assert response.json["content"] == "test"

    # assert that data are present in the database
    from aria import DB as db
    from aria.articles.models import Article
    with test_app.app_context():
        assert len(db.session.query(Article).all()) == 1