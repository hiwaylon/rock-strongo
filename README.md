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
    {
        "workout_template_uid": "Lti9",
        "date": 20120315,
        "time": 0530,
        "duration": "2hrs"
    }

If the request succeeded a HTTP response code of 204 - Created is returned with a JSON body containing a representation of the new resource:

    {
        "uid": "32Je",
        "date": 20120315,
        "time": 0530,
        "duration": "2hrs"
        "url": "/api/v1/workouts/32Je"
    }

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
    and I am logged in
When I request a new program with the following data:
    name = Boston Training
    start = December 2012
    end = April 2013
    goal = Boston Marathon
Then I should receive a successful respnse
    and it should contain the following data:
        {
            "uid": <uid>
            "name": "Boston Training"
            "start": "201212"
            "end": 201304
            "goal": "Boston Marathon"
        }

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
curl -d '' -H 'X-Auth-Token: <access_token>' 'http://api.rs.com/api/v1/programs'

#### Example JSON Response
{
    "uid": "cYUF",
    "name": "Boston Training"
    "start": "201212"
    "end": 201304
    "goal": "Boston Marathon"
}

### Workout Template
Defines how to perform workouts and why they are done. For example, a tempo run is the template for a specific tempo run done by a particular athlete on a certain date.

### Workout
A Workout instance resource represents a workout to be performed on a particular date. It contains specific details concerning performing the workout. Its associated template defines the category of workkout it is as well as general details of how and why a workout of its type is performed.

#### Use Case Satisfied
As a runner, I want to perform speed workouts so that I can increase my speed on race day.

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
    <tbody>
        <tr>
            <td align="left">description</td>
            <td align="left">A unicode string describing the workout in detail.</td>
        </tr>
    </tbody>
    <tbody>
        <tr>
            <td align="left">date</td>
            <td align="left">A date in the format YYYY-MM-DD on which the workout should be performed.</td>
        </tr>
    </tbody>
    <tbody>
        <tr>
            <td align="left">workout_template_uid</td>
            <td align="left">A 4 character string that uniquely identifies the workout template on which this workout is based.</td>
        </tr>
    </tbody>
</table>

#### Example CURL Call
curl -d '' -H 'X-Auth-Token: <access_token>' 'http://api.rs.com/api/v1/programs/cYUF/workouts'

#### Example JSON Response
{
    "uid": "CFTv",
    "description": "Aerobic run. Nice and easy, stay aerobic!",
    "date": "2012-04-04",
    "workout_template_uid": "44d6"
}

### Activity Template
An ActivityTemplate instance resource represents a basic unit of exercise and how it is done, e.g., a tempo run or maintainence strength training. It is the resource by which the coach defines how their workouts are to be done.

##### Use Cases Satisified
As a coach, I want to define a fartlek workout, so that my athletes can perform them in workouts.

##### Resource Properties
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
        <tr>
            <td align="left">name</td>
            <td align="left">A unicode string that names the activity.</td>
        </tr>
        <tr>
            <td align="left">description</td>
            <td align="left">A unicode string description of the activity.</td>
        </tr>
    </tbody>
</table>

#### Example CURL Call
curl -d '' -H 'X-Auth-Token: <access_token>' 'http://api.rs.com/api/v1/activity_templates'

#### Example JSON Response
{
    "uid": "FAMW",
    "name": "Tempo Run",
    "description": "Run performed in a progressing manner such that the beginning is easy and the middle approaches goal race pace. The tempo portion is held for some time before tapering back down and finishing easy."
}

### Activity
Defines an instance of an activity with a particular date, time and length. For example, Run 5 miles on 3/15/2012 or Swim 1600m at 5:30 am.

# TODO: Workout vs. Activity
Workout are defined variably - distance/time and date/day of week. Run 5 miles Monday(s). Swim 1 hr on 4/2/2012. Same resource.
