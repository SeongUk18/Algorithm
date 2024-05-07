#include<iostream>
using namespace std;
int A,B;
int main() {
	cin.tie(NULL);
	std::ios_base::sync_with_stdio(false);
	while (true) {
		cin >> A >> B;
		if (A == 0 && B == 0)
			break;
		else
			cout << A + B << "\n";
	}
	
	return 0;
}