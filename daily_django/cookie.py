'''Sure! Let's look at how we can use cookies in Django with some simple code examples.

Setting a Cookie
When you visit a website, the server can send a cookie to your browser. In Django, you can set a cookie in a view function. Here’s how you do it:'''

from django.http import HttpResponse

def set_cookie_view(request):
    response = HttpResponse("Here's a cookie for you!")
    # Setting a cookie named 'favorite_color' with the value 'blue'
    response.set_cookie('favorite_color', 'blue')
    return response

'''Getting a Cookie
To read a cookie that was previously set, you use the request object in your view:'''

from django.http import HttpResponse

def get_cookie_view(request):
    # Reading the cookie 'favorite_color'
    favorite_color = request.COOKIES.get('favorite_color')
    if favorite_color:
        return HttpResponse(f'Your favorite color is {favorite_color}.')
    else:
        return HttpResponse("You don't have a favorite color set.")

'''In this example, when you visit the get_cookie_view URL, the server checks if the favorite_color cookie exists. If it does, it displays the value of the cookie. If not, it tells you that the favorite color isn't set.'''


'''Deleting a Cookie
To delete a cookie, you set its value to an empty string and set its expiration date in the past:'''

from django.http import HttpResponse

def delete_cookie_view(request):
    response = HttpResponse("Cookie has been deleted.")
    # Deleting the cookie 'favorite_color'
    response.delete_cookie('favorite_color')
    return response
# In the Django code provided, the session cookie is set when the user logs in. Specifically, this happens when the login(request, user) function is called in the login_view. Let's break down the relevant part of the login_view function:

# login_view Function

'''In this example, when you visit the delete_cookie_view URL, the server deletes the favorite_color cookie.'''

'''In the Django code provided, the session cookie is set when the user logs in. Specifically, this happens when the login(request, user) function is called in the login_view. Let's break down the relevant part of the login_view function:

login_view Function'''

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)  # Session cookie is set here
            return redirect('protected')
        else:
            return HttpResponse("Invalid login details.")
    return render(request, 'login.html')


# Explanation
# Form Submission:

# The user submits their username and password via a POST request.
# User Authentication:

# The authenticate(request, username=username, password=password) function checks the provided credentials.
# If the credentials are valid, it returns the user object. Otherwise, it returns None.
# Setting the Session Cookie:

# If the user is authenticated (user is not None), the login(request, user) function is called.
# This function does the following:
# It creates a new session for the user if one doesn't already exist.
# It sets a session cookie in the user's browser. This cookie contains the session ID, which Django uses to associate the session data stored on the server with the user.
# Redirecting to a Protected View:

# After setting the session cookie, the user is redirected to the protected view.
# Session Management in Django
# Django handles session management using the django.contrib.sessions framework. Here's how it works:

# Session Creation: When login(request, user) is called, Django creates a new session object if it doesn't already exist. This session object stores data on the server side.

# Session ID: The session ID is a unique identifier for the session. It is stored in a cookie on the client's browser. The default name for this cookie is sessionid.

# Session Cookie: The session cookie contains the session ID and is sent to the client's browser. This cookie is used to identify the user's session in subsequent requests.

# Session Data: The actual data for the session is stored on the server (e.g., in the database, cache, or filesystem, depending on your session backend configuration).

# Example Session Cookie
# When the login(request, user) function is called, a session cookie similar to the following is set in the user's browser:

# Set-Cookie: sessionid=xyz123abc456; Path=/; HttpOnly


'''sessionid: The unique session identifier.
Path=/: The path for which the cookie is valid (in this case, the entire site).
HttpOnly: A flag indicating that the cookie should not be accessible via JavaScript, enhancing security.
By using Django's built-in authentication and session management, you don't have to manually handle cookies. Django abstracts these details and provides a secure and convenient way to manage user sessions.'''
