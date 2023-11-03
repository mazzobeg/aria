from flask_restx import Resource, Namespace
from aria.articles.models import article_input_model, article_model, Article
from aria import DB as db
from sqlalchemy.exc import IntegrityError
import logging as log

ns = Namespace("api")

@ns.route("/articles")
class ArticleAPI(Resource):
    @ns.expect(article_input_model)
    @ns.marshal_with(article_model)
    def post(self):
        article = Article(
            title=ns.payload["title"],
            link=ns.payload["link"],
            content=ns.payload["content"],
        )
        try:
            db.session.add(article)
            db.session.commit()
            return article, 201
        except IntegrityError:
            log.debug("Article already in database")
            return article, 500