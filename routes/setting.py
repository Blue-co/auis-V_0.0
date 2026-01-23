from flask import Blueprint, render_template

setting_bp = Blueprint('setting', __name__)

@setting_bp.route('/setting')
def setting():
    return render_template('st.html')
