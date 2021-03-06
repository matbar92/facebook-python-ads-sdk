# Copyright 2014 Facebook, Inc.

# You are hereby granted a non-exclusive, worldwide, royalty-free license to
# use, copy, modify, and distribute this software in source code or binary
# form for use in connection with the web services and APIs provided by
# Facebook.

# As with any software that integrates with the Facebook platform, your use
# of this software is subject to the Facebook Developer Principles and
# Policies [http://developers.facebook.com/policy/]. This copyright notice
# shall be included in all copies or substantial portions of the software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL
# THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
# FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER
# DEALINGS IN THE SOFTWARE.

from facebookads.adobjects.abstractobject import AbstractObject

"""
This class is auto-generated.

For any issues or feature requests related to this class, please let us know on
github and we'll fix in our codegen framework. We'll not be able to accept
pull request for this class.
"""

class AdCreativeLinkData(
    AbstractObject,
):

    def __init__(self, api=None):
        super(AdCreativeLinkData, self).__init__()
        self._isAdCreativeLinkData = True
        self._api = api

    class Field(AbstractObject.Field):
        additional_image_index = 'additional_image_index'
        app_link_spec = 'app_link_spec'
        attachment_style = 'attachment_style'
        branded_content_sponsor_page_id = 'branded_content_sponsor_page_id'
        branded_content_sponsor_relationship = 'branded_content_sponsor_relationship'
        call_to_action = 'call_to_action'
        caption = 'caption'
        child_attachments = 'child_attachments'
        description = 'description'
        event_id = 'event_id'
        force_single_link = 'force_single_link'
        image_crops = 'image_crops'
        image_hash = 'image_hash'
        link = 'link'
        message = 'message'
        multi_share_end_card = 'multi_share_end_card'
        multi_share_optimized = 'multi_share_optimized'
        name = 'name'
        offer_id = 'offer_id'
        page_welcome_message = 'page_welcome_message'
        picture = 'picture'
        retailer_item_ids = 'retailer_item_ids'
        show_multiple_images = 'show_multiple_images'

    class AttachmentStyle:
        link = 'link'
        value_default = 'default'

    _field_types = {
        'additional_image_index': 'int',
        'app_link_spec': 'AdCreativeLinkDataAppLinkSpec',
        'attachment_style': 'AttachmentStyle',
        'branded_content_sponsor_page_id': 'string',
        'branded_content_sponsor_relationship': 'string',
        'call_to_action': 'AdCreativeLinkDataCallToAction',
        'caption': 'string',
        'child_attachments': 'list<AdCreativeLinkDataChildAttachment>',
        'description': 'string',
        'event_id': 'string',
        'force_single_link': 'bool',
        'image_crops': 'AdsImageCrops',
        'image_hash': 'string',
        'link': 'string',
        'message': 'string',
        'multi_share_end_card': 'bool',
        'multi_share_optimized': 'bool',
        'name': 'string',
        'offer_id': 'string',
        'page_welcome_message': 'string',
        'picture': 'string',
        'retailer_item_ids': 'list<string>',
        'show_multiple_images': 'bool',
    }

    @classmethod
    def _get_field_enum_info(cls):
        field_enum_info = {}
        field_enum_info['AttachmentStyle'] = AdCreativeLinkData.AttachmentStyle.__dict__.values()
        return field_enum_info
