from odoo import models,fields,api
class Library(models.Model):
    _name="library"
    date_publication=fields.Date("Date pub")
    isbn=fields.Boolean("ISBN valide")
    titre=fields.Text("Titre")
    image=fields.Image("Image")
    maison_edition=fields.Text("Maisopn D'Edition")
    etiquette=fields.Boolean("Est Accesible")
    member = fields.Many2many('res.partner','member')