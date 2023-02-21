# API Endpoints for Django RestApi Application

This project provides a REST API for an django rest api application that allows users to view and filter different types of works and register to the application using an API. The following endpoints are available:

## View Works

`GET /api/works`

This endpoint returns a list of all works in the application.

Result:

    {
        "status": "ok",
        "data": [
            {
            "link": "https://www.youtube.com/watch?v=01",
            "work_type": "youtube"
            },
            ...
        ]
    }

This is a JSON object that contains a "status" field and a "data" field which include "link" & "work_type".

### Filtering with Work Type

`GET /api/works?work_type=<type>`

This endpoint returns a list of works that match the specified type. The `work_type` parameter can be set to any valid work type such as "youtube", "instagram" in the database.

    type: youtube, instagram, other

### Search with Artist Name

`GET /api/works?artist=<artist name>`

This endpoint returns a list of works that match the specified artist name.

## Register User

`POST /api/register`

This endpoint allows a user to register with the application by submitting a username and password in the request body. The following example shows how to use this endpoint:

Once user is created, it automatically created a new client object using signals.

Content-Type: application/json

    {
        "username": "testuser",
        "password": "123123"
    }

