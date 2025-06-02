from odoo import http
from odoo.http import request
from odoo.addons.website_slides.controllers.main import WebsiteSlides

class WebsiteSlidesAccessControl(WebsiteSlides):

    @http.route(['/slides/course/<model("slide.channel"):channel>'], type='http', auth="user", website=True)
    def channel(self, channel, **kwargs):
        user = request.env.user
        partner = user.partner_id

        if channel.product_id and channel.product_id.recurring_invoice:
            # Cari subscription aktif ke produk ini
            subscription = request.env['sale.order'].sudo().search([
                ('partner_id', '=', partner.id),
                ('recurring_invoice_line_ids.product_id', '=', channel.product_id.id),
                ('subscription_state', '=', '3_progress')
            ], limit=1)

            if not subscription:
                return request.redirect('/my/account')

        # Jika tidak diset sebagai subscription, akses diperbolehkan
        return super().channel(channel, **kwargs)
