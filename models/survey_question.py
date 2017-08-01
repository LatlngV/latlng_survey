# -*- coding: utf-8 -*-

from odoo import api, fields, models


class SurveyQuestion(models.Model):
    _name = "latlng.survey.question"
    _description = u"问题"
    _rec_name = "title"

    SELECT_QUESTION_TYPE = [("text", u"文本"), ("datetime", u"时间和日期"), ("number", u"数值"),
                            ("single_choice", u"单项选择"), ("multiple_choice", u"多项选择")]

    title = fields.Char(string=u"问题", required=True)
    standard = fields.Text(string=u"评分标准")
    question_type = fields.Selection(SELECT_QUESTION_TYPE, string=u"问题类型", defaule="number")
    limit_score = fields.Float(string=u"分数", digits=(4, 1))
    answer_question = fields.Boolean(string=u"必答问题", defaule=True)
    question_id = fields.Many2one("latlng.survey.question", string=u"问题")
