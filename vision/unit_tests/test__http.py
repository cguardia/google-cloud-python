# Copyright 2016 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import base64
import unittest

import mock


IMAGE_CONTENT = b'/9j/4QNURXhpZgAASUkq'
PROJECT = 'PROJECT'
B64_IMAGE_CONTENT = base64.b64encode(IMAGE_CONTENT).decode('ascii')


class Test_HTTPVisionAPI(unittest.TestCase):
    def _get_target_class(self):
        from google.cloud.vision._http import _HTTPVisionAPI
        return _HTTPVisionAPI

    def _make_one(self, *args, **kwargs):
        return self._get_target_class()(*args, **kwargs)

    def test_call_annotate_with_no_results(self):
        from google.cloud.vision.feature import Feature
        from google.cloud.vision.feature import FeatureTypes
        from google.cloud.vision.image import Image

        client = mock.Mock(spec_set=['_connection'])
        feature = Feature(FeatureTypes.LABEL_DETECTION, 5)
        image_content = b'abc 1 2 3'
        image = Image(client, content=image_content)

        http_api = self._make_one(client)
        http_api._connection = mock.Mock(spec_set=['api_request'])
        http_api._connection.api_request.return_value = {'responses': []}
        response = http_api.annotate(image, [feature])
        self.assertEqual(len(response), 0)
        self.assertIsInstance(response, list)

    def test_call_annotate_with_more_than_one_result(self):
        from google.cloud.vision.feature import Feature
        from google.cloud.vision.feature import FeatureTypes
        from google.cloud.vision.image import Image
        from google.cloud.vision.likelihood import Likelihood
        from unit_tests._fixtures import MULTIPLE_RESPONSE

        client = mock.Mock(spec_set=['_connection'])
        feature = Feature(FeatureTypes.LABEL_DETECTION, 5)
        image_content = b'abc 1 2 3'
        image = Image(client, content=image_content)

        http_api = self._make_one(client)
        http_api._connection = mock.Mock(spec_set=['api_request'])
        http_api._connection.api_request.return_value = MULTIPLE_RESPONSE
        responses = http_api.annotate(image, [feature])

        self.assertEqual(len(responses), 2)
        image_one = responses[0]
        image_two = responses[1]
        self.assertEqual(len(image_one.labels), 3)
        self.assertIsInstance(image_one.safe_searches, tuple)
        self.assertEqual(image_two.safe_searches.adult,
                         Likelihood.VERY_UNLIKELY)
        self.assertEqual(len(image_two.labels), 0)


class TestVisionRequest(unittest.TestCase):
    @staticmethod
    def _get_target_function():
        from google.cloud.vision._http import _make_request
        return _make_request

    def _call_fut(self, *args, **kw):
        return self._get_target_function()(*args, **kw)

    def test_call_vision_request(self):
        from google.cloud.vision.feature import Feature
        from google.cloud.vision.feature import FeatureTypes
        from google.cloud.vision.image import Image

        client = object()
        image = Image(client, content=IMAGE_CONTENT)
        feature = Feature(feature_type=FeatureTypes.FACE_DETECTION,
                          max_results=3)
        request = self._call_fut(image, feature)
        self.assertEqual(request['image'].get('content'), B64_IMAGE_CONTENT)
        features = request['features']
        self.assertEqual(len(features), 1)
        feature = features[0]
        self.assertEqual(feature['type'], FeatureTypes.FACE_DETECTION)
        self.assertEqual(feature['maxResults'], 3)

    def test_call_vision_request_with_not_feature(self):
        from google.cloud.vision.image import Image

        client = object()
        image = Image(client, content=IMAGE_CONTENT)
        with self.assertRaises(TypeError):
            self._call_fut(image, 'nonsensefeature')

    def test_call_vision_request_with_list_bad_features(self):
        from google.cloud.vision.image import Image

        client = object()
        image = Image(client, content=IMAGE_CONTENT)
        with self.assertRaises(TypeError):
            self._call_fut(image, ['nonsensefeature'])
