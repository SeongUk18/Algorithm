#include<iostream>
using namespace std;
int M,H,C;
int main() {
	cin >> H >> M;
	C = 60*H + M-45;
	if (C < 0) {
		C = 24 * 60 + C;
		cout << C / 60 << " " << C % 60;
	}else
		cout << C / 60 << " " << C % 60;

	return 0;
}