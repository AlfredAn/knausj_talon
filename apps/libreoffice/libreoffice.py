from talon import Context, Module

ctx = Context()
mod = Module()
mod.apps.libreoffice = """
os: win
and app.name: LibreOffice
"""
