from odoo import http
from odoo.http import request
from odoo.addons.website_slides.controllers.main import WebsiteSlides

class WebsiteSlidesAccessControl(WebsiteSlides):

    @http.route(['/slides/slide/<model("slide.channel"):slide>'], type='http', auth="user", website=True)
    def slide(self, slide, **kwargs):
        user = request.env.user
        partner = user.partner_id

        if slide.product_id and slide.product_id.recurring_invoice:
            # Cari subscription aktif ke produk ini
            subscription = request.env['sale.order'].sudo().search([
                ('partner_id', '=', partner.id),
                ('recurring_invoice_line_ids.product_id', '=', slide.product_id.id),
                ('subscription_state', '=', '3_progress')
            ], limit=1)

            if not subscription:
                return request.redirect('/my/account')

        # Jika tidak diset sebagai subscription, akses diperbolehkan
        return super().slide(slide, **kwargs)
