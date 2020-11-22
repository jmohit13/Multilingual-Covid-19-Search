import json
import logging
from django.http import JsonResponse
from rest_framework import views
from rest_framework import status
from rest_framework.response import Response
from .utilities import get_semantic_similarity, detect_lang
from .apps import AppConfig

_LOGGER = logging.getLogger("django")

class Similarity(views.APIView):
    def post(self, request):
        req_json = json.loads(request.body)
        query = req_json["text"]

        if query != "":
            query_lang = detect_lang(query)
            query_vec = AppConfig.laser.embed_sentences(query, lang=query_lang)
            try:
                similar_docs = get_semantic_similarity(
                    query_vec,
                    AppConfig.PROCESSED_DATA_LOADED,
                    AppConfig.BASE_VECTORS_LOADED,
                    AppConfig.df,
                )
                _LOGGER.info(
                    "Found Similar Docs for the Query"
                )
                message = {
                    "text": query,
                    "result": similar_docs,
                }
            except Exception as err:
                _LOGGER.error(str(err))
                return Response(str(err), status=status.HTTP_400_BAD_REQUEST)

        return JsonResponse(message, status=status.HTTP_200_OK)
