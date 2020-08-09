import json
import pytest

from rest_framework import status
from rest_framework.reverse import reverse


@pytest.mark.django_db
def test_shop_product_post(client):
    url = reverse(viewname='product-list')
    data = {
        'name': 'TestProduct',
        'option_set': [
            {
                'name': 'TestOption1',
                'price': 1000
            },
            {
                'name': 'TestOption2',
                'price': 500
            },
            {
                'name': 'TestOption3',
                'price': 0
            }
        ],
        'tag_set': [
            {
                'pk': 1,
                'name': 'ExistTag'
            },
            {
                'name': 'NewTag'
            }
        ]
    }
    response = client.post(url, json.dumps(data), content_type='application/json')
    assert response.status_code == status.HTTP_201_CREATED
