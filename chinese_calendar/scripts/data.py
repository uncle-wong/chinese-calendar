# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

import datetime

import chinese_calendar

constants_template = """# -*- coding: utf-8 -*-
# this file is generated by chinese_calendar.scripts.generate_constants
from __future__ import absolute_import, unicode_literals

import datetime
from enum import Enum


class Holiday(Enum):
    def __new__(cls, english, chinese, days):
        obj = object.__new__(cls)
        obj._value_ = english

        obj.chinese = chinese
        obj.days = days
        return obj

    new_years_day = 'New Year\\'s Day', '元旦', 1
    spring_festival = 'Spring Festival', '春节', 3
    tomb_sweeping_day = 'Tomb-sweeping Day', '清明', 1
    labour_day = 'Labour Day', '劳动节', 1
    dragon_boat_festival = 'Dragon Boat Festival', '端午', 1
    national_day = 'National Day', '国庆节', 3
    mid_autumn_festival = 'Mid-autumn Festival', '中秋', 1


holidays = {}

workdays = {}
"""


class Arrangement(object):
    def __init__(self):
        self.holidays = {}
        self.workdays = {}

        self.year = None
        self.month = None
        self.day = None
        self.holiday = None
        self.is_working = None

        for method in dir(self):
            try:
                int(method[1:])
                getattr(self, method)()
            except ValueError:
                pass

    def _2018(self):
        """ http://www.gov.cn/zhengce/content/2017-11/30/content_5243579.htm
一、元旦：1月1日放假，与周末连休。
二、春节：2月15日至21日放假调休，共7天。2月11日（星期日）、2月24日（星期六）上班。
三、清明节：4月5日至7日放假调休，共3天。4月8日（星期日）上班。
四、劳动节：4月29日至5月1日放假调休，共3天。4月28日（星期六）上班。
五、端午节：6月18日放假，与周末连休。
六、中秋节：9月24日放假，与周末连休。
七、国庆节：10月1日至7日放假调休，共7天。9月29日（星期六）、9月30日（星期日）上班。
        """
        self.year_at(2018) \
            .nyd().rest(1, 1) \
            .sf().rest(2, 15).to(2, 21).work(2, 11).work(2, 24) \
            .tsd().rest(4, 5).to(4, 7).work(4, 8) \
            .ld().rest(4, 29).to(5, 1).work(4, 28) \
            .dbf().rest(6, 18) \
            .nd().rest(10, 1).to(10, 7).work(9, 29).work(9, 30) \
            .maf().rest(9, 24)

    def _2017(self):
        """ http://www.gov.cn/zhengce/content/2016-12/01/content_5141603.htm
一、元旦：1月1日放假，1月2日（星期一）补休。
二、春节：1月27日至2月2日放假调休，共7天。1月22日（星期日）、2月4日（星期六）上班。
三、清明节：4月2日至4日放假调休，共3天。4月1日（星期六）上班。
四、劳动节：5月1日放假，与周末连休。
五、端午节：5月28日至30日放假调休，共3天。5月27日（星期六）上班。
六、中秋节、国庆节：10月1日至8日放假调休，共8天。9月30日（星期六）上班。
        """
        self.year_at(2017) \
            .nyd().rest(1, 1).to(1, 2) \
            .sf().rest(1, 27).to(2, 2).work(1, 22).work(2, 4) \
            .tsd().rest(4, 2).to(4, 4).work(4, 1) \
            .ld().rest(5, 1) \
            .dbf().rest(5, 28).to(5, 30).work(5, 27) \
            .nd().rest(10, 1).to(10, 8) \
            .maf().rest(10, 4).work(9, 30)  # 国庆中秋相连，经查证10月4日为中秋

    def _2016(self):
        """ http://www.gov.cn/zhengce/content/2015-12/10/content_10394.htm
一、元旦：1月1日放假，与周末连休。
二、春节：2月7日至13日放假调休，共7天。2月6日（星期六）、2月14日（星期日）上班。
三、清明节：4月4日放假，与周末连休。
四、劳动节：5月1日放假，5月2日（星期一）补休。
五、端午节：6月9日至11日放假调休，共3天。6月12日（星期日）上班。
六、中秋节：9月15日至17日放假调休，共3天。9月18日（星期日）上班。
七、国庆节：10月1日至7日放假调休，共7天。10月8日（星期六）、10月9日（星期日）上班。
        """
        self.year_at(2016) \
            .nyd().rest(1, 1) \
            .sf().rest(2, 7).to(2, 13).work(2, 6).work(2, 14) \
            .tsd().rest(4, 4) \
            .ld().rest(5, 1).to(5, 2) \
            .dbf().rest(6, 9).to(6, 11).work(6, 12) \
            .maf().rest(9, 15).to(9, 17).work(9, 18) \
            .nd().rest(10, 1).to(10, 7).work(10, 8).to(10, 9)

    def _2015(self):
        """ http://www.gov.cn/zhengce/content/2014-12/16/content_9302.htm
一、元旦：1月1日至3日放假调休，共3天。1月4日（星期日）上班。
二、春节：2月18日至24日放假调休，共7天。2月15日（星期日）、2月28日（星期六）上班。
三、清明节：4月5日放假，4月6日（星期一）补休。
四、劳动节：5月1日放假，与周末连休。
五、端午节：6月20日放假，6月22日（星期一）补休。
六、中秋节：9月27日放假。
七、国庆节：10月1日至7日放假调休，共7天。10月10日（星期六）上班。
        """
        self.year_at(2015) \
            .nyd().rest(1, 1).to(1, 3).work(1, 4) \
            .sf().rest(2, 18).to(2, 24).work(2, 15).work(2, 28) \
            .tsd().rest(4, 5).to(4, 6) \
            .ld().rest(5, 1) \
            .dbf().rest(6, 20).rest(6, 22) \
            .maf().rest(9, 27) \
            .nd().rest(10, 1).to(10, 7).work(10, 10)

    def _2014(self):
        """ http://www.gov.cn/zwgk/2013-12/11/content_2546204.htm
一、元旦：1月1日放假1天。
二、春节：1月31日至2月6日放假调休，共7天。1月26日（星期日）、2月8日（星期六）上班。
三、清明节：4月5日放假，4月7日（星期一）补休。
四、劳动节：5月1日至3日放假调休，共3天。5月4日（星期日）上班。
五、端午节：6月2日放假，与周末连休。
六、中秋节：9月8日放假，与周末连休。
七、国庆节：10月1日至7日放假调休，共7天。9月28日（星期日）、10月11日（星期六）上班。
        """
        self.year_at(2014) \
            .nyd().rest(1, 1) \
            .sf().rest(1, 31).to(2, 6).work(1, 26).work(2, 8) \
            .tsd().rest(4, 5).work(4, 7) \
            .ld().rest(5, 1).to(5, 3).work(5, 4) \
            .dbf().rest(6, 2) \
            .maf().rest(9, 8) \
            .nd().rest(10, 1).to(10, 7).work(9, 28).work(10, 11)

    def _2013(self):
        """ http://www.gov.cn/zwgk/2012-12/10/content_2286598.htm
一、元旦：1月1日至3日放假调休，共3天。1月5日（星期六）、1月6日（星期日）上班。
二、春节：2月9日至15日放假调休，共7天。2月16日（星期六）、2月17日（星期日）上班。
三、清明节：4月4日至6日放假调休，共3天。4月7日（星期日）上班。
四、劳动节：4月29日至5月1日放假调休，共3天。4月27日（星期六）、4月28日（星期日）上班。
五、端午节：6月10日至12日放假调休，共3天。6月8日（星期六）、6月9日（星期日）上班。
六、中秋节：9月19日至21日放假调休，共3天。9月22日（星期日）上班。
七、国庆节：10月1日至7日放假调休，共7天。9月29日（星期日）、10月12日（星期六）上班。
        """
        self.year_at(2013) \
            .nyd().rest(1, 1).to(1, 3).work(1, 5).to(1, 6) \
            .sf().rest(2, 9).to(2, 15).work(2, 16).work(2, 17) \
            .tsd().rest(4, 4).to(4, 6).work(4, 7) \
            .ld().rest(4, 29).to(5, 1).work(4, 27).work(4, 28) \
            .dbf().rest(6, 10).rest(6, 12).work(6, 8).work(6, 9) \
            .maf().rest(9, 19).to(9, 21).work(9, 22) \
            .nd().rest(10, 1).to(10, 7).work(9, 29).work(10, 12)

    def _2012(self):
        """ http://www.gov.cn/zwgk/2011-12/06/content_2012097.htm
一、元旦：2012年1月1日至3日放假调休，共3天。2011年12月31日（星期六）上班。
二、春节：1月22日至28日放假调休，共7天。1月21日（星期六）、1月29日（星期日）上班。
三、清明节：4月2日至4日放假调休，共3天。3月31日（星期六）、4月1日（星期日）上班。
四、劳动节：4月29日至5月1日放假调休，共3天。4月28日（星期六）上班。
五、端午节：6月22日至24日放假公休，共3天。
六、中秋节、国庆节：9月30日至10月7日放假调休，共8天。9月29日（星期六）上班。

        注意：今年元旦特殊处理，去年上班 Σ( ° △ °|||)︴
        """
        self.year_at(2012) \
            .nyd().rest(1, 1).to(1, 3) \
            .sf().rest(1, 22).to(1, 28).work(1, 21).work(1, 29) \
            .tsd().rest(4, 2).to(4, 4).work(3, 31).work(4, 1) \
            .ld().rest(4, 29).to(5, 1).work(4, 28) \
            .dbf().rest(6, 22).rest(6, 24) \
            .maf().rest(9, 30) \
            .nd().rest(10, 1).to(10, 7).work(9, 29)

    def year_at(self, number):
        self.year = number
        return self

    def nyd(self):
        return self.mark(chinese_calendar.Holiday.new_years_day)

    def sf(self):
        return self.mark(chinese_calendar.Holiday.spring_festival)

    def tsd(self):
        return self.mark(chinese_calendar.Holiday.tomb_sweeping_day)

    def ld(self):
        return self.mark(chinese_calendar.Holiday.labour_day)

    def dbf(self):
        return self.mark(chinese_calendar.Holiday.dragon_boat_festival)

    def nd(self):
        return self.mark(chinese_calendar.Holiday.national_day)

    def maf(self):
        return self.mark(chinese_calendar.Holiday.mid_autumn_festival)

    def mark(self, holiday):
        self.holiday = holiday
        return self

    def work(self, month, day):
        return self.save(month, day, is_working=True)

    def rest(self, month, day):
        return self.save(month, day, is_working=False)

    def save(self, month, day, is_working=True):
        if not self.year:
            raise ValueError('should set year before saving holiday')
        if not self.holiday:
            raise ValueError('should set holiday before saving holiday')
        self.is_working = is_working
        self.days[datetime.date(year=self.year, month=month, day=day)] = self.holiday
        self.month = month
        self.day = day
        return self

    def to(self, month, day):
        if not (self.year and self.month and self.day):
            raise ValueError('should set year/month/day before saving holiday range')
        start_date = datetime.date(year=self.year, month=self.month, day=self.day)
        end_date = datetime.date(year=self.year, month=month, day=day)
        if end_date <= start_date:
            raise ValueError('end date should be after start date')
        for i in range((end_date - start_date).days):
            the_date = start_date + datetime.timedelta(days=i + 1)
            self.days[the_date] = self.holiday
        return self

    @property
    def days(self):
        return self.workdays if self.is_working else self.holidays
