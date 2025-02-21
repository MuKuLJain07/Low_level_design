/*
Write code for low level design of a movie ticket booking system like BookMyShow.
System has cinemas located in different cities. Each cinema will have multiple screens, and users can book one or more seats for a given movie show.

System should be able to add new cinemas and movie shows in those cinemas.
Users should be able to list all cinema's in their city which are displaying a particular movie.
For a given cinema, users should also be able to list all shows which are displaying a particular movie.

Booking Criteria:
- Try to book continuous seats from same row.
- In case multiple options are available then choose
  seats starting from lowest row and column.
- If continous seats are not available then pick seats from lowest row, column


Implement the below methods in Solution class:

init(Helper10 helper)
- init() is our constructor/initializer
- helper has methods like, helper.print("") and helper.println("")
    which you can use for printing logs,
    System.out.println logs will not be visible.
 
addCinema(int cinemaId, int cityId,                                        --> Done
int screenCount, int screenRow, int screenColumn)
Add a new cinema inside a city.
- cinemaId is unique across cities
- 0<=cinemaId<=1000
- 0<=cityId<=100
- each cinema can have multiple screens
    1<=screenCount<=10
- each cinema screen will have seats arranged in rows and columns
- 1<=screenRow, screenColumn<=100

addShow(int showId, int movieId, int cinemaId,
int screenIndex, long startTime, long endTime)
Add a show for displaying a movie on a
  cinema screen in a given time slot.
- 0<=showId<=2000
- 0<=movieId<=20
- 1<=screenIndex<=10

List[String] bookTicket(String ticketId,
int showId, int ticketsCount)
Returns list of seats as "row-column"
e.g. ["0-4", "2-14", "2-0", "11-6"]
1<=ticketsCount<=10
See Booking Criteria above on how to book seats.
- If there are less than ticketsCount seats in the given show,
  then don't book any seats and return empty list.

boolean cancelTicket(String ticketId)
cancels ticket and makes all seats booked in ticketId
again available for booking.
- return true if booking with ticketId is cancelled
  and seats are released for booking again
- return false if booking with ticketId doesn't exist
  or it is already cancelled.

int getFreeSeatsCount(int showId)
- return number of free seats available for booking in show showId
- if no show exists with showId or no free seats are available
then return 0

List[Integer] listCinemas(int movieId, int cityId)
- returns cinemaId's of all cinemas which are
    running shows for given movie in the given city
- cinemaId's are ordered in ascending order

List[Integer] listShows(int movieId, int cinemaId)
- returns showId's of all shows displaying
    the given movie in given cinema.
- showId's are ordered in descending order of startTime
    and then showId in ascending order

Input Example
Solution obj=new Solution();
obj.init(helper)
obj.addCinema(cinemaId=0,
cityId=1, screenCount=4,
screenRow=5, screenColumn = 10)
obj.addShow(showId= 1, movieId=4,
cinemaId=0, screenIndex=1,
startTime=1710516108725, endTime=1710523308725)
obj.addShow(showId = 2, movieId=11,
cinemaId = 0, screenIndex = 3,
startTime = 1710516108725, endTime = 1710523308725)

obj.listCinemas(movieId = 0, cityId = 1)
returned cinemaId's list: []
obj.listShows(movieId = 4, cinemaId = 0)
returned showId's list [1]
obj.listShows(movieId = 11, cinemaId = 0)
returned showId's list [2]

obj.getFreeSeatsCount(showId = 1) returned 50
obj.bookTicket(ticketId = 'tkt-1', showId = 1, ticketsCount = 4)
returned seat's list: [0-0, 0-1, 0-2, 0-3]
obj.getFreeSeatsCount(showId = 1) returned 46

obj.cancelTicket(ticketId = 'tkt-1') returned true
obj.getFreeSeatsCount(showId = 1) returned 50
*/

#include <iostream>
#include <map>
#include <string>
#include <vector>
using namespace std;

class Cinema{
    private:
    int cinemaId;
    int screenCount;
    int screenRow;
    int screenColumn;
    vector<vector<bool> > theater;       // false -> empty, true -> occupied
    map<int, vector<vector<string> > > movies;    // screenIndex - showId, movieId,startTime,endTime

    public:
    Cinema(int cinemaId, int screenCount, int screenRow, int screenColumn){
        this->cinemaId = cinemaId;
        this->screenCount = screenCount;
        this->screenRow = screenRow;
        this->screenColumn = screenColumn;

        theater = vector<vector<bool> >(screenRow, vector<bool>(screenColumn, false)); 
    }

    int get_cinemaId(){
        return this->cinemaId;
    }

    void addShow(int showId, int movieId, int cinemaId, int screenIndex, long startTime, long endTime){
        if(0>showId || showId>2000 || 0>movieId || movieId>20){
            cout<<"Invalid show details provided";
            return;
        }

        bool screenIndexFound = false;
        for(auto movie : this->movies){
            if(movie.first == screenIndex){
                screenIndexFound = true;
                movie.second.push_back({to_string(showId), to_string(movieId), to_string(startTime), to_string(endTime)}); 
            }
        }
        if(!screenIndexFound){
            this->movies[screenIndex] = {{to_string(showId), to_string(movieId), to_string(startTime), to_string(endTime)}};
        }
    }
};


class Solution{
    private:
    map<int, vector<Cinema*> > cinemaCity;     // cityId, [class Cinema] 

    public:
    Solution(){

    }
    void addCinema(int cinemaId, int cityId, int screenCount, int screenRow, int screenColumn){
        if(0>cinemaId || cinemaId>1000 || 0 > cityId || cityId>100 || 1>screenCount || screenCount>10 || 1>screenRow || screenColumn>100){
            cout<<"Invalid cinema details provided!!";
            return;
        }

        // check validity for cinema id
        bool cityFound = false;
        for(auto storedCityId : this->cinemaCity){
            if(storedCityId.first == cityId){
                cityFound = true;
                for(auto storedCinemaId : storedCityId.second){
                    if(storedCinemaId->get_cinemaId() == cinemaId){
                        cout<<"Oops !! This cinema id already exists";
                        return;
                    }
                }
                Cinema* newCinema = new Cinema(cinemaId, screenCount, screenRow, screenColumn);
                cinemaCity[storedCityId.first].push_back(newCinema);
            }
        }
        if(!cityFound){
            Cinema* newCinema = new Cinema(cinemaId, screenCount, screenRow, screenColumn);
            vector<Cinema*> temp;
            temp.push_back(newCinema);
            cinemaCity[cityId] = temp;
        }
    }
};

int main(){
    cout<<"Hello World !!";
    return 0;
}