# -*- coding: utf-8 -*-

from odoo import api, fields, models


class Survey(models.Model):
    _name = "latlng.survey"
    _description = u"调查评价"
    _rec_name = "title"

    title = fields.Char(string=u"标题", required=True)
    survey_page_line = fields.One2many("latlng.survey.page", "page_id", string=u"调查页数")

