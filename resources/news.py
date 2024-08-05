from flask_restful import Resource, reqparse
from flask import request
from datetime import datetime
from models import News, db

# Create a request parser for adding news articles
news_parser = reqparse.RequestParser()
news_parser.add_argument('image_url', type=str, required=True, help='Image URL is required')
news_parser.add_argument('description', type=str, required=True, help='Content is required')
news_parser.add_argument('location', type=str, required=True, help='Location is required')
news_parser.add_argument('ticket_price', type=str, required=True, help='Title is required')
news_parser.add_argument('date', type=lambda x: datetime.strptime(x, '%Y-%m-%d'), required=True, help='Publication date is required (YYYY-MM-DD)')

class NewsResource(Resource):
    def get(self):
        news_articles = News.query.all()
        return [article.to_dict() for article in news_articles], 200

    def post(self):
        data = request.get_json()
        news_article = News(
            image_url=data['image_url'],
            description=data['description'],
            location=data['location'],
            ticket_price=data['ticket_price'],
            date=data['date']
        )
        db.session.add(news_article)
        db.session.commit()
        return news_article.to_dict(), 201