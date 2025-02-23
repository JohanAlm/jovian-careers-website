from flask import Flask

app = Flask(
    __name__
)  # create app object and import all functionalities from flask and store it into app variable. All flasks start with this line.

#The name variable tell us of how a particular python script was invoked. mostly it is __main__

# create a route and map it to the endpoint.
# We need to tell flask when a certain url is requested what should be returned.


# route is a part of url after the domain name. (main page)
# endpoint is the url itself.
#we need to register a route.
@app.route('/')  #decorators are used to modify the behavior of a function.
# / ->homepage or the empty route
# define a function below the decorator
def hello_word():
  return "Hello Jovian"
  # The decorator informs flask makes sure that when the / is acessed the function is executed. and Hello World is printed.


if __name__ == '__main__':
  app.run(host='0.0.0.0', debug=True)  #to run locally.
