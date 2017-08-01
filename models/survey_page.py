# -*- coding: utf-8 -*-

from odoo import api, fields, models


class SurveyPage(models.Model):
    _name = "latlng.survey.page"
    _description = u"页数"
    _rec_name = "title"

    page_id = fields.Many2one("latlng.survey", string=u"调查页数")
    title = fields.Char(string=u"网页标题", required=True)
    survey_question_line = fields.One2many("latlng.survey.question", "question_id", string=u"问题", required=True)
