"""Auto-generated file, do not edit by hand. KE metadata"""
from ..phonemetadata import NumberFormat, PhoneNumberDesc, PhoneMetadata

PHONE_METADATA_KE = PhoneMetadata(id='KE', country_code=None, international_prefix=None,
    general_desc=PhoneNumberDesc(national_number_pattern='[1-9]\\d{2,4}', possible_length=(3, 4, 5)),
    toll_free=PhoneNumberDesc(national_number_pattern='1(?:1(?:6|9\\d)|5(?:01|2[127]|6(?:29|6[67])))', example_number='1501', possible_length=(3, 4, 5)),
    premium_rate=PhoneNumberDesc(national_number_pattern='909\\d{2}', example_number='90912', possible_length=(5,)),
    emergency=PhoneNumberDesc(national_number_pattern='112|114|999', example_number='999', possible_length=(3,)),
    short_code=PhoneNumberDesc(national_number_pattern='1(?:0(?:[07-9]|1[0-25]|400)|1(?:[02456]|9[0-579])|2[123]|3[01]|4[14]|5(?:[01][01]|2[0-24-79]|33|4[05]|5[59]|6(?:00|29|6[67]))|6[035]\\d{2}|[78]\\d|9(?:[02-9]\\d{2}|19))|(?:2[0-79]|3[0-29]|4[0-4])\\d{3}|5(?:[0-7]\\d|99)\\d{2}|(?:6[2357]|7[0-29])\\d{3}|8(?:[0-9]\\d{3}|988)|9(?:09\\d{2}|99)', example_number='116', possible_length=(3, 4, 5)),
    carrier_specific=PhoneNumberDesc(national_number_pattern='1(?:0400|3[01]|4[14]|5(?:1[01]|2[25])|6[35]\\d{2})|(?:2[0-79]|3[0-29]|4[0-4])\\d{3}|5(?:[0-7]\\d|99)\\d{2}|(?:6[2357]|7[0-29])\\d{3}|8(?:988|[0-9]\\d{3})|909\\d{2}', example_number='90912', possible_length=(3, 4, 5)),
    sms_services=PhoneNumberDesc(national_number_pattern='1(?:0400|4[14]|5(?:01|55|6(?:29|6[67]))|6[035]\\d{2})|40404|8988|909\\d{2}', example_number='8988', possible_length=(3, 4, 5)),
    short_data=True)
