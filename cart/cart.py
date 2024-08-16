class Cart():
  def __init__(self, request):
    self.session = request.session
    
    cart = self.session.get('session_key')

    if 'session' not in request.session:
      cart = self.session['session_key'] = {}

    self.cart = cart