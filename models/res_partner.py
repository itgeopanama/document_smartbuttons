# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from openerp import models, api, fields


class res_partner(models.Model):
    _inherit = 'res.partner'
    _description = 'res partner'

    attachment_count = fields.Integer(compute='_compute_attachment_count', string='# of Attachment')

    @api.multi
    def action_view_attachment(self):
        self.ensure_one()
        imd = self.env['ir.model.data']
        action = imd.xmlid_to_object('base.action_attachment')
        list_view_id = imd.xmlid_to_res_id('base.view_attachment_tree')
        form_view_id = imd.xmlid_to_res_id('base.view_attachment_form')
        result = {
            'name': action.name,
            'help': action.help,
            'type': action.type,
            'views': [[list_view_id, 'tree'], [form_view_id, 'form']],
            'target': action.target,
            'context': {'default_res_model':self._name ,'default_res_id':self._ids[0] },
            'res_model': action.res_model,
        }
        result['domain'] = [('res_id', 'in', self._ids), ('res_model', '=', self._name)]
        return result

    @api.multi
    def _compute_attachment_count(self):
        attachment = self.env['ir.attachment']
        for partner in self:
            partner.attachment_count = attachment.search_count([
                ('res_id', 'in', partner._ids),('res_model', '=', partner._name)
            ])
# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
