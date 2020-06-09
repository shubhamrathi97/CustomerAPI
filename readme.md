# CUSTOMER REST API

These API developed using Flask, Sqlalchemy and Postgres. We are using Gunicorn, Docker-compose for Deployment.
If using postman, Please import  `CustomerAPI` collection.

## Run Manual
#### Docker-Compose
* Run the `docker-compose up --build -d`. API Service will be available at port `5000`.

#### Without Docker
* Please set environment variable `SQLALCHEMY_DATABASE_URI` for configuring database URI else you can modified the config.py file. 
* Install the dependency listed in `requirements.txt` in virtual environment and
* run  `FLASK_APP=app.py; flask run` 

## Open Endpoints

Open endpoints require no Authentication.


* [Register](#) : `POST /register`

    API for creating the user

        Auth required : NO
        
        Request Data:
        
        {
            "username": "[valid username]",
            "password": "[password in plain text]"
        }
        
        Response Data
        
        {
            "data": {
                "username": "shubham2"
            },
            "result": "success"
        }
        


* [Login](#) : `POST /login`
    
    Used to collect a Token for a registered User.

        Auth required : NO
        
        Request Data:
        
        {
            "username": "[valid username]",
            "password": "[password in plain text]"
        }
        
        Response Data
        
        {
          "data": {
            "access_token": <token>,
            "refresh_token": <refresh_token>
          },
          "result": "success"
        }
        

## Endpoints that require Authentication

Closed endpoints require a valid Bearer Token to be included in the header of the
request. A Token can be acquired from the Login API above.
Please set Authorization header with  `Bearer <token>` before making API request on below endpoints.    

### Current Customer API

Each endpoint manipulates or displays information related to the Customer :

* [Get All Customer](#) : `GET /customers/`
* [Get Youngest 'n' Customer](#) : `GET /customers/?n=<n:int>`
* [Create Customer](#) : `POST /customers/`
* [Get A Customer](#) : `GET /customers/:pk/`
* [Update A Customer](#) : `PUT /customers/:pk/`
* [Delete A Customer](#) : `DELETE /customers/:pk/`


### Account related

* [Logout](#) : `GET /logout`
    
    Endpoints for logout and blacklist the created token of Authenticated User to prevent the replay attack on JWT
* [Refresh Token](#) : `GET /refresh`

    Endpoint for generating the access token from refresh token. Access token is valid for 30mins only while refresh token is valid for 30 days.