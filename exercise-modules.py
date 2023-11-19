#!/usr/bin/env python3
"""
Functions in module 'mini.py' called by a Lambda function.will be
used to exercise some functions in module 'pyfuncs.py'.
"""

from mini import (
    test_dt_weekend,
    test_eb_time_local_zone_false,
    test_eb_time_local_zone_true,
    test_eb_time_utc_zone_false,
    test_eb_time_utc_zone_true,
)

from pyfuncs import (
    add,
    divide,
    eb_time_local,
    eb_time_utc,
    exercise_datetime,
    exercise_inspect,
    exercise_randint,
    exercise_time,
    feet_2_meters,
    get_joke_dict,
    get_joke_else,
    get_random_int,
    is_dt_today_a_weekday,
    kilograms_2_pounds,
    len_joke_dict,
    len_joke_else,
    meters_2_feet,
    multiply,
    pounds_2_kilograms,
    printing_the_name_of_this_function,
    request_input,
    return_args_and_kwargs,
    return_args_only,
    return_kwargs_only,
    subtract,
)


def lambda_handler(event, context):
    test_eb_time_local_zone_false()
    test_eb_time_local_zone_true()
    test_eb_time_utc_zone_false()
    test_eb_time_utc_zone_true()
    test_dt_weekend()
    return


def main():
    # eb_time_local(False)
    # eb_time_utc(False)
    # eb_time_local()
    # eb_time_utc()
    # is_tm_today_a_weekday()
    # is_dt_today_a_weekday()
    # exercise_inspect()
    # exercise_datetime()
    # exercise_time()
    # print(get_joke_dict())
    # print(get_joke_else())
    # print(request_input())
    # access_dict()
    # len_joke_dict()
    # len_joke_else()
    # get_random_int(begin=1, bookend=11, modifier=1)
    # get_random_int()
    test_eb_time_local_zone_false()
    test_eb_time_local_zone_true()
    test_eb_time_utc_zone_false()
    test_eb_time_utc_zone_true()
    test_dt_weekend()
    return


if __name__ == '__main__':
    main()
# EOF
