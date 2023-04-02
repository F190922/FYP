from rest_framework import viewsets
from rest_framework.response import Response
from rank_bm25 import BM25Okapi
from .models import Article
from .serializers import ArticleSerializer
import pymongo

class ArticleViewSet(viewsets.ViewSet):
    def list(self, request):
        # Connect to MongoDB
        client = pymongo.MongoClient("mongodb://localhost:27017/")
        db = client["cnn_data"]
        collection = db["articles"]

        # Fetch all documents from collection
        documents = []
        for doc in collection.find():
            documents.append(doc['text'])

        # Build the BM25 index
        tokenized_docs = [doc.split(" ") for doc in documents]
        bm25 = BM25Okapi(tokenized_docs)

        # Ask user for input to search
        query = request.GET.get('q', '')  # retrieve query from request

        # Retrieve relevant documents
        tokenized_query = query.split(" ")
        doc_scores = bm25.get_scores(tokenized_query)
        relevant_docs = [(score, doc) for score, doc in zip(doc_scores, documents)]
        relevant_docs.sort(reverse=True)

        # Return top 10 results
        results = []
        for i in range(10):
            if i >= len(relevant_docs):
                break
            results.append({'score': relevant_docs[i][0], 'text': relevant_docs[i][1]})

        serializer = ArticleSerializer(results, many=True)
        return Response(serializer.data)
