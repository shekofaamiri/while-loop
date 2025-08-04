#include<iostream>
using namespace std;
class Date{
    private:
    int day,month,year;
    public:
    void set_day(int);
    void set_month(int);
    void set_year(int);
    int get_day();
    int get_month();
    int get_year();
    void print_date();
};
void Date::set_day(int d){
    day=d;
}
int Date::get_day(){
    return day;
}
void Date::set_month(int m){
    month=m;
}
int Date::get_month(){
    return month;
}
void Date::set_year(int y){
    year=y;
}
int Date::get_year(){
    return year;
}
void Date::print_date(){
    cout<<year<<"/"<<month<<"/"<<day;
}