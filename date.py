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