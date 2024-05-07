#include<iostream>
using namespace std;
double A, B;
int main() {
	cin >> A;
	cin >> B;
	cout.precision(10);
	cout << A / B;
	return 0;
}
//double vs float
//둘다 실수 자료형 사용시 사용
//단,정밀도 차이가 있음
//float : 소수점 이하 6자리, double : 소수점 이하 15자리