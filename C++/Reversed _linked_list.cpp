#include <iostream>
using namespace std;

class ListNode {  //class of listNode
    public:
        int val;                //value sorted in node
        ListNode *next;             //pointer to next node
        ListNode(int x) : val(x), next(NULL) {}   //constructor
};

//Add new node to the end of the list and updates the end pointer
void insert_at_tail(ListNode* &end,ListNode* &head,int val){
    ListNode* n = new ListNode(val);        //new node

    if(head==NULL){    //if the linked list is element , head and end pointer will points towards 1st node
        head=n;
        end=n;          //this condition hits only one time
        return;
    }
    end->next=n;        //add pointer to the new node 
    end=n;              //update end pointer
}

//reverses the linked list and updates pointer accordingly
void Make_Reversed_Linked_List(ListNode* &end,ListNode* &head){
    ListNode* temp=head;    //current node
    ListNode* prev=NULL;    //previous node
    ListNode* next=NULL;     //next node
    ListNode* delta =head;    //pointer to current head

    while(temp!=NULL){
        next=temp->next;        //change pointer to previous node instead of next node 
        temp->next=prev;        //to reverse the linked list
        prev=temp;
        temp=next;
    }
    head=prev;          //update head pointer
    end=delta;         //update end pointer
    end->next=NULL;      //end node points to nothing
}

//function to print the linked list (currently of no use but can be used to check our output)
void print(ListNode* head){         
    ListNode* temp=head;
    while(temp!=NULL){              //check condition if pointer to next element is null then terminates it
        cout<<temp->val<<" ";       //print node then move to next node
        temp=temp->next;
    }
}

int main(){
    
    cout<<"Enter number of nodes in Linked List"<<endl;
    int n;              //taking input of number of nodes
    cin>>n;

    if( n==0){              //terminates the code if total nodes = 0
        cout<<"Size of linked list is 0, please enter size greater than 0 ";
        return 0;
    }

    cout<<"Enter elements of linked list"<<endl; 
    ListNode* head=NULL;   //head pointer
    ListNode* end = NULL;   //end pointer(initially both null)

    for (int i=0;i<n;i++){
        int a;                          //input the value saved in node
        cin>>a;
        insert_at_tail(end,head,a);     //adds node to tail of linked list
    }

    Make_Reversed_Linked_List(end,head);        //reverses the linked list and also update head and end pointer 
                                                //accordingly
    cout<<"Reversed Linked list  : ";
    print(head);
    
    
    return 0;
}