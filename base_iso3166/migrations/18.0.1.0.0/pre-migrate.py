from openupgradelib import openupgrade


@openupgrade.migrate()
def migrate(env, version):
    env.cr.execute(
        """
        UPDATE ir_ui_view SET type = 'list'
            WHERE name = 'Country tree (with ISO 3166-1 alpha-3)'
        """
    )
