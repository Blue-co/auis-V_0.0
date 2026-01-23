from flask import Blueprint, render_template

shopping_bp = Blueprint('setting', __name__)

@shopping_bp.route('/setting')
def shopping_list():
    return render_template('st.html')
