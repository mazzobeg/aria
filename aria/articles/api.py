from flask_restx import Resource, Namespace
from aria.articles.models import article_input_model, article_model, Article
from aria import DB as db

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
        db.session.add(article)
        db.session.commit()
        return article, 201