#include<iostream>
#include<vector>
using namespace std;
int N,number, maxNumber, minNumber;
vector<int> numbers;
int main() {
	cin >> N;
	for (int i = 0; i < N; i++) {
		cin >> number;
		numbers.push_back(number);
	}
	maxNumber = numbers[0];
	minNumber = numbers[0];
	for (int i = 0; i < numbers.size(); i++) {
		if (maxNumber < numbers[i]) maxNumber = numbers[i];
		if (minNumber > numbers[i]) minNumber = numbers[i];
	}
	cout << minNumber << " " << maxNumber;


	return 0;
}