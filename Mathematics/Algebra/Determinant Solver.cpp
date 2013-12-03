#include <iostream>
using namespace std;
void getInput(){
	cout << "Enter the value of ";
}
int main(){
getInput();
cout << "X1" << endl;
int x1;
cin >> x1;
getInput();
cout << "Y1" << endl;
int y1;
cin >> y1;
getInput();
cout << "X2" << endl;
int x2;
cin >> x2;
getInput();
cout << "Y2" << endl;
int y2;
cin >> y2;
int answer;
answer = (x1 * y2) - (x2 * y1);
cout << "The value of the determinant is: " << answer;
	cin.get();
	cin.get();
	return 0;
}
