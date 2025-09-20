from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response

from api.constants.custom_reponse import APIResponse


class Pagination(PageNumberPagination):
    default_message = "Success"

    def get_paginated_response(self, data, message=None):
        paginated_data = {
            'next': self.get_next_link(),
            'previous': self.get_previous_link(),
            'total_items': self.page.paginator.count,
            'total_page': self.page.paginator.num_pages
        }
        return APIResponse(
            data=data,
            message=message or self.default_message,
            status=200,
            extra={'page' : paginated_data}
        )
