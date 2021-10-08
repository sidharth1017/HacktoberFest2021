
#include <vector>
#include <queue>
#include <iostream>
#include <string>
using namespace std;

int maxElemLength(const vector<int>& v);
int GetDigit(int number, int k);
vector<queue<int> > ItemsToQueues(const vector<int>& L, int k);
vector<queue<int> > QueuesToArray(const vector<int>& QA, int numDigits);
void RadixSort(vector<int>& L, int numDigits);
void PrintVector(const vector<int>& L);

int main(){
    vector<int> vect{380, 95, 345, 382, 260, 100, 492};
    //vector<int> vect{300,4,54354,4564563, 5};
    PrintVector(vect);
    RadixSort(vect, maxElemLength(vect));
    PrintVector(vect);

}

int maxElemLength(const vector<int>& v){
    int maxElem = 0;

    for (int i=0; i<v.size(); i++){
	int pos = 0;
	int temp = v.at(i);

	while(temp > 0){
	    pos++;
	    temp = temp / 10;
	}

	if (maxElem < pos){
	    maxElem = pos;
	}
    }
    return maxElem;
}

int GetDigit(int number, int k){
    string temp = to_string(number);
    int digit = temp.length() - k-1;
    if (digit > temp.length()){
	return 0;
    }
    else {
	return temp[digit]-'0';
    }

}


vector<queue<int> > ItemsToQueues(const vector<int>& L, int k){
    vector<queue<int> > temp(10);
    for (int i=0; i<L.size(); i++){
	int pos = GetDigit(L.at(i),k);
	temp.at(pos).push(L.at(i));
    }
    return temp;
}


vector<int> QueuesToArray(const vector<queue<int> >& QA, int numDigits){
    vector<int> output;
    for( int i=0; i<QA.size(); i++){
	queue<int> cue = QA.at(i);
	while(!cue.empty()){
	    output.push_back(cue.front());
	    cue.pop();
	}
    }
    return output;

}

void RadixSort(vector<int>& v, int numDigits){
    vector<queue<int> > QA(10);
    for(int k=0; k < numDigits; k++){
	QA = ItemsToQueues(v, k);
	v = QueuesToArray(QA, v.size());
    }

    
}



void PrintVector(const vector<int>& L){
    vector<int> temp = L;

    for (int i=0; i<L.size(); i++){
	cout << L.at(i) << " ";
    }
    cout << endl;

}
