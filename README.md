# Rock Strongo
A RESTful training API.

Rock Strongo provides a simple, general and RESTful API for building training applications. It can support a wide range of training from simple novice 5k, triathlon coaching, boot camp style training and professional level coaching.

It's strength is its simplicity. Given a couple small building blocks, applications may build what every they wish to present to their users.

## Basic Concepts
The following core concepts are key to understanding how to use the API.

### REST
A RESTful API means a resource based design. All requests refer to a resource in some way or another. Whether you are creating a new resource, fetching an existing resource, a list of resources or even computing the number of hours in a training schedule.

### REST Resouce Examples

To create a new workout, send a POST request to the ``/workouts`` url with a JSON body containing te required parameters. This is called a factory resource in that it creates the resources it names.

    POST /api/v1/workouts

```javascript
{
    "workout_template_uid": "Lti9",
    "date": 20120315,
    "time": 0530,
    "duration": "2hrs"
}
```

If the request succeeded a HTTP response code of 204 - Created is returned with a JSON body containing a representation of the new resource:

```javascript
{
    "uid": "32Je",
    "date": 20120315,
    "time": 0530,
    "duration": "2hrs"
    "url": "/api/v1/workouts/32Je"
}
```

One important thing to note here is the ``url`` parameter. This "self-traversing url" is a reference to the new resource. All new resources will contain this parameter. It allows client services to refer back to the resource with little or no knowledge of the system. If this resource contained sub-resources, a factory resource url would also be inclueded to allow creation of a sub-resource.

## Resources
*Template: A <Resource> instance resource represents a <long description>.*

### Athlete (User?)
#### Use Case Satisfied
#### Resource Properties
#### Example CURL Call
#### Example JSON Response

### Program
A Program instance resource represents a training program for an athlete. Extending over a period of time and culminating with a goal it is the resource under which most other resources are based.

#### Use Case Satisfied
As an athlete, I want to train for a marathon, so that I can qualify for the Boston Marathon.

Given I have a User account

    * and I am logged in
    
When I request a new program with the following data:

```    
    name = Boston Training
    start = December 2012
    end = April 2013
    goal = Boston Marathon
```

Then I should receive a successful respnse

    * and it should contain the following data:

```javascript
{
    "uid": <uid>
    "name": "Boston Training"
    "start": "201212"
    "end": 201304
    "goal": "Boston Marathon"
}
```

#### Resource Properties
<table>
    <thead>
        <tr>
            <th align="left">Property</th>
            <th align="left">Description</th>
            </tr>
    </thead>
    <tbody>
        <tr>
            <td align="left">uid</td>
            <td align="left">A 4 character string that uniquely identifies this resource.</td>
        </tr>
    </tbody>
</table>

#### Example CURL Call
``curl -d '' -H 'X-Auth-Token: <access_token>' 'http://api.rs.com/api/v1/programs'``

#### Example JSON Response

```javascript
{
    "uid": "cYUF",
    "name": "Boston Training"
    "start": "201212"
    "end": 201304
    "goal": "Boston Marathon"
}
```

### Activity Template
Defines the basic unit of exercise, e.g., running or strength training.

### Activity
Defines an instance of an activity with a particular date, time and length. For example, Run 5 miles on 3/15/2012 or Swim 1600m at 5:30 am.

### Workout Template
Defines how to perform workouts and why they are done. For example, a tempo run is the template for a specific tempo run done by a particular athlete on a certain date.

### Workout
Defines an association of activities (what) and workout templates (how).
