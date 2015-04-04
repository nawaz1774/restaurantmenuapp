"""This module is the Project file for the application Restaurant Menu. 

This Module creates the flask application. This module holds all the functions that need to respond to HTTP requests.

"""
from flask import Flask, render_template, request, redirect, url_for, flash
import Restaurant as ResMod
import MenuItem as MI

# This create out flask application
app = Flask(__name__)

#Creating the route for Page1: res.html. This will be the initial page with which our web application responds.
@app.route('/')
@app.route('/res/')
def listOfRes():
	"""This function responds to GET request to display all the Restaurants

	Args:
		None

	Returns:
		Returns a HTML Template.

	"""
	pgtitle = "List Of Restaurants"
	rest = ResMod.get_list_of_res(10)
	return render_template('res/res.html', pgtitle = pgtitle, rest = rest)

#This is the route for Page2: menu.html. This page will have all the menu items of a restaurant.
@app.route('/res/<int:res_id>/menu/')
def menuItemsoFRes(res_id):
	"""This function responds to GET request to display all the Menu Items of a Restaurants

	Args:
		res_id: Restaurant id for which the Menu Items are being displayed.

	Returns:
		Returns a HTML Template.

	"""
	pgtitle = "List Of Menu Items"
	items = MI.get_menuitems(res_id)

	return render_template('menu/menu_items.html', pgtitle = pgtitle, items = items, res_id = res_id)

#This is the route for Page3: res_add.html. This page will contain the form to add a new Restaurant.
@app.route('/res/add/', methods = ['GET', 'POST'])
def addNewRes():
	"""This responds to GET requests by sending a Form to add a new Restaurant. Accepts POST to add a new restaurant.

	Args:
		None

	Returns:
		Returns a HTML Template.

	"""
	if request.method == "POST":
		name = request.form['resname']
		cuisine = request.form['cusname']
		desc = request.form['desc']
		resobj = ResMod.Restaurant(name, cuisine, desc)
		ResMod.add_res(resobj)
		flash("new restaurant has been added!")
		return redirect(url_for('listOfRes'))
	else:
		pgtitle = "Add Restaurant"
		return render_template('res/add_res.html', pgtitle = pgtitle)


@app.route('/res/<int:res_id>/edit/', methods = ['GET', 'POST'])
def editRes(res_id):
	"""This responds to GET requests by sending a Form to edit a Restaurant. Accepts POST to edit a restaurant.

	Args:
		res_id: Restaurant id for which the Menu Items are being displayed.

	Returns:
		Returns a HTML Template.

	"""

	return "A form for editing a Restaurant"


@app.route('/res/<int:res_id>/delete/', methods = ['GET', 'POST'])
def deleteRes(res_id):
	"""This responds to GET requests by sending a Form to delete a Restaurant. Accepts POST to delete a restaurant.

	Args:
		res_id: Restaurant id for which the Menu Items are being displayed.

	Returns:
		Returns a HTML Template.

	"""
	res_name = ResMod.get_res_name_with_id(res_id)
	if request.method == "POST":
		result = ResMod.delete_res(res_id)
		if result == 1:
			flash(res_name + " has been removed!")
			return redirect(url_for('listOfRes'))
		else:
			flash(res_name + " could not be has been removed!")
			return redirect(url_for('listOfRes'))
	else:
		pgtitle = "Delete a Restaurant"
		return render_template('res/delete_res.html', pgtitle = pgtitle, res_id = res_id, res_name = res_name)

@app.route('/res/<int:res_id>/menu/add/', methods = ['GET', 'POST'])
def addMenuItem(res_id):
	"""This responds to GET requests by sending a Form to add a new Menu Item. Accepts POST to add a new menu item.

	Args:
		res_id: A Integer that identifies a Restaurant uniquely.

	Returns:
		Returns a HTML Template.
	"""
	if request.method == "POST":
		name = request.form['mname']
		course = request.form['crs']
		desc = request.form['desc']
		menu_item = MI.MenuItem(name, course, desc, res_id)
		result = MI.add_menuitem(menu_item)
		flash("new menu item has been added!")
		return redirect(url_for('menuItemsoFRes', res_id = res_id))
	else:
		pgtitle = "Add a new menu item"
		return render_template('menu/add_menu.html', pgtitle = pgtitle, res_id = res_id)

# This code in needed in case we need to run our own web server
if __name__ == '__main__':
	app.secret_key = 'super_secret_key'
	app.debug = True
	app.run(port = 9000)
