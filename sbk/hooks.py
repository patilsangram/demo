# -*- coding: utf-8 -*-
from __future__ import unicode_literals

app_name = "sbk"
app_title = "sbk"
app_publisher = "sbk"
app_description = "demo app"
app_icon = "octicon octicon-file-directory"
app_color = "grey"
app_email = "sambhaji.k@indictranstech.com"
app_version = "0.0.1"
app_license = "MIT"

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/sbk/css/sbk.css"
# app_include_js = "/assets/sbk/js/sbk.js"

# include js, css files in header of web template
# web_include_css = "/assets/sbk/css/sbk.css"
# web_include_js = "/assets/sbk/js/sbk.js"

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
#	"Role": "home_page"
# }

# Website user home page (by function)
# get_website_user_home_page = "sbk.utils.get_home_page"

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Installation
# ------------

# before_install = "sbk.install.before_install"
# after_install = "sbk.install.after_install"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "sbk.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
# 	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
# 	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
# 	"*": {
# 		"on_update": "method",
# 		"on_cancel": "method",
# 		"on_trash": "method"
#	}
# }

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"sbk.tasks.all"
# 	],
# 	"daily": [
# 		"sbk.tasks.daily"
# 	],
# 	"hourly": [
# 		"sbk.tasks.hourly"
# 	],
# 	"weekly": [
# 		"sbk.tasks.weekly"
# 	]
# 	"monthly": [
# 		"sbk.tasks.monthly"
# 	]
# }

# Testing
# -------

# before_tests = "sbk.install.before_tests"

# Overriding Whitelisted Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "sbk.event.get_events"
# }

